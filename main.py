import csv
import os
from datetime import datetime

# ==========================================================
# File Name
# ==========================================================

EXPENSE_FILE = "expenses.csv"

# ==========================================================
# Create Expense File
# ==========================================================

def create_expense_file():
    """
    Creates the CSV file if it does not already exist.
    """

    if not os.path.exists(EXPENSE_FILE):

        with open(
            EXPENSE_FILE,
            mode="w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "ID",
                "Expense",
                "Category",
                "Amount",
                "Date"
            ])


# ==========================================================
# Load Expenses
# ==========================================================

def load_expenses():
    """
    Reads all expenses from the CSV file.
    Returns a list of dictionaries.
    """

    expenses = []

    create_expense_file()

    with open(
        EXPENSE_FILE,
        mode="r",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            expenses.append(row)

    return expenses


# ==========================================================
# Save Expenses
# ==========================================================

def save_expenses(expenses):
    """
    Saves all expenses back to the CSV file.
    """

    with open(
        EXPENSE_FILE,
        mode="w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Expense",
            "Category",
            "Amount",
            "Date"
        ])

        for expense in expenses:

            writer.writerow([
                expense["ID"],
                expense["Expense"],
                expense["Category"],
                expense["Amount"],
                expense["Date"]
            ])


# ==========================================================
# Display Welcome Screen
# ==========================================================

def welcome_screen():

    print("\n" + "=" * 55)
    print("                 EXPENSE TRACKER")
    print("=" * 55)

    print("\nWelcome! 👋")

    print("\nTrack your daily expenses efficiently.")

    print("\nAvailable Commands")
    print("-" * 55)

    print("1 / view      → View Expenses")
    print("2 / add       → Add Expense")
    print("3 / search    → Search Expense")
    print("4 / delete    → Delete Expense")
    print("5 / summary   → Monthly Summary")
    print("6 / total     → Total Spending")
    print("7 / exit      → Exit")

    print("\nTip: You can enter either the number or the command.")

    input("\nPress Enter to continue...")


# ==========================================================
# Display Main Menu
# ==========================================================

def display_menu():

    print("\n" + "=" * 55)
    print("                 EXPENSE TRACKER")
    print("=" * 55)

    print("What would you like to do?\n")

    print("1. View Expenses")
    print("2. Add Expense")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Monthly Summary")
    print("6. Total Spending")
    print("7. Exit")

    print("\n" + "-" * 55)

# ==========================================================
# Add Expense
# ==========================================================

def add_expense():

    expenses = load_expenses()

    print("\n" + "=" * 55)
    print("                    ADD EXPENSE")
    print("=" * 55)

    added_count = 0

    while True:

        print(f"\nExpense {added_count + 1}")

        expense_name = input("Expense Name : ").strip().title()

        if not expense_name:
            print("❌ Expense name cannot be empty.")
            continue

        category = input("Category     : ").strip().title()

        if not category:
            category = "General"

        while True:

            amount = input("Amount (₹)   : ").strip()

            try:
                amount = float(amount)

                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Please enter a valid amount.")

        expense = {

            "ID": str(len(expenses) + 1),
            "Expense": expense_name,
            "Category": category,
            "Amount": f"{amount:.2f}",
            "Date": datetime.now().strftime("%d-%m-%Y")

        }

        expenses.append(expense)
        added_count += 1

        print(f"\n✅ '{expense_name}' added successfully.")

        choice = input("\nAdd another expense? (y/n): ").strip().lower()

        if choice != "y":
            break

    save_expenses(expenses)

    print(f"\n🎉 {added_count} expense(s) added successfully.")

    input("\nPress Enter to continue...")


# ==========================================================
# View Expenses
# ==========================================================

