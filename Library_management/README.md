# 📚 Library Management System (Python)

A simple Python-based library system that allows you to add, remove, borrow, and return books using a JSON file as storage.

## Features
- Add new books
- Remove existing books
- Borrow and return functionality
- Check availability
- View all books

## Usage

```python
from library import Library

lib = Library()
lib.add_book("1984", "George Orwell")
lib.view_book()
