# 1. Personal Introduction Card — Easy
# Store the following information in appropriately named variables:
# •	Name
# •	Age
# •	City
# •	Profession you are targeting
# •	Whether you are currently learning Python
# Print everything as a neatly formatted introduction.
# Focus: variables, naming, strings, integers, booleans, output.

name = "Dharmendra Saini"
age = 32
city = "Jaipur"
target_profession = "Software Engineer"
learning_python = True

python_status = "Yes" if learning_python else "No"

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"I live in {city}.")
print(f"I am targeting {target_profession} roles.")
print(f"Currently learning Python : {learning_python}.")

#Note - I learned to present the last line in a way the output is more readable. For example using "Yes" or "No" instead of True or False. For this i had to create a new variable and an 'if' condition.Store data in the form best suited for logic ; display it in the form best suited for humans.


# 2. Variable Naming Review — Easy
# You are given these proposed variable names:
# user_name
# 2nd_user
# total-price
# class
# monthlySalary
# is_active
# For each name:
# 1. Decide whether it is valid Python.
# 2. Correct invalid names.
# 3. Improve valid but poorly styled names according to Python conventions.
# Focus: naming rules and conventions.

print("user_name : Valid.")
print("2nd_user : Invalid , Correction: second_user.")
print("total-price : Invalid, Correction: total_price.")
print("class: Invalid, Correction: class_name.")
print("monthlySalary : Valid , but poorly styled. Improvement: monthly_salary.")
print("is_active : Valid.")

# 3. Swap Two Values — Easy
# Store two values in variables and exchange their values.
# Example:
# Before: first = 10, second = 25
# After: first = 25, second = 10
# Solve it:
# 1. Using a temporary variable.
# 2. Using Python tuple-style assignment.
# Focus: assignment.

#using a temporary variable
first = 10
second = 25

temp = first
first = second
second = temp

print(f"first : {first}, second: {second}.")

#using python - tuple style assignment

first = 10
second = 25

first,second = second,first

print(f"first : {first}, second : {second}.")

#Note: Python evaluates the right-hand side first, then assigns them to the variables on the left side in opposite order, so neither value is lost.


# 4. Basic Arithmetic Report — Easy
# Accept two numbers from the user and display:
# •	Addition
# •	Subtraction
# •	Multiplication
# •	Division
# •	Floor division
# •	Remainder
# •	Exponentiation
# Assume the second number is not zero.
# Focus: input, conversion, arithmetic operators.

num1 = int(input())
num2 = int(input())

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
remainder = num1 % num2
exponentiation = num1 ** num2

print("addition : ", addition)
print("subtraction : ", subtraction)
print("multiplication : ", multiplication)
print("division : ", division)
print("floor_division : ", floor_division)
print("remainder : ", remainder)
print("exponentiation : ", exponentiation)

#Note - Floor division removes the fractional part by rounding down.

# 5. Seconds Converter — Easy
# Accept a total number of seconds and convert it into:
# hours, minutes, seconds
# Example:
# Input: 7384
# Output: 2 hours, 3 minutes, 4 seconds
# Use // and %.
# Focus: integers, floor division, remainder.

seconds = int(input())

# 1hr = 3600 seconds

hours = seconds // 3600

seconds_left = seconds % 3600

minutes = seconds_left // 60 

remaining_seconds = seconds_left % 60


print(f"{hours} hours, {minutes} minutes, {remaining_seconds} seconds.")









































#Problem 3
#Problem 4
#Problem 5