def view_expenses():

    expenses = load_expenses()

    print("\n" + "=" * 75)
    print("                     VIEW EXPENSES")
    print("=" * 75)

    if not expenses:

        print("\nNo expenses found.")

        input("\nPress Enter to continue...")

        return

    print(
        f"{'ID':<5}"
        f"{'Expense':<20}"
        f"{'Category':<20}"
        f"{'Amount':<12}"
        f"{'Date'}"
    )

    print("-" * 75)

    total = 0

    for expense in expenses:

        print(
            f"{expense['ID']:<5}"
            f"{expense['Expense']:<20}"
            f"{expense['Category']:<20}"
            f"₹{float(expense['Amount']):<11.2f}"
            f"{expense['Date']}"
        )

        total += float(expense["Amount"])

    print("-" * 75)

    print(f"Total Expenses : {len(expenses)}")
    print(f"Total Spending : ₹{total:.2f}")

    print("-" * 75)

    input("\nPress Enter to continue...")
# ==========================================================
# Search Expense
# ==========================================================

def search_expense():

    expenses = load_expenses()

    print("\n" + "=" * 55)
    print("                  SEARCH EXPENSE")
    print("=" * 55)

    if not expenses:

        print("\nNo expenses found.")

        input("\nPress Enter to continue...")

        return

    keyword = input(
        "\nEnter expense name or category: "
    ).strip().lower()

    print()

    found = False

    print(
        f"{'ID':<5}"
        f"{'Expense':<20}"
        f"{'Category':<20}"
        f"{'Amount':<12}"
        f"{'Date'}"
    )

    print("-" * 75)

    for expense in expenses:

        if (
            keyword in expense["Expense"].lower()
            or
            keyword in expense["Category"].lower()
        ):

            print(
                f"{expense['ID']:<5}"
                f"{expense['Expense']:<20}"
                f"{expense['Category']:<20}"
                f"₹{float(expense['Amount']):<11.2f}"
                f"{expense['Date']}"
            )

            found = True

    print("-" * 75)

    if not found:

        print("No matching expense found.")

    input("\nPress Enter to continue...")
# ==========================================================
# Delete Expense
# ==========================================================

def delete_expense():

    expenses = load_expenses()

    print("\n" + "=" * 55)
    print("                  DELETE EXPENSE")
    print("=" * 55)

    if not expenses:

        print("\nNo expenses found.")

        input("\nPress Enter to continue...")

        return

    print(
        f"{'ID':<5}"
        f"{'Expense':<20}"
        f"{'Category':<20}"
        f"{'Amount':<12}"
        f"{'Date'}"
    )

    print("-" * 75)

    for expense in expenses:

        print(
            f"{expense['ID']:<5}"
            f"{expense['Expense']:<20}"
            f"{expense['Category']:<20}"
            f"₹{float(expense['Amount']):<11.2f}"
            f"{expense['Date']}"
        )

    print("-" * 75)

    try:

        expense_id = input(
            "\nEnter Expense ID to delete: "
        ).strip()

        found = False

        for expense in expenses:

            if expense["ID"] == expense_id:

                confirm = input(
                    f"\nDelete '{expense['Expense']}'? (y/n): "
                ).strip().lower()

                if confirm == "y":

                    expenses.remove(expense)

                    for index, item in enumerate(expenses, start=1):
                        item["ID"] = str(index)

                    save_expenses(expenses)

                    print("\n🗑 Expense deleted successfully.")

                else:

                    print("\nDeletion cancelled.")

                found = True
                break

        if not found:

            print("\nExpense ID not found.")

    except Exception:

        print("\nSomething went wrong.")

    input("\nPress Enter to continue...")


# ==========================================================
# Monthly Summary
# ==========================================================

