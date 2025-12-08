# Libraries / Data Storage
expense_record = []
category_total = {}
unique_categories = set()

print("\nWelcome to expense tracker!")

# Ask how many expenses to enter
while True:
    try:
        num_expenses_input = input("How many expenses do you want to enter? (Enter 0 or 'q' to quit): ")

        if num_expenses_input.lower() == 'q':
            print("Exiting expense entry.")
            exit()

        num_expenses = int(num_expenses_input)

        if num_expenses < 0:
            print("Please enter a non-negative number.")
            continue

        break
    except ValueError:
        print("Invalid input. Please enter a number or 'q'.")

# Collect expenses
if num_expenses > 0:
    for i in range(num_expenses):

        category = input("Enter category: ")
        amount = float(input("Enter your amount: "))
        date = input("Enter date (DD/MM/YYYY): ")

        expense = (category, amount, date)
        expense_record.append(expense)

        # update category totals
        category_total[category] = category_total.get(category, 0) + amount
        unique_categories.add(category)


# If no expenses entered
if len(expense_record) == 0:
    print("\nNo expenses entered. Operation ended.")
    exit()

# --- Calculations ---
amounts = [amount for category, amount, date in expense_record]

total_spending = sum(amounts)
highest_spending = max(amounts)
lowest_spending = min(amounts)
average = total_spending / len(amounts)

# Dictionary
overall_stats = {
    "Total Spending": total_spending,
    "Highest Expense": highest_spending,
    "Lowest Expense": lowest_spending,
    "Average Expense": average
}

# --- Output ---
print("\n===== Overall Spending Summary =====")
print(f"Total Spending: ${overall_stats['Total Spending']:.2f}")
print(f"Average Expense: ${overall_stats['Average Expense']:.2f}")
print(f"Highest Expense: ${overall_stats['Highest Expense']:.2f}")
print(f"Lowest Expense: ${overall_stats['Lowest Expense']:.2f}")

print("\n===== Unique Categories Spent On =====")
for category in unique_categories:
    print(f"- {category}")

print("\n===== Spending by Category =====")
for category, total in category_total.items():
    print(f"{category}: ${total:.2f}")
