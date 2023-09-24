# Importing necessary libraries
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Declaring a Class
class ExpenseTracker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Expense Tracker")
        self.geometry("525x1000")    
        self.configure(bg='lavender')
        self.expenses = {}
        self.total_expense = 0
        self.create_widgets()

    def create_widgets(self):
        self.category_label = ttk.Label(self, text="Category:")
        self.category_label.grid(row=0, column=0, padx=10, pady=10)

        self.categories = ['Rent','Groceries','Transportation','Bills','Essentials','Entertainment','Savings','Miscellaneous']
        self.category_var = tk.StringVar()
        self.category_var.set(self.categories[0])
        self.category_dropdown = ttk.Combobox(self, textvariable=self.category_var, values=self.categories, state='readonly')
        self.category_dropdown.grid(row=0, column=1, padx=10, pady=10)

        self.expense_label = ttk.Label(self, text="Expense:")
        self.expense_label.grid(row=1, column=0, padx=10, pady=10)

        self.expense_entry = ttk.Entry(self, width=30)
        self.expense_entry.grid(row=1, column=1, padx=10, pady=10)

        self.add_button = ttk.Button(self, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.total_expense_label = ttk.Label(self, text="Total Expense: 0")
        self.total_expense_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.figure = Figure(figsize=(5, 5))
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.quit_button = ttk.Button(self, text="Quit", command=self.quit)
        self.quit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def add_expense(self):
        category = self.category_var.get()
        expense = float(self.expense_entry.get())
        self.expenses[category] = self.expenses.get(category, 0) + expense
        self.total_expense += expense

        # Update the total expense label
        self.total_expense_label.config(text=f"Total Expense: {self.total_expense}")

        # Update the pie chart
        self.ax.clear()
        self.ax.pie(self.expenses.values(), labels=self.expenses.keys(), autopct='%1.1f%%')
        self.canvas.draw()

        # Clear the entry field
        self.expense_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = ExpenseTracker()
    app.mainloop()