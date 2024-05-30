import sqlite3

def create_books_table_and_insert_data(conn):
    cursor = conn.cursor()
    
    # Create the books table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        year_published INTEGER NOT NULL,
        author_id TEXT NOT NULL
    );
    ''')

    # Insert data into the books table
    books_data = [
        ('d6f83870-ff21-4a5d-90ab-26a49ab6ed12', 'To Kill a Mockingbird', 1960, '10f88232-1ae7-4d88-a6a2-dfcebb22a596'),
        ('0f5f44f7-44d8-4f49-b8c4-c64d847587d3', '1984', 1949, 'c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70'),
        ('f9d9e7de-c44d-4d1d-b3ab-59343bf32bc2', 'The Great Gatsby', 1925, 'e0b75863-866d-4db4-85c7-df9bb8ee6dab'),
        ('38e530f1-228f-4d6e-a587-2ed4d6c44e9c', 'Brave New World', 1932, '7b144e32-7ff4-4b58-8eb0-e63d3c9f9b8d'),
        ('c2a62a4b-cf5c-4246-9bf7-b2601d542e6d', 'The Catcher in the Rye', 1951, '8d8107b6-1f24-481c-8a21-7d72b13b59b5'),
        ('3a1d835c-1e15-4a48-8e8c-b12239604e98', 'Fahrenheit 451', 1953, '0cc3c8e4-e0c0-482f-b2f7-af87330de214'),
        ('c6e67918-e509-4a6b-bc3a-979f6ad802f0', 'Pride and Prejudice', 1813, '4dca0632-2c53-490c-99d5-4f6d41e56c0e'),
        ('be951205-6cc2-4b3d-96f1-7257b8fc8c0f', 'The Hobbit', 1937, '16f3e0a1-24cb-4ed6-a50d-509f63e367f7'),
        ('dce0f8f2-d3ed-48a9-b8ff-960b6baf1f6f', 'The Lord of the Rings', 1954, '06cf58ab-90f1-448d-8e54-055e4393e75c'),
        ('ca8e64c3-1e67-47f5-82cc-3e4e30f63b75', "Harry Potter and the Philosopher's Stone", 1997, '6b693b96-394a-4a1d-a4e2-792a47d7a568')
    ]

    cursor.executemany('''
    INSERT INTO books (book_id, title, year_published, author_id) VALUES (?, ?, ?, ?);
    ''', books_data)
    
    conn.commit()

def query_aggregation(conn):
    cursor = conn.cursor()
    sql = '''
    SELECT author_id, COUNT(*) AS book_count
    FROM books
    GROUP BY author_id;
    '''
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    # Display the aggregated data
    for row in rows:
        print(f"Author ID: {row[0]}, Book Count: {row[1]}")
    
    print("Query executed successfully.")

def main():
    db_file = "project.db"
    conn = sqlite3.connect(db_file)

    # Create the books table and insert data
    create_books_table_and_insert_data(conn)

    # Perform query aggregation
    query_aggregation(conn)
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
