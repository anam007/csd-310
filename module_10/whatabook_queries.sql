-- Anamanno Umanah
-- Moudule 12
-- Whatabook queries



-- select query to veiw wishlist contents
SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist
    INNER JOIN user ON wishlist.user_id = user.user_id
    INNER JOIN book ON wishlist.book_id = book.book_id
WHERE user.user_id = 1;


-- select query to display store location 
SELECT store_id, locale FROM store;

-- Select to display library for books for whatabook
SELECT book_id, book_name, author, details FROM book;

-- query to veiw books not in users wishlist
SELECT book_id, book_name, author, details
FROM book
WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = 1)

-- insert statement to add book to user wishlist
INSERT INTO wishlist (user_id, book_id)
    VALUES (1, 9)


-- query to delect book from wishlist
DELETE FROM wishlist WHERE user_id = 1 AND book_id = 9;