def monthly_summary():

    expenses = load_expenses()

    print("\n" + "=" * 60)
    print("                  MONTHLY SUMMARY")
    print("=" * 60)

    if not expenses:

        print("\nNo expenses found.")

        input("\nPress Enter to continue...")

        return

    month = input(
    "\nEnter month (1-12): "
).strip().zfill(2)

    year = input(
        "Enter year (YYYY): "
    ).strip()

    total = 0
    count = 0

    print()

    print(
        f"{'ID':<5}"
        f"{'Expense':<20}"
        f"{'Category':<20}"
        f"{'Amount':<12}"
        f"{'Date'}"
    )

    print("-" * 75)

    for expense in expenses:

        expense_date = datetime.strptime(
            expense["Date"],
            "%d-%m-%Y"
        )

        if (
            expense_date.strftime("%m") == month
            and
            expense_date.strftime("%Y") == year
        ):

            print(
                f"{expense['ID']:<5}"
                f"{expense['Expense']:<20}"
                f"{expense['Category']:<20}"
                f"₹{float(expense['Amount']):<11.2f}"
                f"{expense['Date']}"
            )

            total += float(expense["Amount"])
            count += 1

    print("-" * 75)

    print(f"Total Expenses : {count}")
    print(f"Total Spending : ₹{total:.2f}")

    input("\nPress Enter to continue...")
# ==========================================================
# Total Spending Dashboard
# ==========================================================

def total_spending():

    expenses = load_expenses()

    print("\n" + "=" * 60)
    print("                TOTAL SPENDING")
    print("=" * 60)

    if not expenses:

        print("\nNo expenses found.")

        input("\nPress Enter to continue...")

        return

    total = 0

    highest = expenses[0]
    lowest = expenses[0]

    for expense in expenses:

        amount = float(expense["Amount"])

        total += amount

        if amount > float(highest["Amount"]):
            highest = expense

        if amount < float(lowest["Amount"]):
            lowest = expense

    average = total / len(expenses)

    print(f"\nTotal Expenses : {len(expenses)}")
    print(f"Total Spending : ₹{total:.2f}")
    print(f"Average Expense: ₹{average:.2f}")

    print("\nHighest Expense")
    print("-" * 40)
    print(f"Expense : {highest['Expense']}")
    print(f"Category: {highest['Category']}")
    print(f"Amount  : ₹{float(highest['Amount']):.2f}")

    print("\nLowest Expense")
    print("-" * 40)
    print(f"Expense : {lowest['Expense']}")
    print(f"Category: {lowest['Category']}")
    print(f"Amount  : ₹{float(lowest['Amount']):.2f}")

    input("\nPress Enter to continue...")


# ==========================================================
# Main Function
# ==========================================================

def main():

    create_expense_file()

    welcome_screen()

    while True:

        display_menu()

        choice = input(
            "\nEnter your choice (number or command): "
        ).strip().lower()

        # ===========================
        # View Expenses
        # ===========================

        if choice in ["1", "view"]:

            view_expenses()

        # ===========================
        # Add Expense
        # ===========================

        elif choice in ["2", "add"]:

            add_expense()

        # ===========================
        # Search Expense
        # ===========================

        elif choice in ["3", "search"]:

            search_expense()

        # ===========================
        # Delete Expense
        # ===========================

        elif choice in ["4", "delete"]:

            delete_expense()

        # ===========================
        # Monthly Summary
        # ===========================

        elif choice in ["5", "summary"]:

            monthly_summary()

        # ===========================
        # Total Spending
        # ===========================

        elif choice in ["6", "total"]:

            total_spending()

        # ===========================
        # Exit Program
        # ===========================

        elif choice in ["7", "exit"]:

            expenses = load_expenses()

            total = 0

            for expense in expenses:

                total += float(expense["Amount"])

            print("\n" + "=" * 55)
            print("                     GOODBYE")
            print("=" * 55)

            print("\nThank you for using Expense Tracker!")

            print(f"\nTotal Expenses : {len(expenses)}")
            print(f"Total Spending : ₹{total:.2f}")

            print("\nHave a productive day! 👋")

            break

        # ===========================
        # Invalid Choice
        # ===========================

        else:

            print("\n❌ Invalid choice!")
            print("Please choose a valid option (1-7).")

            input("\nPress Enter to continue...")


# ==========================================================
# Run Program
# ==========================================================

if __name__ == "__main__":
    main()
