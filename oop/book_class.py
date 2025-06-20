class Book:
    def __init__(self, title, author, year):
        """Constructor: Initializes the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """String representation: For user-friendly printing."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation: Used for debugging and recreation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor: Called when the object is deleted."""
        print(f"Deleting {self.title}")
