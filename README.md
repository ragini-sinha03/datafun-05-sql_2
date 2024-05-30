# datafun-05-sql_2

## created project and then coned to the machine:

#### I created a new repository on GitHub.
#### I clicked READ.md file.
#### I opened File Explorer on my computer and opened the terminal on that file.
#### I cloned the repository to that folder by using the following command:
gitbash

git clone site_URL


## Added files:

#### I then added a .py file to work in, a requirements.txt to hold the required project modules, a .venv to act as a virtual environment, a .gitignore to hold .venv and .vscode file. 

## Created Virtual Environment

#### On windows, I created a project virtual environment in the .venv folder. 
py -m venv .venv
.venv\Scripts\Activate

## Installed required packages into local project virtual environment

#### I installed all the required packages.
py -m pip install -r requirements.txt
py -m pip freeze > requirements.txt


## Git add and commit

#### I added, commit and push the file to the web by using following command.
git add .
git commit -m "add .gitignore"
git push

## Added data folder and .csv

#### I manually added a data folder to the project foler, then added two .csv files in VS Code.

## Created a db_initialize_ragini.py file

#### I created a database and create_tables.sql

## Created a db_operations_ragini.py file

#### I created thsi database to insert data into the file. The file when called added the held files to the database in the respective categories. 

## created tables
#### I created tables by using following code:
CREATE TABLE authors(
author_id TEXT PRIMARY KEY,
first_name TEXT,
last_name TEXT
);

CREATE TABLE books(
book_id TEXT PRIMARY KEY,
title TEXT,
year_published INTEGER,
author_id TEXT,
FOREIGN KEY(author_id) REFERENCES authors(author_id)
);

## Performed inner_join function
#### I use inner join to combine two tables. The inner join matches authors.author_id with books.author_id.So, only the rows with matching author_id in both authors and books tables are returned. I use the following code:

    SELECT books.title, authors.first_name, authors.last_name
    FROM authors
    INNER JOIN books ON authors.author_id = books.author_id;
    
## Performed query_fetchall function
#### I performed fetchall() to retrive all the values of authors table. 

## Performed query_aggregation function
#### I performed query aggregation using the group by clause. I executed a group by clause to group the authors by their last_name and then counted it. 


