import sqlite3

#conn=sqlite3.connect("project.db")
#cursor=conn.cursor()
#sql="select * from authors"
#cursor.execute(sql)
#results=cursor.fetchall()
#print(results)


import sqlite3

def fetch_all_authors(db_name):
    # Connect to the SQLite database
    conn = sqlite3.connect("project.db")
    cursor = conn.cursor()
    
    # Execute the SQL query
    sql = "SELECT * FROM authors"
    cursor.execute(sql)
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Close the connection
    conn.close()
    
    return results

def main():
    # Database name
    db_name = "project.db"
    
    # Fetch authors from the database
    authors = fetch_all_authors(db_name)
    
    # Print the results
    print(authors)

# Call the main function
if __name__ == "__main__":
    main()
