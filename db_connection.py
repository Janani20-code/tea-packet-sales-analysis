import sys
import pathlib
sys.path.append(str(pathlib.Path("C:/Users/janani/PycharmProjects/PythonProject1/password_mask").resolve()))
from password_security import get_decrypted_password
import mysql.connector

# 1. Database Connection
def connect_to_db():
    """Establish connection to MYSQL database"""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password=get_decrypted_password(),  # Replace with your MySQL password
            database='tea_business'
        )
        print("Successfully connected to database")
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        exit(1)