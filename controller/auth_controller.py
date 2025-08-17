import psycopg2
from models.user_model import UserCreate, UserInDB, UserLogin
from config.db_config import get_db_config
from psycopg2.extras import DictCursor
from utils.password_utils import hash_password,verify_password
from utils.auth_utils import create_access_token

cfg = get_db_config()
def register_user(user_data: UserCreate):
    try:
        with psycopg2.connect(**cfg) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT user_id FROM users where email=%s", (user_data.email,))
                if cur.fetchone():
                    return "USER ALREADY EXISTS"
                hashed = hash_password(user_data.password)
                cur.execute("INSERT INTO users(email,password) VALUES (%s,%s) RETURNING email", (user_data.email,hashed))
                created_email = cur.fetchone()[0]
                conn.commit()
                return {"email": created_email}
    except Exception as e:
        return str(e)
    finally:
        conn.close()

def login_user(login_data: UserLogin):
    try:
        with psycopg2.connect(**cfg) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT user_id,password from users where email=%s",(login_data.email,))
                result = cur.fetchone()
                if not result or not verify_password(login_data.password,result[1]):
                    raise Exception("INVALID CREDENTIAL")
                token = create_access_token({"sub": str(result[0])})
                return{"access_token": token}
    except Exception as e:
        return  str(e)
    finally:
        conn.close()