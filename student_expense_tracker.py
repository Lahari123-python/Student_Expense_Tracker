#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("================================")
print("     STUDENT EXPENSE TRACKER")
print("================================")

print("1. Add Expense")
print("2. View Expenses")
print("3. Show Total Expenses")
print("4. Exit")


# In[2]:


expenses = []

def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    print("Expense added successfully!")


# In[3]:


add_expense()


# In[4]:


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found!")

    else:
        print("\n----- ALL EXPENSES -----")

        for i, expense in enumerate(expenses, start=1):
            print("\nExpense:", i)
            print("Amount: ₹", expense["amount"])
            print("Category:", expense["category"])
            print("Description:", expense["description"])


# In[5]:


view_expenses()


# In[8]:


def total_expenses():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expenses: ₹", total)


# In[9]:


total_expenses()


# In[10]:


def delete_expense():
    view_expenses()

    if len(expenses) == 0:
        return

    number = int(input("Enter expense number to delete: "))

    if 1 <= number <= len(expenses):
        expenses.pop(number - 1)
        print("Expense deleted successfully!")

    else:
        print("Invalid expense number!")


# In[11]:


delete_expense()


# In[12]:


import json
import os

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("Expenses saved successfully!")


# In[13]:


save_expenses()


# In[14]:


def load_expenses():
    global expenses

    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

        print("Previous expenses loaded successfully!")

    else:
        expenses = []
        print("No previous expenses found!")


# In[15]:


load_expenses()


# In[16]:


def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    save_expenses()

    print("Expense added successfully!")


# In[17]:


add_expense()


# In[18]:


def delete_expense():
    view_expenses()

    if len(expenses) == 0:
        return

    number = int(input("Enter expense number to delete: "))

    if 1 <= number <= len(expenses):
        expenses.pop(number - 1)

        save_expenses()

        print("Expense deleted successfully!")

    else:
        print("Invalid expense number!")


# In[19]:


delete_expense()


# In[20]:


def category_expenses():
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\n--- CATEGORY WISE EXPENSES ---")

    for category, total in category_totals.items():
        print(category, ": ₹", total)


# In[22]:


category_expenses()


# In[23]:


print(expenses)


# In[24]:


add_expense()


# In[25]:


category_expenses()


# In[26]:


def main():
    load_expenses()

    while True:
        print("\n===== STUDENT EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Delete Expense")
        print("5. Category Wise Expenses")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            category_expenses()

        elif choice == "6":
            save_expenses()
            print("Thank you for using Student Expense Tracker!")
            break

        else:
            print("Invalid choice! Try again.")


# In[27]:


main()


# In[28]:


def add_expense():
    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        category = input("Enter expense category: ")
        description = input("Enter description: ")

        if not category.strip():
            print("Category cannot be empty!")
            return

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)

        save_expenses()

        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount! Please enter numbers only.")


# In[29]:


main()


# In[30]:


from datetime import date

today = date.today()

print("Today's Date:", today)


# In[31]:


def add_expense():
    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        category = input("Enter expense category: ")
        description = input("Enter description: ")

        if not category.strip():
            print("Category cannot be empty!")
            return

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": str(date.today())
        }

        expenses.append(expense)

        save_expenses()

        print("Expense added successfully!")
        print("Date:", date.today())

    except ValueError:
        print("Invalid amount! Please enter numbers only.")


# In[32]:


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found!")
    else:
        print("\n----- ALL EXPENSES -----")

        for i, expense in enumerate(expenses, start=1):
            print("\nExpense:", i)
            print("Amount: ₹", expense["amount"])
            print("Category:", expense["category"])
            print("Description:", expense["description"])
            print("Date:", expense.get("date", "Date not available"))


# In[33]:


main()


# In[34]:


def monthly_expenses():
    month = input("Enter month (YYYY-MM): ")

    total = 0

    for expense in expenses:
        expense_date = expense.get("date", "")

        if expense_date.startswith(month):
            total += expense["amount"]

    print("Monthly Expenses: ₹", total)


