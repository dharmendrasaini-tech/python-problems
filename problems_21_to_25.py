# Prediction and Debugging Problems
# 21. Operator Precedence Prediction — Medium
# Predict each result without running the code:
# print(2 + 3 * 4)
# print((2 + 3) * 4)
# print(10 > 5 and 3 < 1)
# print(True or False and False)
# print(not 5 == 5)
# print(8 / 2 ** 2)
# After predicting, run the program and explain any incorrect predictions.
# Focus: operator precedence.

# Ans - 14
# Ans - 20
# Ans - True
# Ans - False
# Ans - False
# Ans - 2

print(2 + 3 * 4)
print((2 + 3) * 4)
print(10 > 5 and 3 < 1)
print(True or False and False)
print(not 5 == 5)
print(8 / 2 ** 2)


# 22. Parentheses for Clarity — Medium
# Rewrite this expression with parentheses so that its intended grouping is obvious:
# age >= 18 and has_id or has_permission and not account_blocked
# Then describe the conditions under which it becomes True.
# Focus: logical operators, precedence, readability.

#Ans - # (age >= 18 and has_id) or (has_permission and not account_blocked)
#Ans - It becomes True when the age is at least 18 and has id or has permission and account is not blocked.




# 23. Conversion Bug — Debug
# The following program fails:
# age = input("Enter your age: ")
# future_age = age + 5
# print(future_age)
# Correct it and explain why the original failed.
# Also determine what happens when the user enters "34".
# Focus: input always returning a string.

#Ans - the original failed because input always return string.

age = int(input("Enter your age: "))
future_age = age + 5
print(future_age)


# 24. Concatenation Bug — Debug
# Correct this program:
# price = 99.5
# quantity = 3
# print("Total: " + price * quantity)
# Solve it in two ways:
# 1. Explicit conversion to a string.
# 2. An f-string.
# Focus: strings, arithmetic, formatting.


#1. Explicit conversion to a string.

price = 99.5
quantity = 3

print("Total: " + str(price * quantity))

#2. An f-string

print(f"Total: {price * quantity:.2f}")





# 25. Division Assumption — Debug
# This code is intended to calculate the average of three numbers:
# first = 10
# second = 20
# third = 30

# average = first + second + third / 3
# print(average)
# Fix the logic and explain the precedence problem.
# Focus: precedence, assumptions.

first = 10
second = 20
third = 30

average = (first + second + third)/3

print(average)

#Python will evaluate division first therefore we need to enclose first , second and third in parantheses.



