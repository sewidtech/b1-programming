#calculator



def add(a, b):

    return a + b

def subtract(a, b):

    return a - b

def multiply(a, b):

    return a * b

def divide(a, b):

    if b == 0:

        return "Error: Division by zero is not allowed."

    return a / b

def calculator():
    print("Welcome to calculator")

    #MENU
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    Choice = input("Enter choice(1/2/3/4): ")

    if Choice not in ('1', '2', '3', '4'):
        print("Invalid input")
        return

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    if Choice == '1':
        result = add(number1, number2)
        print(f"{number1} + {number2} = {result}")
    elif Choice == '2':
        result = subtract(number1, number2)
        print(f"{number1} - {number2} = {result}")
    elif Choice == '3':
        result = multiply(number1, number2)
        print(f"{number1} * {number2} = {result}")
    elif Choice == '4':
        result = divide(number1, number2)
        print(f"{number1} / {number2} = {result}")




calculator()

print("Thank you for using calculator")

    
