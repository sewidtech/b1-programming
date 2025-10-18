#CalculatorProgram
print("Welcome to the Business calculator")


choice = int(input("Please choose an option:\n1. Revenue\n2. Cost\n3. Profit\n"))


#revenue and costs
Revenue = float(input("Please enter your Revenue:"))
Cost = float(input("Please enter your Cost:"))


Profit = Revenue - Cost



#OPERATIONS
sum = (Revenue + Cost)
subtraction = (Revenue - Cost)
multiplication = (Revenue * Cost)
division = (Revenue / Cost)


display_results = bool(input("Do you want to see the results? (yes/no): "))





if choice == 1:Revenue
print("The result is:" ,Revenue)
if choice == 2:Cost
print("The result is:" ,Cost)
if choice == 3:Profit
print("The result is:" ,Profit)


margin = (Profit / Revenue) * 100
if display_results:
    print(f"Profit Margin: {margin:.2f}%")



#RESULTS