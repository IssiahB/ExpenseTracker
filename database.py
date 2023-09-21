import sqlite3
from typing import Callable,Any

DB_NAME = "expense_tracker.db"

def connect():
    # Connect to the sqlite database
    return sqlite3.connect(DB_NAME)

def database_decorator(func: Callable[[sqlite3.Connection, Any], Any]) -> Callable:
    """
    Used to ensure that errors are handled properly when working with the sqlite database.
    Functions that use this decorator will be passed the database connection as their first argument 'db'.
    Doing this makes curtain that the database connection is always handled by this decorator and will always
    be closed to prevent data leaks.
    """
    def wrapper(*args, **kwargs):
        try:
            db = connect()
            func(db, args, kwargs)
        except sqlite3.Error as e:
            print(f'Error during database operation: {e}')
        finally:
            db.close()
    return wrapper

@database_decorator
def create_tables(db, args, kwargs):
    # Create the expenses and income table if it doesn't exist
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entries (
                   id INTEGER PRIMARY KEY,
                   type TEXT NOT NULL,
                   description TEXT NOT NULL,
                   date TEXT,
                   amount REAL,
                   reoccur INTEGER,
                   reoccur_type TEXT
        )
    """)
    db.commit()