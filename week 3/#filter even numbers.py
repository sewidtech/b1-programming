#filter even numbers

def print_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is even")

# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Call the function
print_even_numbers(numbers)