# Use code to see stored csv file.


import os

current_directory = os.getcwd()
csv_file_path = os.path.join(current_directory, 'expenses.csv')

print("CSV file is stored at:", csv_file_path)


# Functions:
def piechart(exp, lab):  # Used later in the options given to user
    import sys
    import matplotlib
    matplotlib.use('TkAgg')
   
    import matplotlib.pyplot as plt
    import numpy as np

    # Filter out categories with zero expenses
    non_zero_exp = [exp[i] for i in range(len(exp)) if exp[i] > 0]
    non_zero_lab = [lab[i] for i in range(len(exp)) if exp[i] > 0]

    p = np.array(non_zero_exp)
    plt.pie(p, labels=non_zero_lab)
    plt.show()

def method_of_payment(x, y):  # Used later in the options given to user
    import sys
    import matplotlib
    matplotlib.use('TkAgg')

    import matplotlib.pyplot as plt
    import numpy as np

    plt.bar(x, y)
    plt.show()

# To save the data in a CSV file
import csv

def save_to_csv(filename, expenses, labels, methods):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["Category", "Amount", "Method of Payment"])
        for label, expense, method in zip(labels, expenses, methods):
            writer.writerow([label, expense, method])

def load_from_csv(filename):
    expenses, labels, methods = [], [], []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            labels.append(row[0])
            expenses.append(float(row[1]))
            methods.append(row[2])
    return expenses, labels, methods

def load_categories_from_csv(filename):
    categories = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            categories.append(row[0])
    return categories

print("Welcome to your Personal Expense Tracker. \nLet's track Expenses!!\n")

expenses, label, methods = [],[],[] #Defining lists used in the code.

spendings = 0
budget = float(input("Enter your budget: "))
n = int(input("How many categories do you want to divide your expenses into: "))

try:
    expenses, label, methods = load_from_csv('expenses.csv')
    spendings = sum(expenses)
except FileNotFoundError:
    pass

existing_categories = load_categories_from_csv('expenses.csv')
print("Do you want to any of the pre-defined categories?")  # Asks user if they want to use a pre=defined category
for i, category in enumerate(existing_categories, start=1):
    print(f"{i}. {category}")
print(f"{len(existing_categories) + 1}. No, create a new category")

for i in range(n):
    reuse_choice = int(input("\nEnter your choice: ")) # Choice Menu

    if 1 <= reuse_choice <= len(existing_categories):
        chosen_category = existing_categories[reuse_choice - 1]
        print(f"\nYou chose : {chosen_category}")

        if chosen_category in label:
            index = label.index(chosen_category)
            exp = float(input("Amount expensed: "))
            expenses[index] += exp
            spendings += exp
            meth = input("Method of Payment: ")
            methods[index] = meth
        else:
            exp = float(input("Amount expensed: "))
            expenses.append(exp)
            label.append(chosen_category)
            spendings += exp
            meth = input("Method of Payment: ")
            methods.append(meth)
        save_to_csv('expenses.csv', expenses, label, methods)
    else:
        name = input("\nEnter the category name: ")
        caps = name.capitalize()
        label.append(caps)
        exp = float(input("Amount expensed: "))
        expenses.append(exp)
        spendings += exp
        meth = input("Method of Payment: ")
        methods.append(meth)
        save_to_csv('expenses.csv', expenses, label, methods)

print("\nSelect an option:") #Choice Menu
print("1. Analyze budget.")
print("2. See a detailed analysis of your expenses")
print("3. See a detailed analysis with respect to payment methods ")
print("4. Exit.")

while True:                          # Will repeat till user chooses to leave.
    choice = int(input("\nEnter your choice.. "))
    if choice == 1:
        saved = budget - spendings
        label.append("Savings")
        expenses.append(saved)
        listlen = len(label)
        for j in range(listlen):
            print(label[j], ":", expenses[j])

        if spendings > budget:
            print("You have spent", spendings - budget, "more than your budget. Please try to reduce your spendings.")
        elif spendings < budget:
            print("Congratulations!! You saved ", saved, ".\nKeep it up.")
        elif spendings == budget:
            print("You have exhausted your budget. Please try to save some amount.")
    elif choice == 2:                                   # Plots a pie-chart of expenses and labels the categories
        try:
            piechart(expenses, label)
        except ValueError:
            print("\nAs your spendings are more than your budget, You were analyzed based on your expenses and not your budget.")
            label.remove("Savings")
            expenses.pop(-1)
            piechart(expenses, label)
    elif choice == 3:                                   # Plots a barplot of methods vs expenses
        method_of_payment(methods, expenses)

    elif choice == 4:                                   # Exits menu and prints Thank you.
        break

print("Thank you for using this expense tracker.")