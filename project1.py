'''A program that reads a sequence of numbers entered by the user.
   The number of input is recorded and given as a result.
   Occurrence is in terms of even or odd.
   The program terminates when zero is received as an input by the user
'''
#instantiate variables to store count
odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
# Check if the number is odd.
    if number % 2 == 0:
# Increase the odd_numbers counter.
        even_numbers += 1
    else:
# Increase the even_numbers counter.
        odd_numbers += 1
# Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

