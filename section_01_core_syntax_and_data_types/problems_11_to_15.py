# Application Problems
# 11. BMI Calculator — Easy
# Accept:
# •	Weight in kilograms
# •	Height in metres
# Calculate:
# BMI = weight / height²
# Display the result to two decimal places.
# Classification belongs to Section 2, so this problem only calculates the number.
# Focus: input, floats, exponentiation, formatting.


weight = float(input())
height = float(input())

bmi = weight / (height ** 2)

print(f"BMI : {bmi:.2f}")


# 12. Simple Interest Calculator — Easy
# Accept:
# •	Principal
# •	Annual interest rate
# •	Time in years
# Calculate simple interest and total amount.
# Simple interest = principal × rate × time / 100
# Focus: arithmetic, numeric types.


principal = float(input())
annual_interest = float(input())
time = float(input())

simple_interest = (principal * annual_interest * time) / 100

total_amount = principal + simple_interest

print(f"Simple interest : {simple_interest:.2f}")
print(f"Total amount : {total_amount:.2f}")


# 13. Shopping Bill — Easy
# Accept:
# •	Product name
# •	Price per item
# •	Quantity
# •	Tax percentage
# Calculate:
# •	Subtotal
# •	Tax amount
# •	Final total
# Print a formatted receipt.
# Focus: strings, floats, integers, f-strings.

product_name = input()
price_per_item = float(input())
quantity = int(input())
tax_percentage = float(input())
subtotal = (price_per_item * quantity)
tax_amount = (subtotal * tax_percentage)/100
final_total = subtotal + tax_amount



print("============== Payment Receipt ==============")

print(f"Product name    : {product_name}")
print(f"Price           : ₹ {price_per_item:.2f}")
print(f"Quantity        : {quantity}")
print(f"Subtotal        : ₹ {subtotal:.2f}")
print(f"Tax Amount      : ₹ {tax_amount:.2f}")

print("-------------------------------------------")
print(f"Final Total     : ₹ {final_total:.2f}")
print("-------------------------------------------")



# 14. Currency Note Breakdown — Medium
# Accept an integer amount and calculate the minimum number of these notes required:
# ₹500, ₹200, ₹100, ₹50, ₹20, ₹10, ₹5, ₹2, ₹1
# Assume unlimited notes are available.
# Example:
# ₹786 = 1×₹500, 1×₹200, 1×₹50, 1×₹20, 1×₹10, 1×₹5, 1×₹1
# Focus: floor division, remainder, assignment.

amount = int(input())

five_hundred_notes = amount // 500
remaining_amount = amount % 500

two_hundred_notes = remaining_amount // 200
remaining_amount = remaining_amount % 200

one_hundred_notes = remaining_amount // 100
remaining_amount = remaining_amount % 100

fifty_notes = remaining_amount // 50
remaining_amount = remaining_amount % 50

twenty_notes = remaining_amount // 20
remaining_amount = remaining_amount % 20

ten_notes = remaining_amount // 10
remaining_amount = remaining_amount % 10

five_notes = remaining_amount // 5
remaining_amount = remaining_amount % 5

two_notes = remaining_amount // 2
remaining_amount = remaining_amount % 2

one_notes = remaining_amount

print(f"=== Notes in ₹{amount} ===")
print(f"{five_hundred_notes} * ₹500")
print(f"{two_hundred_notes} * ₹200")
print(f"{one_hundred_notes} * ₹100")
print(f"{fifty_notes} * ₹50")
print(f"{twenty_notes} * ₹20")
print(f"{ten_notes} * ₹10")
print(f"{five_notes} * ₹5")
print(f"{two_notes} * ₹2")
print(f"{one_notes} * ₹1")



# 15. Average Speed Calculator — Easy
# Accept:
# •	Distance travelled
# •	Time taken in hours
# Display the average speed to two decimal places.
# Also display whether the speed is exactly equal to a supplied reference speed as a boolean.
# Focus: division, comparison, booleans.

distance = float(input())
time = float(input())
average_speed = distance / time
reference_speed = float(input())

print(f"Average speed: {average_speed:.2f}")
print(f"is_equal_to_reference_speed : {average_speed == reference_speed}")







