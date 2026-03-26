import datetime
transactions = []
budgets = {}
def add_transaction():
 category = input("Enter category: ")
 amount = float(input("Enter amount (+ for income, - for expense): "))
 description = input("Enter description: ")
 date = input("Enter date (YYYY-MM-DD): ")
 payment_method = input("Enter payment method: ")
 transaction = {
 "category": category,
 "amount": amount,
 "description": description,
 "date": datetime.datetime.strptime(date, "%Y-%m-%d"),
 "payment_method": payment_method
 }
 transactions.append(transaction)
 print("Transaction added successfully!\n")
def delete_transaction():
 view_all_transactions()
 index = int(input("Enter index of transaction to delete: "))
 if 0 <= index < len(transactions):
 del transactions[index]
 print("Transaction deleted.\n")
 else:
 print("Invalid index.\n")
def edit_transaction():
 view_all_transactions()
 index = int(input("Enter index of transaction to edit: "))
 if 0 <= index < len(transactions):
 category = input("Enter new category (leave blank to keep current): ")
 amount_input = input("Enter new amount (leave blank to keep current): ")
 description = input("Enter new description (leave blank to keep current): ")
 date = input("Enter new date (YYYY-MM-DD) (leave blank to keep current): ")
 payment_method = input("Enter new payment method (leave blank to keep current): ")
 if category:
 transactions[index]['category'] = category
 if amount_input:
 transactions[index]['amount'] = float(amount_input)
 if description:
 transactions[index]['description'] = description
 if date:
 transactions[index]['date'] = datetime.datetime.strptime(date, "%Y-%m-%d")
 if payment_method:
 transactions[index]['payment_method'] = payment_method
 print("Transaction updated.\n")
 else:
 print("Invalid index.\n")
def set_budget():
 category = input("Enter category to set budget for: ")
 limit = float(input("Enter budget limit: "))
 budgets[category] = limit
 print("Budget set.\n")
def report_budget():
 spent = {}
 for category in budgets:
 spent[category] = 0
 for t in transactions:
 if t['category'] in budgets:
 spent[t['category']] += t['amount']
 for category in budgets:
 print(f"{category}: Spent ₹{spent[category]}, Budget ₹{budgets[category]}")
 print()
def generate_insights():
 total_income = 0
 total_expense = 0
 for t in transactions:
 if t['amount'] > 0:
 total_income += t['amount']
 elif t['amount'] < 0:
 total_expense -= t['amount']
 print(f"Total Income: ₹{total_income}")
 print(f"Total Expenses: ₹{total_expense}")
 print(f"Net Savings: ₹{total_income - total_expense}\n")
def generate_monthly_report():
 month = int(input("Enter month (1-12): "))
 year = int(input("Enter year (e.g., 2025): "))
 monthly_income = 0
 monthly_expense = 0
 for t in transactions:
 if t['date'].month == month and t['date'].year == year:
 if t['amount'] > 0:
 monthly_income += t['amount']
 elif t['amount'] < 0:
 monthly_expense -= t['amount']
 print(f"Report for {month}/{year} => Income: ₹{monthly_income}, Expenses: ₹{monthly_expense}, Net:
₹{monthly_income - monthly_expense}\n")
def forecast_next_3_months():
 today = datetime.datetime.today()
 income = []
 expense = []
 for t in transactions:
 if t['amount'] > 0:
 income.append(t['amount'])
 elif t['amount'] < 0:
 expense.append(-t['amount'])
 avg_income = sum(income) / len(income) if income else 0
 avg_expense = sum(expense) / len(expense) if expense else 0
 for i in range(1, 4):
 forecast_date = today + datetime.timedelta(days=30 * i)
 print(f"Forecast {forecast_date.strftime('%B %Y')} => Expected Income: ₹{avg_income:.2f}, Expenses:
₹{avg_expense:.2f}, Net: ₹{avg_income - avg_expense:.2f}")
 print()
def search_transactions():
 print("\nSearch Options:")
 print("1. By Category")
 print("2. By Description Keyword")
 print("3. By Date Range")
 choice = input("Enter your choice: ")
 if choice == "1":
 cat = input("Enter category to search: ").lower()
 for i in range(len(transactions)):
 t = transactions[i]
 if cat in t['category'].lower():
 print_transaction(i, t)
 elif choice == "2":
 keyword = input("Enter keyword to search in description: ").lower()
 for i in range(len(transactions)):
 t = transactions[i]
 if keyword in t['description'].lower():
 print_transaction(i, t)
 elif choice == "3":
 start = input("Enter start date (YYYY-MM-DD): ")
 end = input("Enter end date (YYYY-MM-DD): ")
 start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
 end_date = datetime.datetime.strptime(end, "%Y-%m-%d")
 for i in range(len(transactions)):
 t = transactions[i]
 if start_date <= t['date'] <= end_date:
 print_transaction(i, t)
 print()
def view_all_transactions():
 print("\nAll Transactions:")
 for i in range(len(transactions)):
 print_transaction(i, transactions[i])
 print()
def print_transaction(i, t):
 print(f"{i}: ₹{t['amount']}, {t['category']}, {t['description']}, {t['date'].strftime('%Y-%m-%d')},
{t['payment_method']}")
# Menu Loop
def main():
 while True:
 print("------ Personal Finance Manager ------")
 print("1. Add Transaction")
 print("2. Edit Transaction")
 print("3. Delete Transaction")
 print("4. View All Transactions")
 print("5. Set Budget")
 print("6. Budget Report")
 print("7. Monthly Report")
 print("8. Financial Insights")
 print("9. Forecast Next 3 Months")
 print("10. Search Transactions")
 print("11. Exit")
 choice = input("Enter your choice (1-11): ")
 if choice == "1":
 add_transaction()
 elif choice == "2":
 edit_transaction()
 elif choice == "3":
 delete_transaction()
 elif choice == "4":
 view_all_transactions()
 elif choice == "5":
 set_budget()
 elif choice == "6":
 report_budget()
 elif choice == "7":
 generate_monthly_report()
 elif choice == "8":
 generate_insights()
 elif choice == "9":
 forecast_next_3_months()
 elif choice == "10":
 search_transactions()
 elif choice == "11":
 print("Exiting program. Goodbye!")
 break
 else:
 print("Invalid choice. Please try again.\n")
# Run the program
main()
