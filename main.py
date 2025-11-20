from library_books import library_books
from datetime import datetime, timedelta

#helpers
def _today():
    return datetime.today().date()

# helper to look up a book by ID
def _find_book(book_id):
    for book in library_books:
        # compare IDs as strings (upper/lower doesn't matter)
        if str(book["id"]).upper() == str(book_id).upper():
            return book
    return None

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
def view_available_books():
    """return the book dictionary if the ID matches"""
    available = []
    for book in library_books:
        if book["available"] is True:
            line = f'{book["id"]} | {book["title"]} by {book["author"]}'
            available.append(line)
    return available
# Output should include book ID, title, and author


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
def search_books(term):
    """search for your books by author or genre(don't worry about casing)"""
    term = term.lower().strip()
    if term == "":
        return[]
    
    results =[]
    for book in library_books:
        if term in book["author"].lower() or term in book["genre"].lower():
            results.append(book)
    return results
#this basically allows you to search up books based on its predesigned 
#genre or its author so its easier to locate
# Search should be case-insensitive
# Return a list of matching books


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
def check_book(book_id):
# If the book is available:
    """check the book out if it is available"""
    book = _find_book(book_id)
#   - Mark it unavailable
    if book is None:
        return f"no book with that ID'{book_id} found."
    
    if book["available"] is False:
        return f'"{book["title"]}" is already check out (due {book["due_date"]})0.'
    
#book is available --> checkout
    due_date = _today() + timedelta(days=14)
    book["available"] =False
    book["due_date"] = due_date.strftime("%Y-%m-%d")
    book["checkouts"] += 1
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

    return f'you checked out "{book["title"]}". it is due back on {book["due_date"]}.'




# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
def return_book(book_id):
    """return the book and mark it available again."""
    book = _find_book(book_id)

    if book is None:
        return f"sorry, no book with ID '{book_id}' found."

    if book["available"] is True:
        return f'"{book["title"]}" is already returned.'

    book["available"] = True
    book["due_date"] = None
    return f'"{book["title"]}" has been returned. thank you!'

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def list_overdue_books():
    """find all your overdue-books."""
    overdue = []
    today = _today()

    for book in library_books:
        if book["available"] is False and book["due_date"] is not None:
            due = datetime.strptime(book["due_date"], "%Y-%m-%d").date()
            if due < today:
                overdue.append(book)

    return overdue

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    print("\n--- available books ---")
    for b in view_available_books():
        print(b)

    print("\n--- search: 'fantasy' ---")
    for b in search_books("fantasy"):
        print(f'{b["id"]} | {b["title"]} by {b["author"]}')

    print("\n--- checkout 1 ---")
    print(check_book("1"))

    print("\n--- return 1 ---")
    print(return_book("1"))

    print("\n--- overdue books ---")
    overdue = list_overdue_books()
    if not overdue:
        print("no overdue books right now.")
    else:
        for b in overdue:
            print(f'{b["id"]} | {b["title"]} (due {b["due_date"]})')