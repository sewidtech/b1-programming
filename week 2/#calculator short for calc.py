print("Welcome to calculator")

#MENU
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")



Choice = input("Enter choice(1/2/3/4): ")


if Choice not in ('1', '2', '3', '4'):print("Invalid input")

if Choice not in ('1', '2', '3', '4'): exit()


number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

sum = number1 + number2
subtract = number1 - number2
multiply = number1 * number2
divide = number1 / number2



if Choice in ('1') :sum = number1 + number2
if Choice in ('2') :subtract = number1 - number2
if Choice in ('3') :multiply = number1 * number2
if Choice in ('4') :divide = number1 / number2




if Choice == '1':print(result := f"{number1} + {number2} = {sum}")
if Choice == '2':print(result := f"{number1} - {number2} = {subtract}")
if Choice == '3':print(result := f"{number1} * {number2} = {multiply}")
if Choice == '4':print(result := f"{number1} / {number2} = {divide}")


if Choice == '4' and number2 == 0:
    print("Error: Division by zero is not allowed.")
3

print("Thank you for using calculator")