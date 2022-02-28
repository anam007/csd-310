-- drop user if exist 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create pysport_user and grant them all priviledges to the pysport database
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MyRootPassword';

-- grant all priviledges to the pysport database to user pysport_user on localhost
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop user if exist
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS store;

CREATE TABLE user (
    user_id     INT         NOT NULL    AUTO_INCREMENT,
    first_name  VARCHAR(75) NOT NULL,
    last_name   VARCHAR(75) NOT NULL,
    PRIMARY KEY (user_id)

);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_id)

);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

-- insert users info
INSERT INTO user (first_name, last_name)
    VALUES ('Richard', 'Sunday');

INSERT INTO user (first_name, last_name)
    VALUES ('Mike', 'Tuesday');

INSERT INTO user (first_name, last_name)
    VALUES ('Toney', 'Barns');


-- insert books info
INSERT INTO book(book_name, author, details)
    VALUES('Think Like a Man', 'Steve Harvey', 'A guide to having successful relationships');

INSERT INTO book(book_name, author, details)
    VALUES('The purple Hibiscus', 'Chimamanda Ngozi Adichie', 'The life of a eastern Nigerian Girl');

INSERT INTO book(book_name, author, details)
    VALUES('Half of a Yellow Sun', 'Chimamanda Ngozi Adichie', 'About the Nigerian Civil War');

INSERT INTO book(book_name, author, details)
    VALUES('The Thing Around Your Neck', 'Chimamanda Ngozi Adichie', 'Another Story from Chimamanda Ngozi Adichie');

INSERT INTO book(book_name, author, details)
    VALUES('Wahala', 'Nikki May', 'Story about three Anglo-Nigerian friends');

INSERT INTO book(book_name, author, details)
    VALUES('Atomic Habbits: An Easy & Proven Way to Build Good Habits & Break Bad ', 'James Clear', 'Build good habits, how to break the bad ones');

INSERT INTO book(book_name, author, details)
    VALUES('Born a Crime', 'Trevor Noah', 'The childhood stories of Trevor Noah');

INSERT INTO book(book_name, author, details)
    VALUES('Rich Dad Poor Dad', 'Robert Kiyosaki and Sharon Lechter', 'Improve your personal finances');

INSERT INTO book(book_name, author)
    VALUES('Lagoon', 'Nnedi Okorafor');


-- insert wishlist data
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Richard'), 
        (SELECT book_id FROM book WHERE book_name = 'Think Like a Man')
    );

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Mike'), 
        (SELECT book_id FROM book WHERE book_name = 'The Purple Hibiscus')
    );  
    
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Toney'), 
        (SELECT book_id FROM book WHERE book_name = 'Half of a Yellow Sun')
    );    
      
INSERT INTO store(locale )
    VALUES('5026 Garden Green Road, Houston, TX 78542');

