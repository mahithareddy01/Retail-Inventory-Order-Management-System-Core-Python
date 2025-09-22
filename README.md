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


```bash
git clone https://github.com/mahithareddy01/Retail-Inventory-Order-Management-System-Core-Python.git

cd Retail-Inventory-Order-Management-System-Core-Python

# Install dependencies
pip install -r requirements.txt

# Set up PostgreSQL database (run SQL scripts in your SQL client)

# Add a product
python -m src.cli.main product add --name "Laptop" --sku "LP1001" --price 75000 --stock 10 --category "Electronics"

# List all products
python -m src.cli.main product list

# Add a customer
python -m src.cli.main customer add --name "John Doe" --email "john@example.com" --phone "1234567890" --city "Hyderabad"

# List all customers
python -m src.cli.main customer list

# Create an order
python -m src.cli.main order create --customer 1 --item 1:2 --item 3:1

# Show an order
python -m src.cli.main order show --order 1

# Cancel an order
python -m src.cli.main order cancel --order 1

# Process payment
python -m src.cli.main payment process --order 1 --method card

# Refund payment
python -m src.cli.main payment refund --order 1

# Generate reports
python -m src.cli.main report top-products
python -m src.cli.main report revenue
python -m src.cli.main report orders-per-customer
python -m src.cli.main report frequent-customers

