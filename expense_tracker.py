import json
import os

FILE_NAME = "expenses_record.json"

def get_records():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_records(records):
    with open(FILE_NAME, "w") as f:
        json.dump(records, f, indent=4)

def insert_expense(records):
    print("\n--- ENTER NEW EXPENSE ---")
    title = input("Enter item name: ").strip()
    try:
        cost = float(input("Enter amount spent: "))
        group = input("Enter category (e.g. Food, Travel): ").strip()
        
        new_entry = {"title": title, "cost": cost, "group": group}
        records.append(new_entry)
        save_records(records)
        print("Record added successfully.")
    except ValueError:
        print("Invalid input. Amount must be a number.")

def display_all(records):
    print("\n--- ALL EXPENSES ---")
    if not records:
        print("No expenses recorded yet.")
        return
    
    grand_total = 0
    print(f"{'Item Name':<20} | {'Amount':<10} | {'Category':<15}")
    print("=" * 50)
    for row in records:
        print(f"{row['title']:<20} | {row['cost']:<10} | {row['group']:<15}")
        grand_total += row['cost']
    print("=" * 50)
    print(f"Total Expenditure: {grand_total}")

def main():
    records = get_records()
    while True:
        print("\n*** EXPENSE TRACKER SYSTEM ***")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Exit Application")
        
        selection = input("Select an option (1/2/3): ").strip()
        
        if selection == "1":
            insert_expense(records)
        elif selection == "2":
            display_all(records)
        elif selection == "3":
            print("Exiting application. Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()