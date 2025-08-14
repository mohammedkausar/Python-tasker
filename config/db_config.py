import os
from dotenv import  load_dotenv

load_dotenv()

def get_db_config():
    return {
        "host":os.getenv("PG_HOST","localhost"),
        "port": int(os.getenv("PG_PORT",5432)),
        "dbname": os.getenv("PG_DB"),
        "user":os.getenv("PG_USER"),
        "password": os.getenv("PG_PASSWORD")
    }