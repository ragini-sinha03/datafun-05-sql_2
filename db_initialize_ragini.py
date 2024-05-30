'''this project integrates python and sql, focusing on database interactions using sqlite. This project introduces logging, a useful tool for debugging and monitoring projects, and involves creating and managing a database, building a schema, and performing various sql opefrations.
'''

import sqlite3
import pandas as pd
import pathlib
#import logging

db_file=pathlib.Path("project.db")

# create a databse
def create_database():
    """this function will create a database"""
    
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("database created successfully")
    except sqlite3.Error as e:
        print("error creating the database:",e)


def create_tables():
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file=pathlib.Path("create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script=file.read()
            conn.executescript(sql_script)
    except IOError as e:
        print("table created successfully")

def main():
    create_database()
    create_tables()

if __name__=="__main__":
    main()








