import sqlite3
import pandas as pd
import pathlib

db_file=pathlib.Path("project.db")

def insert_data_from_csv():
    try:
      #  author_data_path="C:\\RaginiWorkArea\\sourcecode\\practice_with_sql+python\\data\\authors.csv"  #pathlib.Path("data","authors.csv")
        author_data_path=pathlib.Path("data","authors.csv")
        book_data_path=pathlib.Path("data","books.csv")

        authors_df=pd.read_csv(author_data_path)
        books_df=pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # using pandas dataframe to_sql() method to insert data
            authors_df.to_sql("authors",conn,if_exists="replace", index=False)
            books_df.to_sql("books",conn,if_exists="replace", index=False)
            print("data inserted successfully")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("There is an error inserting data from csv:",e)


def main():
    insert_data_from_csv()

if __name__=="__main__":
    main()

        





          

