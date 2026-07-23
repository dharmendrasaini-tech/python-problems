# match Problems
# 41. Day Number — Easy
# Use match and case to convert:
# 1 → Monday
# 2 → Tuesday
# ...
# 7 → Sunday
# Handle any other value as invalid.
# Focus: match, wildcard case.


day = int(input())

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid value")



    

# 42. CLI Command Interpreter — Medium
# Accept one command:
# start
# stop
# pause
# status
# help
# Use match to print what the command does.
# Handle unknown commands.
# Focus: structural pattern matching.

command = input().strip().lower()

match command:
    case "start":
        print("Start the program.")
    case "stop":
        print("Stop the program.")
    case "pause":
        print("Pause the program.")
    case "status":
        print("Show the current Status.")
    case "help":
        print("Show the help Section.")
    case _:
        print("Unknown command")



# 43. Simple Calculator with match — Medium
# Accept:
# •	First number
# •	Operator
# •	Second number
# Support:
# +, -, *, /
# Use match for the operator.
# Handle division by zero using a condition.
# Focus: match, arithmetic, defensive branching.

first_number = int(input())
operator = input().strip()
second_number = int(input())

match operator:
    case "+":
        print(first_number + second_number)
    case "-":
        print(first_number - second_number)
    case "*":
        print(first_number * second_number)
    case "/":
        if second_number == 0:
            print("Cannot divide by zero.")
        else:
            print(first_number / second_number)

    case _:
        print("Invalid operator.")

#int(input())          # int() handles surrounding whitespace



# 44. HTTP Status Category — Medium
# Use match to display meanings for:
# 200, 201, 400, 401, 403, 404, 500
# Use one combined case for statuses that share a broad category where appropriate.
# Focus: multiple patterns in match.

http_status = int(input())

match http_status:
    case 200 | 201:
        print("Success")
    case 400 | 401 | 403 | 404:
        print("Client Error")
    case 500:
        print("Server Error")

    case _:
        print("Invalid status code.")



# Loop Problems
# 45. Print a Number Range — Easy
# Accept a start and end value and print every integer inclusively.
# Ensure your range() boundaries are correct.
# Focus: for, range(), off-by-one reasoning.


start_value = int(input())
end_value = int(input())

for i in range(start_value,end_value+1):
    print(i)




# 46. Sum from 1 to N — Easy
# Accept a positive integer n and calculate the sum from 1 through n using a loop.
# Do not use sum().
# Test:
# n = 1
# n = 5
# n = 100
# Focus: accumulator pattern.

n = int(input())
total = 0

for i in range(1,n+1):
    total += i

print(total)



# 47. Multiplication Table — Easy
# Accept a number and display its multiplication table from 1 through 10.
# Format each line clearly.
# Focus: loops, range.

number = int(input())

for i in range(1,11):
    print(f"{number} * {i} = {number * i}")



# 48. Count Even and Odd Numbers — Medium
# Accept how many numbers the user wants to enter.
# Read those numbers one at a time and count:
# •	Even values
# •	Odd values
# •	Zeros
# Decide whether zero should also count as even and explain your decision.
# Focus: loop counters, conditions.

number_count = int(input())
even_values = 0
odd_values = 0
zeros = 0

for _ in range(number_count):
    number = int(input())

    if number == 0:
        zeros += 1
        
    if number % 2 == 0:
        even_values += 1

    else:
        odd_values += 1

print(f"zeros: {zeros}")
print(f"even_values: {even_values}")
print(f"odd_values: {odd_values}")

#zero should also count as even number because 0 % 2 == 0





# 49. Countdown with while — Easy
# Accept a starting number and count down to zero.
# After zero, print "Launch!".
# Reject a negative starting number with a condition.
# Focus: while, update invariant.

starting_number = int(input())

if starting_number < 0:
    print("Negative number not allowed.")

else:
    while starting_number >= 0:
        print(starting_number)
        starting_number -= 1

    print("Lanuch!")




# 50. Password Retry — Medium
# Give the user at most three attempts to enter a predefined password.
# Stop immediately when the password is correct.
# Print a failure message after all attempts are used.
# Focus: while, attempt counters, break.

correct_password = "password123"

attempts = 0

while attempts < 3:
    entered_password = input()

    if entered_password == correct_password:
        print("Access Granted.")
        break

    attempts += 1

if attempts == 3:
    print("Access Denied.")
