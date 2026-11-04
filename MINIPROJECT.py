class Book:

  def __init__(self, book_id, title, author):
    self.book_id = book_id
    self.title = title
    self.author = author
    self.is_issued = False

  def __str__(self):
    status = "Issued" if self.is_issued else "Available"
    return f"[{self.book_id}] '{self.title}' by {self.author} — Status: {status}"


class Library:

  def __init__(self):
    self.books = {}

  def add_book(self, book_id, title, author):
    if book_id in self.books:
      print(" Error: Book ID already exists!")
    else:
      self.books[book_id] = Book(book_id, title, author)
      print(" Book added successfully!")

  def view_books(self):
    if not self.books:
      print(" The library has no books currently.")
      return
    print("\n--- Library Catalog ---")
    for book in self.books.values():
      print(book)

  def issue_book(self, book_id):
    if book_id in self.books:
      if not self.books[book_id].is_issued:
        self.books[book_id].is_issued = True
        print(" Book issued successfully!")
      else:
        print(" This book is already issued out.")
    else:
      print(" Error: Book ID not found.")

  def return_book(self, book_id):
    if book_id in self.books:
      if self.books[book_id].is_issued:
        self.books[book_id].is_issued = False
        print(" Book returned successfully!")
      else:
        print(" This book was not marked as issued.")
    else:
      print(" Error: Book ID not found.")


def main():
  library = Library()

  # Pre-loaded catalog with popular books
  initial_books = [
      ("101", "The Alchemist", "Paulo Coelho"),
      ("102", "Atomic Habits", "James Clear"),
      ("103", "To Kill a Mockingbird", "Harper Lee"),
      ("104", "1984", "George Orwell"),
      ("105", "The Great Gatsby", "F. Scott Fitzgerald"),
      ("106", "Pride and Prejudice", "Jane Austen"),
      ("107", "Harry Potter and the Sorcerer's Stone", "J.K. Rowling"),
      ("108", "The Hobbit", "J.R.R. Tolkien"),
  ]

  for b_id, title, author in initial_books:
    library.add_book(b_id, title, author)

  while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
      b_id = input("Enter Book ID: ").strip()
      title = input("Enter Book Title: ").strip()
      author = input("Enter Author Name: ").strip()
      library.add_book(b_id, title, author)

    elif choice == "2":
      library.view_books()

    elif choice == "3":
      b_id = input("Enter Book ID to issue: ").strip()
      library.issue_book(b_id)

    elif choice == "4":
      b_id = input("Enter Book ID to return: ").strip()
      library.return_book(b_id)

    elif choice == "5":
      print("Exiting system. Goodbye!")
      break

    else:
      print(" Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
  main()
