# 16. Eligibility Expression — Medium
# Accept:
# •	Age
# •	Whether the person has an ID
# •	Whether the person has special permission
# Create one boolean expression representing:
# The person is eligible when they are at least 18 and have an ID, or when they have special permission.
# Print only the final boolean result.
# Do not use an if statement.
# Focus: logical operators and precedence.

age = int(input())
has_id = input().strip().lower() == "yes"
has_special_permission = input().strip().lower() == "yes"

is_eligible = (age >= 18 and has_id) or has_special_permission

print(is_eligible)


# 17. Membership Checker — Easy
# Accept:
# •	A word
# •	A character or smaller string
# Display whether the smaller value occurs inside the word.
# Use both:
# •	in
# •	not in
# Focus: membership operators.

word = input()
substring = input()

substring_in_word = substring in word
substring_not_in_word = substring not in word

print(substring_in_word)
print(substring_not_in_word)


# 18. Email Domain Checker — Easy
# Accept an email address and a domain such as:
# gmail.com
# Print whether the domain occurs in the email address.
# You do not need to validate whether the email is correctly formed.
# Focus: strings, membership.

email_address = input()
domain = input()

is_domain_in_email_address = domain in email_address

print(is_domain_in_email_address)

# 19. None as an Unknown Value — Medium
# Create a variable representing a user’s middle name and initially assign None.
# Print:
# •	Its value
# •	Its type
# •	Whether it is None
# Then assign an actual middle name and repeat the checks.
# Focus: None, identity operators.

middle_name = None

print(f"Middle name: {middle_name}")
print(f"Type: {type(middle_name)}")
print(f"is_None: {middle_name is None}")

middle_name = "Bahubali"

print(f"Middle name: {middle_name}")
print(f"Type: {type(middle_name)}")
print(f"is_None: {middle_name is None}")

#Mental model: == means same value; is means same object. For None, always use is.




# 20. Equality Versus Identity — Medium
# Predict the output before running:
# first = [1, 2, 3]
# second = first
# third = [1, 2, 3]

# print(first == second)
# print(first is second)
# print(first == third)
# print(first is third)
# Then explain:
# •	Which variables contain equal values?
# •	Which variables refer to the same object?
# •	Why are equality and identity different?
# Using lists here is only to demonstrate references; no list operations are required.
# Focus: == versus is.


first = [1, 2, 3]
second = first
third = [1, 2, 3]

print(first == second) #true
print(first is second) #true
print(first == third) #true
print(first is third) #false

# first and third
# first and second
# equality means same value and identity means same object


# Python variables are names that refer to objects. Writing second = first makes both names point to the same object, while creating another list separately makes a different object with possibly equal values. The == operator compares values, whereas is checks whether two variables refer to the exact same object. With mutable objects like lists, changes made through one shared reference are visible through the other.







