# Shopping Cart with MySQL

## Overview

This is a **Shopping Cart** application built using Python and **MySQL** for managing products in the cart. The application allows users to add, update, remove, and view items in the cart. It also includes the functionality to export the cart data to a CSV file. 

The items in the cart are stored in a **MySQL database** instead of JSON, making the data storage more scalable and persistent.

---

## Features

- **Add Item:** Add items to the shopping cart, including their price and discount (if applicable).
- **Update Item:** Modify the details (name, price, or discount) of items in the cart.
- **Remove Item:** Remove an item from the cart based on its unique ID.
- **View Items:** View all the items currently in the cart, along with their details.
- **Export to CSV:** Export the cart data into a CSV file for easy access or analysis.
- **Discount System:** Apply a 20% discount to products that cost $50 or more.

---

## Requirements

- **Python 3.x** (For running the script)
- **MySQL Database** (for storing the cart data)
- **MySQL Connector for Python** (for connecting Python with MySQL)

To install the MySQL connector:

```bash
pip install mysql-connector-python
