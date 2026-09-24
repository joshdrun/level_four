# this program takes expences, evaluates tehm and then provides relevant insights and recommendations based on the analysis.

#initialize variables
expenses = []

small_expense = 0
medium_expense = 0
large_expense = 0
keep_going = True


#get all of the expenses from the user
while keep_going == True:
    expense = float(input("Enter an expense (or 0 to stop): "))
    if expense != 0:
        expenses.append(expense)
    else:  
        keep_going = False


#evaluate the expenses and categorize them into small, medium, and large
for i in range(len(expenses)):
    if expenses[i] < 25:
        small_expense += 1
    elif expenses[i] <= 100:
        medium_expense += 1
    else:
        large_expense += 1



# print the expense summary
print("Expense Summary: \n ---------------------------")


#print calculations
print("Total number of expenses:", len(expenses))
print("Total amount of expenses:", sum(expenses))
print("Average expense:", sum(expenses) / len(expenses))
print("Smallest expense:", min(expenses))
print("Largest expense:", max(expenses))

#print categorization of expenses
print("Small expenses:", small_expense)
print("Medium expenses:", medium_expense)
print("Large expenses:", large_expense)