# In[35]:


monthly_expenses()


# In[36]:


def check_budget():

    budget = float(input("Enter your monthly budget: "))

    month = input("Enter month (YYYY-MM): ")

    total = 0

    for expense in expenses:
        expense_date = expense.get("date", "")

        if expense_date.startswith(month):
            total += expense["amount"]

    print("Your Monthly Budget: ₹", budget)
    print("Your Total Expenses: ₹", total)

    remaining = budget - total

    if remaining > 0:
        print("Remaining Budget: ₹", remaining)

    elif remaining == 0:
        print("Your budget is fully used!")

    else:
        print("Warning! You exceeded your budget by ₹", abs(remaining))


# In[37]:


check_budget()


# In[49]:



def check_budget():

    try:
        budget = float(input("Enter your monthly budget: "))

        if budget <= 0:
            print("Please enter a budget greater than zero!")
            return

        month = input("Enter month (YYYY-MM): ")

        total = 0

        for expense in expenses:
            expense_date = expense.get("date", "")

            if expense_date.startswith(month):
                total += expense["amount"]

        remaining = budget - total
        percentage = (total / budget) * 100

        print("\n----- BUDGET REPORT -----")
        print("Budget: ₹", budget)
        print("Spent: ₹", total)
        print("Used:", round(percentage, 2), "%")

        if total > budget:
            print("Warning! Budget exceeded!")

        elif percentage >= 80:
            print("Warning! You have used 80% of your budget!")

        else:
            print("You are within your budget!")

        print("Remaining: ₹", remaining)

    except ValueError:
        print("Invalid input! Please enter a valid number.")


# In[53]:


check_budget()


# In[40]:


import matplotlib.pyplot as plt


# In[41]:


def expense_dashboard():

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    if not category_totals:
        print("No expenses available for dashboard!")
        return

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(8, 5))

    plt.bar(categories, amounts)

    plt.title("Student Expense Dashboard")
    plt.xlabel("Categories")
    plt.ylabel("Amount (Rs)")

    plt.show()


# In[42]:


expense_dashboard()


# In[43]:


def expense_pie_chart():

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        category_totals[category] = (
            category_totals.get(category, 0) + amount
        )

    if not category_totals:
        print("No expenses available!")
        return

    plt.figure(figsize=(7, 7))

    plt.pie(
        category_totals.values(),
        labels=category_totals.keys(),
        autopct="%1.1f%%"
    )

    plt.title("Expense Distribution")

    plt.show()


# In[44]:


expense_pie_chart()


# In[64]:


def main():

    load_expenses()

    while True:

        print("\n===== STUDENT EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Delete Expense")
        print("5. Category Wise Expenses")
        print("6. Monthly Report")
        print("7. Budget Check")
        print("8. Bar Dashboard")
        print("9. Pie Chart")
        print("10. search expenses")
        print("11.Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            category_expenses()

        elif choice == "6":
            monthly_expenses()

        elif choice == "7":
            check_budget()

        elif choice == "8":
            expense_dashboard()

        elif choice == "9":
            expense_pie_chart()

        elif choice == "10":
            search_expenses()
        elif choice == "11":
            print("Thank you for using Student Expense Tracker!")
            break

        else:
            print("Invalid choice! Try again.")


# In[65]:


main()


# In[47]:


main()


# In[48]:


check_budget()


# In[66]:



def search_expenses():

    search_category = input("Enter category to search: ").strip().lower()

    found = False

    print("\n----- SEARCH RESULTS -----")

    for expense in expenses:

        if expense["category"].lower() == search_category:

            print("Date:", expense.get("date", "Not available"))
            print("Category:", expense["category"])
            print("Amount: ₹", expense["amount"])
            print("Description:", expense["description"])
            print("----------------------")

            found = True

    if not found:
        print("No expenses found in this category!")


# In[67]:


search_expenses()


# In[68]:


main()


# In[69]:


main()


# In[ ]:




