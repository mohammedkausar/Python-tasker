from psycopg2.extras import DictCursor

from config.db_config import get_db_config
import psycopg2
from models.task_model import Task,TaskInDB

cfg = get_db_config()

def create_task(task: Task):
    try:
        with psycopg2.connect(**cfg) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                create_script = 'INSERT INTO task(title, description, completed) VALUES(%s,%s,%s) RETURNING id'
                cur.execute(create_script,(task.title,task.description,task.completed))
                task_id = cur.fetchone()['id']
                return TaskInDB(id=task_id, **task.model_dump())
    except Exception as e:
        return e
    finally:
        conn.close()