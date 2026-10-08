# Byte & Brew Cafe Kiosk

total_bill = 0.00

print("Welcome to Byte & Brew!")

while True:
    print("\n--- Byte & Brew Menu ---")
    print("1. Black Coffee - $2.50")
    print("2. Vanilla Latte - $4.00")
    print("3. Blueberry Muffin - $3.00")
    print("4. Complete Order (Checkout)")

    try:
        choice = int(input("\nEnter your choice (1-4): "))
    except ValueError:
        print("Invalid selection. Please enter a number from 1 to 4.")
        continue

    if choice == 1:
        total_bill += 2.50
        print(f"Added Black Coffee. Current total: ${total_bill:.2f}")

    elif choice == 2:
        total_bill += 4.00
        print(f"Added Vanilla Latte. Current total: ${total_bill:.2f}")

    elif choice == 3:
        total_bill += 3.00
        print(f"Added Blueberry Muffin. Current total: ${total_bill:.2f}")

    elif choice == 4:
        print(f"\nYour final total is: ${total_bill:.2f}")
        print("Thank you for visiting Byte & Brew!")
        break

    else:
        print("Invalid selection. Please choose a valid menu item.")
