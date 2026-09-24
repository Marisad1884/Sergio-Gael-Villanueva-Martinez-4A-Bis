class library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def borrow_book(self, book_id, user_id):
        book = next((book for book in self.books if book.id == book_id), None)
        user = next((user for user in self.users if user.id == user_id), None)

        if book is None or user is None or not book.available:
            return False

        book.available = False
        book.borrowed_by = user
        return True

    def return_book(self, book_id):
        book = next((book for book in self.books if book.id == book_id), None)

        if book is None or book.available:
            return False

        book.available = True
        book.borrowed_by = None
        return True

    def show_books(self):
        for book in self.books:
            print(book.show_book_info())

    def show_users(self):
        for user in self.users:
            print(user.show_user_info())