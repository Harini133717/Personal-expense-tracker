
import json
import os

FILE = "expenses.json"

if os.path.exists(FILE):
    with open(FILE, "r") as f:
        expenses = json.load(f)
else:
    expenses = []

while True:
    print("\nPERSONAL EXPENSE TRACKER")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be positive.")
            continue

        expenses.append({
            "category": category,
            "amount": amount
        })

        with open(FILE, "w") as f:
            json.dump(expenses, f, indent=4)

        print("Expense saved successfully!")

    elif choice == "2":
        for item in expenses:
            print(item["category"], "-", item["amount"])

    elif choice == "3":
        total = sum(item["amount"] for item in expenses)
        print("Total expenses:", total)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
