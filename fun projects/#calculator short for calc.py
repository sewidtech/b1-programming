import sys
import logging
logging.basicConfig(
    level = logging.INFO ,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = input("What is your name? ")

print(f"Welcome to the calculator, {name}.")
logging.info('user started calculator : {name}')

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice (1/2/3/4): ")



if choice not in ('1', '2', '3', '4'):
    logging.warning(f"{name} entered invalid choice : {choice}")
    exit()

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

try:
    if choice == '1':
        result = number1 + number2
        print(f"{number1} + {number2} = {result}")
        logging.info(f"{name} performed addition")
    if choice == '2':
        result = number1 - number2
        print(f"{number1} - {number2} = {result}")
        logging.info(f'{name} performed subtraction')
    if choice == '3':
        result = number1 * number2
        print(f"{number1} * {number2} = {result}")
        logging.info(f'{name} performed multiplication')
    if choice == '4':
        result = number1 / number2
        print(f"{number1} / {number2} = {result}")
        logging.info(f'{name} performed division')

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    logging.error(f"{name} attempted division by zero : {number1} / {0}")

print(f"Thank you for using the calculator, {name}.")
