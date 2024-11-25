import argparse
import os
import json
import webbrowser
import unittest
import doctest

library = "library.json"
def create_parser():
    parser = argparse.ArgumentParser(description="Command-line Book Store App")
    parser.add_argument("-a", "--add", nargs=3, metavar=("title/название_книги", "author/автор_книги", "year/год_издания"), help="Add a new book, give title, author and year in order")
    parser.add_argument("-l", "--list", action="store_true", help="List of all books")
    parser.add_argument("-r", "--remove", metavar="book_index", help="Remove a book by ID", type=int)
    parser.add_argument("-f", "--find", metavar="year/author/title", help="Search for a book by year, author, or title")
    parser.add_argument("-c", "--changestatus", nargs=2, metavar=("book_index", "new_status"), help= "Изменение статуса книги.  вводите id книги и новый статус ('в наличии' или 'выдана')")
    return parser

def load_library(json_filename:str) -> dict:
    try:
        with open(json_filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def update_library(json_filename, new_data) -> None:
    with open(json_filename, "w") as file:
        json.dump(new_data, file, indent=4)

def add_book(title:str, author: str, year: int)->None:
    file_data = load_library(library)
    
    new_book = {"id": 1,
                "title": title,
                "author": author,
                "year": year,
                "status": "в наличии"
                }
    if len(file_data["books"])>0:
        current_id = 1 + file_data["books"][-1]["id"]
        new_book["id"]= current_id
    file_data["books"].append(new_book)
    update_library(library, file_data)
    print("Book successfully added to library")

def display_books()->None:
    print('-'*35)
    print("|📖  LIST OF BOOKS IN LIBRARY   📖|")
    print('-'*35)
    file_data = load_library(library)
    books = file_data["books"]
    if len(books)==0:
        print("No books found in Library. Library is empty")
    else:
        for i in books:
            print(f"ID: {i['id']}, Title: {i['title']}, Author: {i['author']}, Year: {i['year']}, Status: {i['status']}")
        print('-'*35)

def remove_book(index: int)->None:
    file_data = load_library(library)
    books = file_data["books"]
    if len(books)>0:
        book_found = False
        for i in books:
            if i["id"]== index:
                book_found = True
                print(f"Book {i} removed successfully.")
                books.remove(i)
                update_library(library, file_data)
        if book_found == False:
            print("Book not found")
    else :
        print("No books in library. Can't delete book 🫤")

# код функции очень похож на функцию remove_task. изменение в наличие параметра newstatus и строке 84.
def change_status(index: int, newstatus: str)->'None':
    file_data = load_library(library)
    books = file_data["books"]
    if len(books)>0:
        book_found = False
        for i in books:
            if i["id"]== index:
                book_found = True
                print(f"Book status changed successfully.")
                i["status"]= newstatus
                update_library(library, file_data)
        if book_found == False:
            print("Book not found. Check if you typed the correct index.")
    else :
        print("No books in library. Can't complete this command 🫤")

def find_book(attribute: str)->'None':
    file_data = load_library(library)
    books = file_data["books"]
    if len(books)>0:
        book_found = False
        for i in books:
            if i["title"]== attribute or i["author"]==attribute or (str)(i["year"])==attribute:
                book_found = True
                print("Book found.")
                print("Book info: ")
                print(f"ID: {i['id']}, Title: {i['title']}, Author: {i['author']}, Year: {i['year']}, Status: {i['status']}")
                browse_book = input('Хотите узнать о чем книга? Да -> Y /Нет -> n \n')
                if browse_book=='Y':
                    query = ''+ i['title'] + i['author'] + 'книга'
                    webbrowser.open(query)
                            
        if book_found == False:
            print("Book not found. Check if you typed the correct index.")
    else :
        print("No books in library. Can't complete this command 🫤")

def main():

    parser = create_parser()
    args = parser.parse_args()
    #while not args.q:
    if args.add:
        add_book(args.add[0], args.add[1], int(args.add[2]))
    elif args.list:
        display_books()
    elif args.remove:
        remove_book(int(args.remove))
    elif args.changestatus:
        change_status(int(args.changestatus[0]), args.changestatus[1])
    elif args.find:
         find_book(args.find)
    else:
        parser.print_help()
    
if __name__ == "__main__":
    main()
    