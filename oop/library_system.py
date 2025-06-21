# library_system.py

class Book:
    """
    Base class for all types of books in the library system.
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the Book.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived class for electronic books, inheriting from Book.
    Attributes:
        file_size (int): The size of the EBook file in KB.
    """
    def __init__(self, title, author, file_size):
        """
        Initializes a new EBook instance.
        Args:
            title (str): The title of the EBook.
            author (str): The author of the EBook.
            file_size (int): The size of the EBook file in KB.
        """
        super().__init__(title, author)  # Call the base class's __init__ method
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the EBook, including file size.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived class for print books, inheriting from Book.
    Attributes:
        page_count (int): The number of pages in the PrintBook.
    """
    def __init__(self, title, author, page_count):
        """
        Initializes a new PrintBook instance.
        Args:
            title (str): The title of the PrintBook.
            author (str): The author of the PrintBook.
            page_count (int): The number of pages in the PrintBook.
        """
        super().__init__(title, author)  # Call the base class's __init__ method
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation of the PrintBook, including page count.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    Class demonstrating composition, managing a collection of various book types.
    Attributes:
        books (list): A list to store instances of Book, EBook, and PrintBook.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book (Book, EBook, or PrintBook instance) to the library's collection.
        Args:
            book (Book): An instance of Book or its derived classes.
        """
        if isinstance(book, Book): # Ensure that only Book objects or its children are added
            self.books.append(book)
        else:
            print(f"Cannot add {type(book).__name__}. Only Book instances can be added to the library.")

    def list_books(self):
        """
        Prints the details of each book currently in the library.
        """
        if not self.books:
            print("The library is currently empty.")
            return

        # Removed the line "print("Listing all books in the library:")"
        for book in self.books:
            print(book) # This will call the __str__ method of each book object
