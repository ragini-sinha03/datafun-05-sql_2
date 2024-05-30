import sqlite3
import pathlib

db_file = "project.db"

def inner_join():
    """Function to read and execute SQL statements to perform INNER JOIN and display the results"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("inner_join.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            rows = cursor.fetchall()
            # Display the joint data
            for row in rows:
                print(f"Title: {row[1]}, Author's Last Name: {row[2]}")
            print("Query executed successfully.")
    except IOError as e:
        print("Error in executing query:", e)

def main():
    # Create the query_join.sql file
    sql_query = '''
    SELECT books.title, authors.first_name, authors.last_name
    FROM authors
    INNER JOIN books ON authors.author_id = books.author_id;
    '''
    
    with open("inner_join.sql", "w") as file:
        file.write(sql_query)

    # Call the inner_join function
    inner_join()

if __name__ == "__main__":
    main()
