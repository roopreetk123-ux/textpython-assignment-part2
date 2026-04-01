# Restaurant Menu & Order Management System (Part 2)

## 📌 Overview
This project is a Python-based Restaurant Order Management System.  
It uses core data structures like lists and dictionaries to manage menu items, customer orders, inventory, and sales data.

---

## 🚀 Features

### 1. Menu Exploration
- Displays menu items grouped by category (Starters, Mains, Desserts)
- Shows availability status of each item
- Finds:
  - Total number of items
  - Available items
  - Most expensive item
  - Items under ₹150

### 2. Cart Operations
- Add items to cart with quantity
- Prevent adding unavailable or non-existing items
- Update quantity if item already exists
- Remove items from cart
- Generates Order Summary with:
  - Subtotal
  - GST (5%)
  - Total payable amount

### 3. Inventory Management
- Uses deep copy to create a backup of inventory
- Demonstrates that original data remains unchanged
- Updates stock after order placement
- Shows reorder alerts when stock is low

### 4. Sales Log Analysis
- Calculates total revenue per day
- Identifies best-selling day
- Finds most ordered item
- Adds new sales data dynamically
- Displays all orders using enumeration

---

## 🛠️ Concepts Used

- Lists and Dictionaries
- Nested Data Structures
- Loops (for loops)
- Conditional Statements (if-else)
- Functions
- Deep Copy (`copy.deepcopy()`)
- String formatting

---

## ▶️ How to Run

1. Open terminal or command prompt  
2. Navigate to project folder  
3. Run the file:

```bash
python part2_order_system.py
