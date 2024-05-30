import sqlite3

def create_authors_table_and_insert_data(conn):
    cursor = conn.cursor()
    
    # Create the authors table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS authors (
        author_id TEXT PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL
    );
    ''')

    # Insert data into the authors table
    authors_data = [
        ('10f88232-1ae7-4d88-a6a2-dfcebb22a596', 'Harper', 'Lee'),
        ('c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70', 'George', 'Orwell'),
        ('e0b75863-866d-4db4-85c7-df9bb8ee6dab', 'F. Scott', 'Fitzgerald'),
        ('7b144e32-7ff4-4b58-8eb0-e63d3c9f9b8d', 'Aldous', 'Huxley'),
        ('8d8107b6-1f24-481c-8a21-7d72b13b59b5', 'J.D.', 'Salinger'),
        ('0cc3c8e4-e0c0-482f-b2f7-af87330de214', 'Ray', 'Bradbury'),
        ('4dca0632-2c53-490c-99d5-4f6d41e56c0e', 'Jane', 'Austen'),
        ('16f3e0a1-24cb-4ed6-a50d-509f63e367f7', 'J.R.R.', 'Tolkien'),
        ('06cf58ab-90f1-448d-8e54-055e4393e75c', 'J.R.R.', 'Tolkien'),
        ('6b693b96-394a-4a1d-a4e2-792a47d7a568', 'J.K.', 'Rowling')
    ]

    cursor.executemany('''
    INSERT INTO authors (author_id, first_name, last_name) VALUES (?, ?, ?);
    ''', authors_data)
    
    conn.commit()

def query_aggregation(conn):
    cursor = conn.cursor()
    sql = '''
    SELECT last_name, COUNT(*) AS author_count
    FROM authors
    GROUP BY last_name;
    '''
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    # Display the aggregated data
    for row in rows:
        print(f"Last Name: {row[0]}, Author Count: {row[1]}")
    
    print("Query executed successfully.")

def main():
    db_file = "project.db"
    conn = sqlite3.connect(db_file)

    # Create the authors table and insert data
    create_authors_table_and_insert_data(conn)

    # Perform query aggregation
    query_aggregation(conn)
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
