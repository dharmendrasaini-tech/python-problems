# Conditional Problems
# 31. Positive, Negative, or Zero — Easy
# Accept a number and print whether it is:
# •	Positive
# •	Negative
# •	Zero
# Test:
# 10, -4, 0
# Focus: if, elif, else.

number = int(input())

if number < 0:
    print("Negative")
elif number == 0:
    print("Zero")
else:
    print("Positive")



# 32. Even or Odd — Easy
# Accept an integer and determine whether it is even or odd.
# Also test negative integers and zero.
# Focus: conditions, remainder.

number = int(input())

if number % 2 == 0:
    print("Even")
else:
    print("Odd")



# 33. Age Category — Easy
# Classify a person into:
# 0–2: Infant
# 3–12: Child
# 13–17: Teenager
# 18–59: Adult
# 60 or above: Senior
# Reject negative ages using a condition.
# Focus: ordered conditions, boundaries.

age = int(input())

if age < 0:
    print("Invalid age.")
elif age >= 60:
    print("Senior")
elif age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
elif age >= 3:
    print("Child")
else:
    print("Infant")


# 34. Largest of Three Numbers — Medium
# Accept three numbers and print the largest.
# Handle equal values correctly.
# Examples:
# 10, 20, 15
# 20, 20, 5
# 8, 8, 8
# Focus: conditions and equality.

number1 = int(input())
number2 = int(input())
number3 = int(input())


if number1 >= number2 and number1 >= number3:
    print(number1)
elif number2 >= number1 and number2 >= number3:
    print(number2)
else:
    print(number3)



# 35. Grade Calculator — Easy
# Convert a score into:
# 90–100: A
# 80–89: B
# 70–79: C
# 60–69: D
# Below 60: F
# Print "Invalid score" when the score is outside 0–100.
# Focus: validation and boundary conditions.

score = int(input())

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


#Validate first, then check ordered boundaries from highest to lowest.



# 36. Leap Year — Medium
# Determine whether a year is a leap year.
# Rules:
# •	Divisible by 400 → leap year
# •	Divisible by 100 but not 400 → not a leap year
# •	Divisible by 4 but not 100 → leap year
# •	Otherwise → not a leap year
# Test:
# 1900, 2000, 2024, 2025
# Focus: logical operators, ordered rules.

year = int(input())

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")



# 37. Triangle Validity — Medium
# Accept three side lengths.
# First determine whether they can form a triangle:
# a + b > c
# a + c > b
# b + c > a
# If valid, classify it as:
# •	Equilateral
# •	Isosceles
# •	Scalene
# Focus: nested conditions, validation.

a = int(input())
b = int(input())
c = int(input())

is_valid = (a + b > c) and (a + c > b) and (b + c > a)

if is_valid:
    if a == b == c:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Scalene")



# 38. Login Decision — Medium
# Accept:
# •	Username
# •	Password
# •	Whether the account is blocked
# Rules:
# •	Credentials must match predefined values.
# •	A blocked account must not be allowed to log in.
# •	Print a specific reason for failure.
# Use nested conditions so the logic is easy to follow.
# Focus: nested conditions.

username = input()
password = input()
account_blocked = input().strip().lower() == "yes"

correct_username = "dsputania"
correct_password = "python123"

if username == correct_username:
    if password == correct_password:
        if account_blocked:
            print("Account is blocked.")
        else:
            print("Access granted.")
    else:
        print("Invalid Password.")

else:
    print("Invalid Username.")




# 39. Truthy and Falsy Inputs — Medium
# Create variables containing:
# ""
# "Python"
# 0
# 1
# None
# False
# Use each directly inside an if statement and record whether Python treats it as truthy or falsy.
# Then write one sentence describing the general rule.
# Focus: truthiness.


name1 = ""
language2 = "Python"
number3 = 0
number4 = 1
is_valid5 = None
is_completed6 = False

if name1:
    print("Truthy1")

else:
    print("Falsy1")

if language2:
    print("Truthy2")
else:
    print("Falsy2")

if number3:
    print("Truthy3")
else:
    print("Falsy3")

if number4:
    print("Truthy4")
else:
    print("Falsy4")

if is_valid5:
    print("Truthy5")
else:
    print("Falsy5")

if is_completed6:
    print("Truthy6")
else:
    print("Falsy5")


#1. Empty string is considered as falsy value.
#2. Non- empty string is considered as truthy value.
#3. 0 is considered as falsy value.
#4. Any non-zero digit is consideered as truthy value.
#5. None is considered as falsy value.
#6. False is considered as falsy value.

#Python treats empty values, zero, None, and False as falsy; most non-empty and non-zero values are truthy.





# 40. Conditional Expression — Easy
# Accept a number and assign either "Even" or "Odd" using a conditional expression:
# result = value_if_true if condition else value_if_false
# Then print the result.
# Focus: ternary expression.

number = int(input())

result = "Even" if number % 2 == 0 else "Odd"

print(result)
