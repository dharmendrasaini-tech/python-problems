# 61. Unequal zip() Inputs — Predict
# Predict what happens:
# names = ["A", "B", "C", "D"]
# scores = [80, 90]


# for name, score in zip(names, scores):
#     print(name, score)
# Explain:
# •	How many iterations occur?
# •	What happens to the extra elements?
# •	Why could this be dangerous?
# Focus: zip() behaviour.


# Two iterations occur because zip() stops when the shorter iterable ends.

# The extra elements "C" and "D" remain in the names list,
# but zip() ignores them during iteration.

# This can be dangerous because missing data is ignored silently.
# The program does not produce an error, so you may not notice
# that some names were never processed.



# 62. Off-by-One Debugging — Debug
# This code should print numbers from 1 through 10:
# for number in range(1, 10):
#     print(number)
# Fix it.
# Then write ranges for:
# •	0 through 10
# •	10 through 1
# •	Every even number from 2 through 20
# Focus: range boundaries.


for number in range(1, 11):
    print(number)

for number in range(11):
    print(number)

for number in range(10,0,-1):
    print(number)

for number in range(2,21):
    if number % 2 == 0:
        print(number)



# 63. FizzBuzz — Medium
# Print numbers from 1 through 100.
# •	Multiples of 3 → "Fizz"
# •	Multiples of 5 → "Buzz"
# •	Multiples of both → "FizzBuzz"
# •	Otherwise → the number
# Explain why the combined condition must be checked first.
# Focus: condition ordering.

for i in range(1,101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)

#The combined condition must come first because Python stops checking an if–elif chain as soon as one condition is true.





# 64. ATM Withdrawal Validator — Challenge
# Accept:
# •	Account balance
# •	Withdrawal amount
# •	Whether the account is active
# Allow withdrawal only when:
# •	Account is active
# •	Amount is positive
# •	Amount is a multiple of ₹100
# •	Amount does not exceed the balance
# Print the precise reason when rejected.
# Focus: defensive conditions, ordering, boundaries.

account_balance = int(input())
withdrawal_amount = int(input())
is_account_active = input().strip().lower() == "yes"

if not is_account_active:
    print("Account is inactive.")
elif withdrawal_amount <= 0:
    print("Withdrawal amount must be positive.")
elif withdrawal_amount % 100 != 0:
    print("Please enter amount in multiples of 100.")
elif withdrawal_amount > account_balance:
    print("Insufficient balance.")

else:
    print("Amount withdrawn.")







# 65. Number Guessing Game — Challenge
# Use a fixed secret number.
# Repeatedly ask the user to guess until correct.
# After each guess, print:
# •	"Too high"
# •	"Too low"
# •	"Correct"
# Count attempts.
# Add an optional maximum-attempt limit.
# Focus: while loop, conditions, state updates.

secret_number = 10
maximum_attempts = 5
attempts = 0

while attempts < maximum_attempts:

    attempts += 1
    number = int(input())

    if number < secret_number:
        print("Too low")
    elif number > secret_number:
        print("Too high")
    else:
        print("Correct")
        break

else:
    print("Game over")

    


# 66. Menu-Driven Unit Converter — Challenge
# Repeatedly show:
# 1. Metres to kilometres
# 2. Kilometres to metres
# 3. Celsius to Fahrenheit
# 4. Fahrenheit to Celsius
# 5. Exit
# Requirements:
# •	Use match or if/elif.
# •	Continue until Exit is chosen.
# •	Reject unknown menu choices.
# •	Ask only for inputs needed by the selected conversion.
# Covers: control flow, loops, arithmetic, menus.

while True:
    print("1. Metres to kilometres")
    print("2. Kilometres to metres")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Exit")

    selected_option = int(input())

    match selected_option:
        case 1:
            metres = float(input())
            print(f"There are {metres/1000:.2f} km in {metres:.2f}.")

        case 2:
            kilometres = float(input())
            print(f"There are {kilometres * 1000:.2f} metres in {kilometres:.2f}.")

        case 3:
            celsius = float(input())
            print(f"There are {(celsius * 9/5) + 32:.2f} fahrenheit in {celsius:.2f}.")

        case 4:
            fahrenheit = float(input())
            print(f"There are {(fahrenheit-32) * 5/9:.2f} celsius in {fahrenheit:.2f}.")

        case 5:
            break

        case _:
            print("Invalid menu option.")



