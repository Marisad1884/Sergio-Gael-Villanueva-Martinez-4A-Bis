from books import book
from users import user
from library import library


# Create instances of the classes
# Para remarcar estas son Instancias, o sea que se crean a traves de las clases
book1 = book(1, "Red riding hood", "Charles Perrault", "Hachette Livre")
book2 = book(2, "Alice in Wonderland", "Lewis Carroll", "Macmillan Publishers")

user1 = user(1, "Scott Pilgrim")
user2 = user(2, "Knives chau")

# Create a library instance
lib = library()

# Add books and users to the library
lib.add_book(book1)
lib.add_book(book2)
lib.add_user(user1)
lib.add_user(user2)

# Display information about books and users
print("Books in the library:")
lib.show_books()

print("\nUsers in the library:")
lib.show_users()

print("\nBorrowing book 1:", lib.borrow_book(1, 1))
print("Trying to borrow book 1 again:", lib.borrow_book(1, 2))
print("Returning book 1:", lib.return_book(1))
#Requirements
#1 the system must allow to registers books
#2 The system must allow to register users
#3 The system must allow to be borrow by a user
#4 A book that has already been borrowed cannot be borrowed again
#5 The system must allow a book to be returned

 