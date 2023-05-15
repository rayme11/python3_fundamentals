
expenses = []

num_expenses = int(input("How many expenses your have\n"))

for i in range(num_expenses):
    expenses.append(float(input("Enter an expense\n")))

total = sum(expenses)  # cool function from python
print('You spent ', total)

for expense in expenses:
    print(expense)
