# =========================================
# PART 2: RESTAURANT ORDER SYSTEM
# =========================================

import copy

# ======================
# GIVEN DATA (DON'T EDIT)
# ======================

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price": 40.0,  "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price": 90.0,  "available": True},
    "Rasgulla":       {"category": "Desserts",  "price": 80.0,  "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock": 8,  "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock": 6,  "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock": 5,  "reorder_level": 2},
    "Rasgulla":       {"stock": 4,  "reorder_level": 3},
    "Ice Cream":      {"stock": 7,  "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1, "items": ["Paneer Tikka", "Garlic Naan"], "total": 220.0},
        {"order_id": 2, "items": ["Gulab Jamun", "Veg Soup"], "total": 210.0},
        {"order_id": 3, "items": ["Butter Chicken", "Garlic Naan"], "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4, "items": ["Dal Tadka", "Garlic Naan"], "total": 220.0},
        {"order_id": 5, "items": ["Veg Biryani", "Gulab Jamun"], "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
        {"order_id": 7, "items": ["Butter Chicken", "Veg Biryani"], "total": 570.0},
        {"order_id": 8, "items": ["Garlic Naan", "Gulab Jamun"], "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9, "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"], "total": 270.0},
    ],
}

# =========================================
# TASK 1: MENU EXPLORATION
# =========================================

print("\n===== TASK 1: MENU =====")

categories = ["Starters", "Mains", "Desserts"]

for cat in categories:
    print(f"\n===== {cat} =====")
    for item, details in menu.items():
        if details["category"] == cat:
            status = "Available" if details["available"] else "Unavailable"
            print(f"{item:<15} ₹{details['price']:.2f}   [{status}]")

# Analysis
total_items = len(menu)
available_items = sum(1 for i in menu.values() if i["available"])

most_expensive = max(menu.items(), key=lambda x: x[1]["price"])

cheap_items = [(name, d["price"]) for name, d in menu.items() if d["price"] < 150]

print(f"\nTotal Items: {total_items}")
print(f"Available Items: {available_items}")
print(f"Most Expensive: {most_expensive[0]} ₹{most_expensive[1]['price']}")

print("\nItems under ₹150:")
for item, price in cheap_items:
    print(f"{item} ₹{price}")

# =========================================
# TASK 2: CART OPERATIONS
# =========================================

print("\n===== TASK 2: CART =====")

cart = []

def add_item(name, qty):
    if name not in menu:
        print(f"{name} not in menu")
        return
    if not menu[name]["available"]:
        print(f"{name} is unavailable")
        return
    
    for item in cart:
        if item["item"] == name:
            item["quantity"] += qty
            return
    
    cart.append({
        "item": name,
        "quantity": qty,
        "price": menu[name]["price"]
    })

def remove_item(name):
    for item in cart:
        if item["item"] == name:
            cart.remove(item)
            return
    print(f"{name} not in cart")

# Simulation
add_item("Paneer Tikka", 2)
add_item("Gulab Jamun", 1)
add_item("Paneer Tikka", 1)
add_item("Mystery Burger", 1)
add_item("Chicken Wings", 1)
remove_item("Gulab Jamun")

# Order Summary
print("\n========== Order Summary ==========")
subtotal = 0

for item in cart:
    total = item["quantity"] * item["price"]
    subtotal += total
    print(f"{item['item']:<15} x{item['quantity']}   ₹{total:.2f}")

gst = subtotal * 0.05
total_pay = subtotal + gst

print("------------------------------------")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"GST (5%): ₹{gst:.2f}")
print(f"Total Payable: ₹{total_pay:.2f}")
print("====================================")

# =========================================
# TASK 3: INVENTORY + DEEP COPY
# =========================================

print("\n===== TASK 3: INVENTORY =====")

inventory_backup = copy.deepcopy(inventory)

# Modify original
inventory["Paneer Tikka"]["stock"] = 0

print("\nOriginal:", inventory["Paneer Tikka"])
print("Backup:", inventory_backup["Paneer Tikka"])

# Restore
inventory["Paneer Tikka"]["stock"] = 10

# Deduct stock
for item in cart:
    name = item["item"]
    qty = item["quantity"]
    
    if inventory[name]["stock"] >= qty:
        inventory[name]["stock"] -= qty
    else:
        print(f"Low stock for {name}")
        inventory[name]["stock"] = 0

# Reorder alerts
for name, data in inventory.items():
    if data["stock"] <= data["reorder_level"]:
        print(f"⚠ Reorder Alert: {name} — Only {data['stock']} left")

# =========================================
# TASK 4: SALES ANALYSIS
# =========================================

print("\n===== TASK 4: SALES =====")

# Revenue per day
daily_revenue = {}

for date, orders in sales_log.items():
    total = sum(o["total"] for o in orders)
    daily_revenue[date] = total
    print(f"{date}: ₹{total}")

# Best day
best_day = max(daily_revenue, key=daily_revenue.get)
print(f"\nBest Day: {best_day} ₹{daily_revenue[best_day]}")

# Most ordered item
item_count = {}

for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            item_count[item] = item_count.get(item, 0) + 1

most_ordered = max(item_count, key=item_count.get)
print(f"Most Ordered Item: {most_ordered}")

# Add new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\nUpdated Revenue:")
for date, orders in sales_log.items():
    total = sum(o["total"] for o in orders)
    print(f"{date}: ₹{total}")

# Enumerate orders
print("\nAll Orders:")
count = 1
for date, orders in sales_log.items():
    for order in orders:
        items = ", ".join(order["items"])
        print(f"{count}. [{date}] Order #{order['order_id']} — ₹{order['total']} — Items: {items}")
        count += 1


input("\nPress Enter to exit...")
