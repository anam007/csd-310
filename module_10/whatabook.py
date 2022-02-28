#Anamanno Umanah
#Module 12
#02/25/2022

#WhatABook Project



import sys
import mysql.connector
from mysql.connector import errorcode 

""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MyRootPassword",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}


#diplay menu
def show_menu():
    print ("--- MAIN MENU ---")

    print (" 1. View Books\n  2. Store Locations\n  3. View My Account\n  4. Close Program")
    try:
        option = int(input(" Please select menu option: eg, 1 to view books\n")) 

        return option
    except ValueError:
        print("\n  Invalid number, program terminated...\n")
        sys.exit(0)

#disply books
def show_books(_cursor):
    _cursor.execute ("SELECT book_id, book_name, author, details FROM book")

    #get results 
    books = _cursor.fetchall()

    print ('\n --- DISPLAYING BOOKS ---')
    for book in books:
        print ("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))




#display location
def show_location (_cursor):
    _cursor.execute ('SELECT store_id, locale FROM store;')

    #get results
    locations = _cursor.fetchall()
    
    print ('\n--- DISPLAYING LOCATIONS ---')
    for location in locations:
        print ("  Locale: {}\n".format(location[1]))




#validate user
def validate_user ():
    """validate the user id"""

    user_id = int(input('Please enter user ID number'))

    return user_id




#display user account menu
def show_account_menu():
    print ('\n--- User Menu ---')
    print ('   1. Wishlist\n       2. Add Book\n       3. Main Menu')    

    user_option = int(input ('Please enter menu option number\n '))

    return user_option


#display wishlist books
def show_wishlist (_cursor, _user_id):
    """ query database for list of books added to the users wishlist """

    _cursor.execute ('SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author'
                    'FROM wishlist' +
                    'INNER JOIN user ON wishlist.user_id = user.user_id'+
                    'INNER JOIN book ON wishlist.book_id = user.book_id'+
                    'WHERE user.user_id = {}'.format(_user_id))

    wishlist = _cursor.fetchall()

    print ('\n --- DISPLAYING WISHLIST BOOKS ---')
    for book in wishlist:
        print ('        Book Name: {}\n        Author: {}\n'.format(book[4], book[5]))





#display books to add
def show_books_to_add (_cursor, _user_id):
    """ query database for list of books not in the users wishlist """

    not_in_wishlist = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    _cursor.execute(not_in_wishlist) 
    print (not_in_wishlist) 
    

    add_books = _cursor.fetchall()

    print ('\n--- AVAILABLE BOOKS ---')
    for book in add_books:
        print ('  Book Id: {}\n        Book Name: {}\n'.format(book[0], book[1]))




#add books to wishlist 
def add_book_to_wishlist (_cursor, user_id, book_id):
    _cursor.execute ('INSERT INTO wishlist (user_id, book_id) VALUES ({}, {})'.format(user_id, book_id))       



try:
#connect to database
    db = mysql.connector.connect(**config) 

    cursor = db.cursor() 


    print ('WhatABook Application!')




    # display the main menu 
    user_selection = show_menu()

    # while the user's selection is not 4
    while user_selection != 4:

        #if user selects option 1, call the show_books method and display the books
        if user_selection == 1:
            show_books(cursor)

        # if user selects option 2, call the show_locations method and display the locations
        if user_selection == 2:
            show_location(cursor)

        #if user selects option 3, call the validate_user method to validate the provided user_id 
        #then call the show_account_menu() to display the account settings menu
        if user_selection == 3:
            the_user_id = validate_user()
            account_option = show_account_menu()

            # while account option does not equal 3
            while account_option != 3:

                # if the user selects option 1, call the show_wishlist() method to display the current users 
                # configured wishlist items 
                if account_option == 1:
                    show_wishlist(cursor, the_user_id)

                # if the user selects option 2, call the show_books_to_add function to show the user 
                # the books not currently configured in the users wishlist
                if account_option == 2:

                    # show the books not currently configured in the users wishlist
                    show_books_to_add(cursor, the_user_id)

                    # get the entered book_id 
                    book_id = int(input("\n        Enter the id of the book you wish to add: "))
                    
                    # add the selected book the users wishlist
                    add_book_to_wishlist(cursor, the_user_id, book_id)

                    # commit the changes to the database 
                    db.commit() 

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))

                #if the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please try again...")

                # show the account menu 
                account_option = show_account_menu()
        
        # if the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid option, please try again...")
            
        # show the main menu
        user_selection = show_menu()

    print("\n\n  Program terminated...")

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()