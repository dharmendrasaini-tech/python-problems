

# 51. Input Range Validation — Medium
# Repeatedly ask for an age until the user enters a number from 0 through 120.
# Assume the user enters numeric text.
# Print the number of invalid attempts.
# Focus: validation loop.


invalid_attempts = 0

while True:

    age = int(input())

    if 0 <= age <= 120:
        break
    
    invalid_attempts += 1

print(invalid_attempts)




# 52. First Divisible Number — Medium
# Search numbers from 1 through 100 and print the first number divisible by both 7 and 11.
# Stop immediately after finding it.
# Focus: break.

for i in range(1,101):
    if i % 7 == 0 and i % 11 == 0:
        print(i)
        break




# 53. Skip Multiples — Easy
# Print numbers from 1 through 50, except numbers divisible by 3.
# Use continue.
# Focus: continue.

for number in range(1,51):
    if number % 3 == 0:
        continue

    print(number)




# 54. Menu Placeholder with pass — Easy
# Create a small menu with these options:
# 1. Add
# 2. Edit
# 3. Delete
# 4. Exit
# Implement only Exit. Use pass as a temporary placeholder for the unfinished options.
# Explain why pass is different from continue.
# Focus: pass.

command = input().strip().lower()

if command == "1.add":
    pass

elif command == "2.edit":
    pass
elif command == "3.delete":
    pass
elif command == "4.exit":
    print("Exit the program.")




# 55. Prime Check with Loop else — Challenge
# Accept an integer greater than 1.
# Use a loop to search for a divisor.
# •	If a divisor is found, print "Not prime" and break.
# •	If no divisor is found, use the loop’s else block to print "Prime".
# Focus: loop else, break, invariants.

number = int(input())

for i in range(2,number):
    if number % i == 0:
        print("Not prime")
        break


else:
    print("Prime")




# 56. Nested Multiplication Table — Medium
# Print multiplication tables from 1 through 5.
# Each table should contain multipliers 1 through 10.
# Focus: nested loops.

for i in range(1,6):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")


# 57. Rectangle Pattern — Easy
# Accept rows and columns and print a rectangle of *.
# Example:
# Rows: 3
# Columns: 5

# *****
# *****
# *****
# Focus: nested loops.


rows = int(input())
cols = int(input())

for row in range(rows):
    for col in range(cols):
        print("*",end="")

    print()




# 58. Coordinate Pairs — Medium
# Using nested loops, print all coordinate pairs where:
# x is from 0 to 2
# y is from 0 to 3
# Then count the total number of pairs.
# Focus: nested loops, counting.

pairs = 0

for x in range(3):
    for y in range(4):
        print((x,y))

        pairs += 1

print(pairs)




# Iteration Helpers and Mixed Problems
# 59. Ranking with enumerate() — Easy
# Given a sequence of names:
# names = ["Asha", "Ravi", "Meera", "Kabir"]
# Print rankings starting from 1.
# Expected form:
# 1. Asha
# 2. Ravi
# Do not maintain the position manually.
# Focus: enumerate().


names = ["Asha","Ravi","Meera","Kabir"]

for index, name in enumerate(names,start=1):
    print(f"{index}. {name}")


# 60. Product Invoice with zip() — Medium
# Given:
# products = ["Book", "Pen", "Bag"]
# prices = [500, 20, 1200]
# Print each product beside its price using zip().
# Then calculate the total.
# Focus: zip(), parallel iteration.

products = ["Book", "Pen", "Bag"]
prices = [500, 20, 1200]

product_width = 15
price_width = 10

total = 0

print("-" * (product_width + price_width))
print(f"{'Product':<{product_width}}{'Price':>{price_width}}")
print("-" * (product_width + price_width))


for product, price in zip(products, prices):
    print(f"{product:<{product_width}}₹{price:>{price_width-1},}")
    total += price

print("-" * (product_width + price_width))
print(f"{'Total':<{product_width}}₹{total:>{price_width-1},}")
print("-" * (product_width + price_width))

