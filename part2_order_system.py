# Order Management System using Data Structures

def display_menu(menu):
    print("\n🍽️ MENU")
    for item, price in menu.items():
        print(f"{item} : ₹{price}")


def take_order(menu):
    order = []
    
    while True:
        item = input("\nEnter item to order (or type 'done' to finish): ").lower()
        
        if item == "done":
            break
        
        if item in menu:
            quantity = int(input(f"Enter quantity for {item}: "))
            order.append((item, quantity))
        else:
            print("❌ Item not available in menu.")
    
    return order


def calculate_bill(order, menu):
    total = 0
    print("\n🧾 BILL DETAILS")
    
    for item, quantity in order:
        price = menu[item]
        item_total = price * quantity
        total += item_total
        print(f"{item} x {quantity} = ₹{item_total}")
    
    print(f"\n💰 Total Bill: ₹{total}")
    return total


def main():
    # Dictionary (Menu)
    menu = {
        "pizza": 200,
        "burger": 100,
        "pasta": 150,
        "sandwich": 80,
        "coffee": 50
    }

    print("🛒 Welcome to Order System")

    display_menu(menu)
    order = take_order(menu)

    if order:
        calculate_bill(order, menu)
    else:
        print("No items ordered.")


if __name__ == "__main__":
    main()