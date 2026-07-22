
# 26. Comparison Chain Prediction — Medium
# Predict:
# age = 25

# print(18 <= age <= 60)
# print(age < 18 < 10)
# print(20 < age == 25)
# Rewrite each chained comparison using and.
# Focus: comparison operators.

age = 25

#True
#False
#True

print(18 <= age and age <= 60)
print(age < 18 and 18 < 10)
print(20 < age and age == 25)




# 27. Floating-Point Surprise — Challenge
# Run and inspect:
# result = 0.1 + 0.2

# print(result)
# print(result == 0.3)
# Explain why the comparison may be false.
# Then display the result rounded to two decimal places.
# You do not need to solve floating-point precision fully yet.
# Focus: floats, representation, comparison.


result = 0.1 + 0.2

#It only changes how the number is displayed. It does not change the actual stored value.
print(f"result : {result:.2f}")


print(result == 0.3)

#0.30000000000000004 is the floating-point approximation of 0.3, caused by the limited precision of binary floating-point representation.



# 28. Comments and Docstrings — Easy
# Write a small program that calculates the area of a circle.
# Include:
# •	A module-level docstring explaining the program
# •	One useful comment explaining a non-obvious line
# •	Clear variable names
# •	No comments that merely repeat the code
# Focus: comments, docstrings, readability.

"""Calculate the area of a circle from user-provided radius"""

radius = float(input())

value_of_pi = 3.14

area = value_of_pi * (radius ** 2)


print(f"Area of circle with radius : {radius} is {area:.2f}")




# 29. Formatted Invoice — Medium
# Create an invoice showing:
# •	Product name
# •	Unit price
# •	Quantity
# •	Subtotal
# •	Discount
# •	Final amount
# Formatting requirements:
# •	Currency values must have two decimal places.
# •	Product name must occupy a fixed-width column.
# •	Numerical values must be aligned.
# Focus: advanced f-string formatting.

product_name = input()
unit_price = float(input())
quantity = int(input())
subtotal = unit_price * quantity
discount = float(input())
final_amount = subtotal - discount

print()
print("=" * 40)
print(f"{'INVOICE':^40}")
print("=" * 40)
print()
print(f"{'Product':<18}{product_name:<22}")
print(f"{'Unit Price':<18}{unit_price:>22.2f}")
print(f"{'Quantity':<18}{quantity:>22}")
print("-" * 40)
print(f"{'Subtotal':<18}{subtotal:>22.2f}")
print(f"{'Discount':<18}{discount:>22.2f}")
print("-" * 40)
print(f"{'Final Amount':<18}{final_amount:>22.2f}")
print("=" * 40)





# 30. Mixed Order Summary — Challenge
# Accept:
# •	Customer name
# •	Item name
# •	Unit price
# •	Quantity
# •	Discount percentage
# •	Tax percentage
# •	Whether the customer is a premium member
# Calculate the final amount.
# Store and print these boolean facts without using if:
# •	Whether the order value is above ₹1,000
# •	Whether the customer is premium
# •	Whether the product name contains the word "Python"
# Produce a clean order summary.
# Covers: variables, types, conversion, arithmetic, comparison, logical operators, membership, booleans, input/output, f-strings.


customer_name = input()
item_name = input()
unit_price = float(input())
quantity = int(input())

order_value = unit_price * quantity

discount_percentage = float(input())
discount_amount = (order_value * discount_percentage)/100

amount_after_discount = order_value - discount_amount

tax_percentage = float(input())
tax_amount = (amount_after_discount * tax_percentage)/100

final_amount = amount_after_discount + tax_amount



is_customer_premium_member = input().strip().lower() == "yes"
is_python_in_product_name = "python" in item_name.lower()
is_order_value_above_1000 = order_value > 1000


print("=" * 40)
print(f"{'ORDER SUMMARY':^40}")
print("=" * 40)

print(f"{'Customer Name':<16}{customer_name:<24}")
print(f"{'Item Name':<16}{item_name:<24}")
print()
print(f"{'Unit Price':<16}{unit_price:>24.2f}")
print(f"{'Quantity':<16}{quantity:>24}")
print(f"{'Order Value':<16}{order_value:24.2f}")
print()
print(f"{'Discount':<16}{discount_amount:24.2f}")
print(f"{'Tax':<16}{tax_amount:24.2f}")
print("=" * 40)
print(f"{'Final Amount':<16}{final_amount:24.2f}")
print("=" * 40)
print(f"{'Above Rs 1000':<16}{str(is_order_value_above_1000):>24}")
print(f"{'Premium Member':<16}{str(is_customer_premium_member):>24}")
print(f"{'Contains Python':<16}{str(is_python_in_product_name):>24}")








































