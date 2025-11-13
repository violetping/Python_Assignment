# ===========================================================
# Name: Gaurav Kumar
# Roll No: 2501660010
# Program: BCA (Cyber Security)
# Course Code: ETCCCPP103
# Course Name: Problem Solving with Python
# Faculty: Ms. Neha Kaushik
# Session: 2025-26 | Semester: I
# Assignment: Unit-2 Mini Project
# Title: Library Inventory & Borrowing System
# ===========================================================

import csv  # for optional CSV persistence 
from typing import Dict, List  # type hints for readability

# -----------------------------
# In-memory data structures
# -----------------------------
books: Dict[str, Dict[str, object]] = {}  # { "B101": {"title": "...", "author": "...", "copies": int} }
borrowed: Dict[str, str] = {}             # { "StudentName": "BookID" }

# -----------------------------
# Persistence (Bonus)
# -----------------------------
BOOKS_CSV = "books.csv"
BORROWED_CSV = "borrowed.csv"

def save_to_csv():
    # Save books
    with open(BOOKS_CSV, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)  # csv.writer writes rows as lists
        writer.writerow(["book_id", "title", "author", "copies"])
        for bid, data in books.items():
            writer.writerow([bid, data["title"], data["author"], data["copies"]])
    # Save borrowed
    with open(BORROWED_CSV, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["student", "book_id"])
        for student, bid in borrowed.items():
            writer.writerow([student, bid])

def load_from_csv():
    # Load books if file exists
    try:
        with open(BOOKS_CSV, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)  # csv.reader returns iterable rows
            header = next(reader, None)
            for row in reader:
                if len(row) != 4:
                    continue
                bid, title, author, copies = row
                books[bid] = {"title": title, "author": author, "copies": int(copies)}
    except FileNotFoundError:
        pass
    # Load borrowed if file exists
    try:
        with open(BORROWED_CSV, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            for row in reader:
                if len(row) != 2:
                    continue
                student, bid = row
                borrowed[student] = bid
    except FileNotFoundError:
        pass

# -----------------------------
# Formatting helpers
# -----------------------------
def print_header(title: str):
    print("\n" + title)
    print("-" * len(title))

def print_books_table():
    # Column widths for alignment using f-strings: < left, > right 
    print_header("Books")
    if not books:
        print("No books in inventory.")
        return
    print(f"{'Book ID':<8} | {'Title':<30} | {'Author':<20} | {'Copies':>6}")
    print("-" * 72)
    for bid, data in books.items():
        print(f"{bid:<8} | {data['title']:<30} | {data['author']:<20} | {data['copies']:>6}")
    print()

def print_borrowed_list():
    print_header("Borrowed Books")
    if not borrowed:
        print("No active borrowings.")
        return
    # List comprehension requirement [student -> book]
    borrowed_list = [f"{student} -> {book_id}" for student, book_id in borrowed.items()]
    for line in borrowed_list:
        print(line)
    print()

# -----------------------------
# Core functions (Tasks 2–5)
# -----------------------------
def add_book():
    print_header("Add Book")
    bid = input("Enter Book ID (e.g., B101): ").strip()
    if not bid:
        print("Book ID cannot be empty.")
        return
    if bid in books:
        print("Book ID already exists.")
        return
    title = input("Enter Title: ").strip()
    author = input("Enter Author: ").strip()
    try:
        copies = int(input("Enter Copies (integer >= 0): ").strip())
        if copies < 0:
            raise ValueError
    except ValueError:
        print("Invalid copies number.")
        return
    books[bid] = {"title": title, "author": author, "copies": copies}
    print(f"Book {bid} added successfully.\n")

def search_by_id(bid: str):
    # Function-based searching
    return books.get(bid)

def search_by_title_substring(substr: str) -> List[str]:
    substr_lower = substr.lower()
    matches = []
    for bid, data in books.items():
        if substr_lower in data["title"].lower():
            matches.append(bid)
    return matches

def search_book():
    print_header("Search Book")
    print("1) By Book ID")
    print("2) By Title (substring)")
    choice = input("Choose option: ").strip()
    if choice == "1":
        bid = input("Enter Book ID: ").strip()
        record = search_by_id(bid)
        if record:
            print("Book Found")
            print(f"{'Book ID':<8} | {'Title':<30} | {'Author':<20} | {'Copies':>6}")
            print("-" * 72)
            print(f"{bid:<8} | {record['title']:<30} | {record['author']:<20} | {record['copies']:>6}")
        else:
            print("Book Not Found")
    elif choice == "2":
        q = input("Enter title substring: ").strip()
        bids = search_by_title_substring(q)
        if not bids:
            print("Book Not Found")
        else:
            print("Book Found")
            print(f"{'Book ID':<8} | {'Title':<30} | {'Author':<20} | {'Copies':>6}")
            print("-" * 72)
            for bid in bids:
                data = books[bid]
                print(f"{bid:<8} | {data['title']:<30} | {data['author']:<20} | {data['copies']:>6}")
    else:
        print("Invalid choice.")
    print()

def borrow_book():
    print_header("Borrow Book")
    student = input("Enter student name: ").strip()
    bid = input("Enter Book ID: ").strip()
    data = books.get(bid)
    if not data:
        print("Error: Book does not exist.")
        return
    if data["copies"] <= 0:
        print("Error: No copies available.")
        return
    # If the student already borrowed a book, enforce one-at-a-time simple rule
    if student in borrowed:
        print("Error: Student already has a borrowed book.")
        return
    data["copies"] -= 1
    borrowed[student] = bid
    print(f"Borrow confirmed: {student} -> {bid}")
    print()

def return_book():
    print_header("Return Book")
    student = input("Enter student name: ").strip()
    bid = input("Enter Book ID: ").strip()
    # Validate borrowing record
    current = borrowed.get(student)
    if not current:
        print("Error: No active borrowing found for this student.")
        return
    if current != bid:
        print("Error: Provided Book ID does not match borrowed record.")
        return
    # Increment copies and remove borrowing
    if bid in books:
        books[bid]["copies"] += 1
    borrowed.pop(student, None)
    print("Return successful.")
    # Show borrowed list via list comprehension
    print_borrowed_list()

# -----------------------------
# Seed data for minimum checks
# -----------------------------
def seed_minimum_books():
    # Ensure at least 5 books exist for the submission checklist
    if len(books) >= 5:
        return
    default = {
        "B101": {"title": "Python Basics", "author": "Guido", "copies": 5},
        "B102": {"title": "DSA", "author": "Cormen", "copies": 3},
        "B103": {"title": "Clean Code", "author": "Robert Martin", "copies": 4},
        "B104": {"title": "Fluent Python", "author": "Luciano Ramalho", "copies": 2},
        "B105": {"title": "Automate Boring Stuff", "author": "Al Sweigart", "copies": 6},
    }
    for k, v in default.items():
        if k not in books:
            books[k] = dict(v)

# -----------------------------
# Menu loop (Tasks 1 & 6)
# -----------------------------
def main():
    # Optional load for bonus
    load_from_csv()
    seed_minimum_books()

    # Welcome screen and menu
    while True:
        print("\nWelcome to Library Book Manager")
        print("-------------------------------")
        print("1) Add Book")
        print("2) View Books")
        print("3) Search Book")
        print("4) Borrow Book")
        print("5) Return Book")
        print("6) View Borrowed List")
        print("7) Save to CSV")
        print("8) Load from CSV")
        print("9) Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            print_books_table()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print_borrowed_list()
        elif choice == "7":
            save_to_csv()
            print("Saved to CSV.")
        elif choice == "8":
            load_from_csv()
            print("Loaded from CSV.")
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

