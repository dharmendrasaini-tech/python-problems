# 6. Temperature Converter — Easy
# Accept a temperature in Celsius and convert it into:
# •	Fahrenheit
# •	Kelvin
# Display both answers to two decimal places.
# Focus: floats, arithmetic, formatting.


celsius = float(input())

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print(f"celsius to fahrenheit: {fahrenheit:.2f}")
print(f"celsius to kelvin: {kelvin:.2f}")

#:.2f formats a number as a floating-point value with exactly two digits after the decimal point.

# 7. Rectangle Measurement Report — Easy
# Accept the length and width of a rectangle.
# Display:
# •	Area
# •	Perimeter
# •	Whether the rectangle is a square
# Do not use an if statement. Store the comparison result in a boolean variable.
# Focus: floats, comparison operators, booleans.

length = float(input())
width = float(input())

area = length * width
perimeter = 2 * (length + width)    

is_square = length == width

print(f"area : {area}")
print(f"perimeter : {perimeter}")
print(f"is_square : {is_square}")


# 8. Type Explorer — Easy
# Create values of these types:
# •	Integer
# •	Float
# •	Complex number
# •	Boolean
# •	String
# •	None
# Print each value together with its type using type().
# Focus: built-in data types.

integer_number = 5

float_number = 14.00
complex_number = 3 + 6j
boolean_value = True
string_value = "Dharmendra"
none_value = None

print(f" Integer: {integer_number} , {type(integer_number)}")
print(f" Float: {float_number}, {type(float_number)}")
print(f" Complex_number: {complex_number}, {type(complex_number)}")
print(f" Boolean: {boolean_value}, {type(boolean_value)}")
print(f" String: {string_value}, {type(string_value)}")
print(f" None: {none_value}, {type(none_value)}")

#In an f-string, curly braces {} can contain any valid Python expression, including variables, calculations, #comparisons, and function calls.
# Python evaluates that expression first, converts the result to a string, and inserts it into the final #output.


# 9. Complex Number Calculator — Easy
# Create two complex numbers and display:
# •	Their sum
# •	Their difference
# •	Their product
# •	The real and imaginary parts of each number
# Focus: complex numbers.

num1 = 3 + 5j
num2 = 2 - 6j


print(f"Sum : {num1 + num2}")
print(f"Difference : {num1 - num2}")
print(f"Product : {num1 * num2}")

print(f"num1 Real part: {num1.real}")
print(f"num1 Imaginary part: {num1.imag}")

print(f"num2 Real part: {num2.real}")
print(f"num2 Imaginary part: {num2.imag}")

# 10. Explicit Type Conversion — Easy
# Start with these values:
# age = "34"
# price = "499.75"
# items = 3
# Convert them as needed and calculate:
# Age after five years
# Total price for three items
# Print the resulting values and their types.
# Focus: int(), float(), type conversion.


age = "34"
price = "499.75"
items = 3

age_after_five = int(age) + 5

price_for_three = float(price) * items

print(f"Age after five: {age_after_five}, type: {type(age_after_five)}")
print(f"Price for three: {price_for_three}, type: {type(price_for_three)}")

# Python automatically produces a float when multiplying a float by an int.

























