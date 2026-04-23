# import libs
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# fastAPI class
app = FastAPI()

# data model
class Book(BaseModel):
    book_id: int
    book_title: str
    book_author: str
    book_condition: Optional[str] = None
    book_edition: Optional[str] = None
    

# fake DB
books: List[Book] = [
    Book(
        book_id=1,
        book_title="English Dictionary",
        book_author="Oxford Group"
    ),
    Book(
        book_id=2,
        book_title="Diary of a Wimpy Kid",
        book_author="The Beatles",
        book_condition="on fire"
    ),
    Book(
        book_id=3,
        book_title="Space Wars",
        book_author="James Conway",
        book_edition="Super rare"
    )
]

# root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the online library"}

# getting all books - ENDPOINT
@app.get("/books", response_model=List[Book])
def get_books():
    return books

# get specific book by ID
@app.get("/books/{book_id}", respone_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.book_id == book_id:
            return book
    return {"error": "Book not found"}