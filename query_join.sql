
    SELECT books.title, authors.first_name, authors.last_name
    FROM authors
    INNER JOIN books ON authors.author_id = books.author_id;
    