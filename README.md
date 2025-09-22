# Retail Inventory & Order Management System

## Project Overview
This is a **Python-based CLI application** designed to manage products, customers, orders, and payments for a retail business.  
It simulates real-world retail operations, providing functionalities such as **order creation, stock management, payment processing, and reporting**.

---

## Features

### Product Management
- Add new products with SKU, price, stock, and category.
- List all products with details.

### Customer Management
- Add customers with name, email, phone, and city.
- List all customers.

### Order Management
- Create orders with multiple items.
- View order details.
- Cancel orders.
- Automatic stock validation during order creation.

### Payment Management
- Process payments using different methods (e.g., card, cash).
- Refund payments.
- Payment status tracking.

### Reporting
- Top-selling products.
- Total revenue last month.
- Total orders per customer.
- Frequent customers (more than 2 orders).

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/mahithareddy01/Retail-Inventory-Order-Management-System-Core-Python.git
cd Retail-Inventory-Order-Management-System-Core-Python

2.**Install dependencies (if using a virtual environment):**

```bash
pip install -r requirements.txt


3.**Set up the PostgreSQL database and create the necessary tables.**

Usage

Run the CLI using Python:
```bash
python -m src.cli.main <module> <action> [options]
