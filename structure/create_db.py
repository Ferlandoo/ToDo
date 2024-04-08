from sqlalchemy import create_engine, text

def create_database():
    engine = create_engine('mysql+pymysql://root:1234@localhost:3306')
    with engine.connect() as connection:
        connection.execute(text("CREATE DATABASE IF NOT EXISTS todo_db"))
