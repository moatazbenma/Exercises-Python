# Shopping Cart Project

## Overview

This project is a simple **Shopping Cart** application that allows users to add, update, remove, and view items in their cart. Users can also export their cart data to a CSV file and track their discounts when items are added.

---

## Features

- **Add Item:** Add items to the shopping cart with price and optional discount.
- **Update Item:** Update the details (name, price, or discount) of an item in the cart.
- **Remove Item:** Remove items from the cart using the product's ID.
- **View Items:** View all items in the cart, including their price and discounted price.
- **Export to CSV:** Export the cart items to a CSV file for further use.
- **Discount System:** Apply a 20% discount to items that cost $50 or more.

---

## Requirements

- **Python 3.x** (For running the script)
- **CSV module** (Included with Python by default)
- **JSON module** (Included with Python by default)

---

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/shopping-cart.git
    ```

2. Navigate to the project directory:

    ```bash
    cd shopping-cart
    ```

3. The script doesn't require any external dependencies, as it uses Python's built-in libraries (CSV, JSON).

---

## How to Run

1. Navigate to the directory where the script is located.
2. Run the **main.py** script:

    ```bash
    python main.py
    ```

3. Follow the on-screen prompts to:
   - Add an item to the cart
   - Update an item
   - Remove an item
   - View items in the cart
   - Export the cart to a CSV file

---

## Usage

### Adding an Item

- You can add an item by providing the product's ID, name, and price.
- If the price is $50 or more, a 20% discount is applied automatically.

### Updating an Item

- You can update an item's name, price, and/or discount by specifying its ID.

### Removing an Item

- You can remove an item from the cart by providing its ID.

### Viewing Items

- Displays all the items currently in the cart, showing their ID, name, price, and discounted price (if any).

### Exporting to CSV

- The cart data is exported to a CSV file (`cart.csv`), which can be opened in any spreadsheet software.

---

## Example

Here's a sample interaction with the program:

