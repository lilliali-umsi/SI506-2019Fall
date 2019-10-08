# START LAB EXERCISE 04
print('Lab Exercise 04 \n')

# SETUP
# Data description
# Problem 3 will involve working with the list of integers named numbers.
numbers = [1, 2, 3, 4, 5, 6]

# Print statements have been provided as an aid to debugging.
# Uncomment them as necessary to view the output of your work.

# END SETUP


# PROBLEM 1 (5 Points)
# Define a function named multiply. The function accepts two arguments, both integers,
# For this problem pass to the function the integers 506 and 507, multiply them together,
# and return the result.

# BEGIN PROBLEM 1 SOLUTION

def multiply(x, y):
    return x * y


print(f"multiply() = {multiply(506, 507)}")
# END PROBLEM 1 SOLUTION


# PROBLEM 2 (10 Points)
# Define a function named greeting. The function accepts a string value and adds the value to
# a string comprising the greeting, i.e., "How are you doing <name>?
# For this problem the value to pass to the function is "Rob".

# BEGIN PROBLEM 2 SOLUTION

def greeting(name):
    line = 'How are you doing {}?'.format(name)
    return line


print(f"greeting() = {greeting('Rob')}")
# END PROBLEM 2 SOLUTION


# PROBLEM 3 (10 Points)
# Define a function named sum_all. The function accepts a list of integers named numbers as an argument.
# Call the function passing it numbers and iterate over the list, returning the sum of the integers in the list.

# BEGIN PROBLEM 3 SOLUTION
def sum_all(numbers):
    s = 0
    for i in numbers:
        s = s + i
    return s


print(f"sum_all() = {sum_all(numbers)}")
# END PROBLEM 3 SOLUTION

# END LAB EXERCISE
