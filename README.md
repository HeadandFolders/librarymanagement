# Library Management System
A command-line application for managing a book library. The program allows you to:
* Add books
* Remove books
* Search for books by title, author, or year
* View all books
* Update the status of books ("в наличии" or "выдана")
## Features
-Add New Book
  Add a new book by specifying its title, author, and publication year.

-List All Books
  Display a list of all books, including their ID, title, author, year, and current status.

-Remove a Book
  Remove a book from the library by its ID.

-Find a Book
  Search for a book by its title, author, or publication year.

-Change Book Status
  Update the status of a book ("в наличии" or "выдана") by specifying its ID.

Data Persistence
All data is stored in a JSON file (library.json) for persistence between sessions.

## Installation
Clone or download the project.
Ensure Python 3.x is installed on your machine.

Usage
Run the script from the terminal using Python:

## Commands
Add a Book

```bash
python bookstore.py -a "Book Title" "Author Name" 2000
```
Example:

```bash
python bookstore.py -a "Война и мир" "Лев Толстой" 1869
```
List All Books

```bash
python bookstore.py -l
```
Remove a Book
```bash
python bookstore.py -r <book_id>
```
Example:

```bash
python bookstore.py -r 1
```
Find a Book
```bash
python bookstore.py -f "Search Query"
```
Example:
```bash
python bookstore.py -f "Лев Толстой"
```
Change Book Status
```bash
python bookstore.py -c <book_id> <new_status>
```
Example:
```bash
python bookstore.py -c 2 "выдана"
```
Examples
Add a Book
Command:
```bash
python bookstore.py -a "The Great Gatsby" "F. Scott Fitzgerald" "1925"
```
Output:

```python
Book successfully added to library
```
List All Books
Command:

```bash
python bookstore.py -l
```
Output:
```python
-----------------------------------
|📖  LIST OF BOOKS IN LIBRARY   📖|
-----------------------------------
ID: 1, Title: The Great Gatsby, Author: F. Scott Fitzgerald, Year: 1925, Status: в наличии
-----------------------------------
```
Remove a Book
Command:

```bash
python bookstore.py -r 1
```
Output:

```python
Book {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925, 'status': 'в наличии'} removed successfully.
```
Find a Book
Command:

```bash
python bookstore.py -find "F. Scott Fitzgerald"
```
Output:
```python
Book found.
Book info: 
ID: 1, Title: The Great Gatsby, Author: F. Scott Fitzgerald, Year: 1925, Status: в наличии
```
Change Book Status
Command:

```bash
python bookstore.py -c 1 "выдана"
```
Output:

```python
Book status changed successfully.
```
## File Structure
```plaintext
📂 LibraryManagementSystem
├── app.py           # Main application script
├── library.json     # Data file to store library books
└── README.md        # Documentation
```

License
This project is licensed under the MIT License.
