from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

# Get database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "fastapi_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

def get_db_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

@app.get("/")
def read_root():
    return {"message": "FastAPI is running on port 8003!"}

@app.get("/db-check")
def db_check():
    try:
        conn = get_db_connection()
        conn.close()
        return {"message": "Database connection successful!"}
    except Exception as e:
        return {"Database connection failed. Reason: ": str(e)}

