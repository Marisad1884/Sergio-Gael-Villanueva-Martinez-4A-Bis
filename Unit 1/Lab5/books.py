class book:
    def __init__(self, id_book, name, author, editorial):
        self.id = id_book
        self.name = name
        self.author = author
        self.editorial = editorial
        self.available = True
        self.borrowed_by = None

    def show_book_info(self):
        return f"Book ID: {self.id}, Author: {self.author}, Editorial: {self.editorial}, Available: {self.available}"