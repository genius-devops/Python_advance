import math
# from icecream import icecream as ic # Debugging tool | ic function can serv as print function
print("Programming","Essentials","in", sep="***", end="...")
print("Python")

print()
print("*"*3, " "*3, "*"*3)

print()
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
print()

# Sample Solution

###################
print("original version:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("with fewer 'print()' invocations:")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("higher:\n")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("doubled:\n")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)

# section two python literals

print(0o123)  # the value is 83
print(0x123)  # output: 291
print(3e8)    # speed  of light
print(6.62607e-34)  # Planck's constant (h)
print(0.0000000000000000000001) # same as 1e-22
print("I like \"Monty Python\"")
# alternatively
print('i like "Monty Python"')
print('i\'m Monty Python')
print("i'm Monty Python")  # same as above
print(True > False)        # True
print(True < False)        # False
print("\"i\'m\"\n\"\"learning\"\"\n\"\"\"Python\"\"\" ")
# output: "I'm"
# ""learning""
# """Python"""
# "1.5", 2.0, 528, False
# The first is a string, the second is a numerical literal (a float), the third is a numerical literal (an integer), and the fourth is a boolean literal.
# 1011: It's 11, because (2**0) + (2**1) + (2**3) = 11
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

# How not to divide
# As you probably know, division by zero doesn't work.
#
# Do not try to:
#
# perform a division by zero;
# perform an integer division by zero;
# find a remainder of a division by zero.

print(-4 + 4)
print(-4. + 8)
print(9 % 6 % 2)  # modulo used left sided effect as in it runs from left to right
print(2 ** 2 ** 3)  # exponent give right sided effect in python instead of conventionally 64 but 256
print(-3 ** 2)   # -9
print(-2 ** 3)   # -8
print(-(3 ** 2))  # -9
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)  # 10.0
print(2 * 3 % 5)   # 1
print((2 ** 4), (2 * 4.), (2 * 4))  # 16 8.0 8
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))   # -0.5 0.5 0 -1
print((2 % -4), (2 % 4), (2 ** 3 ** 2))  # -2 2 512
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  # same as  c = math.sqrt(a ** 2 + b ** 2)
print("c =", c) # c = 5.0

john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=',')

total_apples = john + mary + adam
print(total_apples)

# peter = 12.5
# suzy = 2
# print(peter / suzy)
# print("Total number of apples:", total_apples)

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

# interaction with the users: THE INPUT() FUNCTION
name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

print("\nPress Enter to end the program.")
input()
print("THE END.")

print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

anything = input("Enter a number: ")
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# Testing a TypeError message.

anything = input("Enter a number: ")
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)


fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")


print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
# output
# +----------+
# |          |
# |          |
# |          |
# |          |
# |          |
# +----------+
# Note the way in which we've used the parentheses in the second line of the code.
#
# Try practicing to create other shapes or your own artwork!
#
# This type of conversion is not a one-way street. You can also convert a number into a string, which is way easier and safer ‒ this kind of operation is always possible.
#
# A function capable of doing that is called str():

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

a = float(input("Enter first value: "))
b = float(input("Enter second value: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("\nThat's all, folks!")

x = float(input("Enter value for x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')

name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

print("\nPress Enter to end the program.")
input()
print("THE END.")

var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

var = 0  # Assigning 0 to var
print(var != 0)

var = 1  # Assigning 1 to var
print(var != 0)

n = int(input("Enter a number: "))
print(n >= 100)

# The way to assemble subsequent if-elif-else statements is sometimes called a cascade.

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than the current largest_number
# and update the largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than the current largest_number
# and update the largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)

# use of elif
largest_number = number1
if number2 > largest_number:
    largest_number = number2
elif number3 > largest_number:
    largest_number = number3
print("The largest number is:", largest_number)


largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Go to line 02




# optimizing the code instead of using if statement
# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)


# Write a program that utilizes the concept of conditional execution, takes a string as input, and:
#
# prints the sentence "Yes - Spathiphyllum is the best
# plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
# prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
# prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

plant = input("Please enter a plant")
if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "pelargonium":
    print("Spathiphyllum! Not pelargonium!")
elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    pass

# marking scheme => required answer
name = input("Enter flower name: ")

if name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif name == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", name + "!")

#
# if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
# if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
Your task is to write a tax calculator.
#
# It should accept one floating-point value: the income.
# Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you – you'll find it in the skeleton code in the editor.
# solution


income = float(input("Enter the annual income: "))

if income < 85528:
    tax = income * 0.18 - 556.02
else:
    tax = (income - 85528) * 0.32 + 14839.02

if tax < 0.0:
    tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

#
# As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.
#
# Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:
#
# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.
year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")

x = 1
y = 1.0
z = "1"

if x == y:
    print("one")        # True: output is one
if y == int(z):
    print("two")        # True: output is two
elif x == y:
    print("three")
else:
    print("four")


# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)

# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

# the code below describes while loop in details and new programmers friendly
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

# this is also same as above
counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

#
# A junior magician has picked a secret number. He has hidden it in a variable named secret_number. He wants everyone who runs his program to play the Guess the secret number game, and guess what number he has picked for them. Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.
#
# Your task is to help the magician complete the code in the editor in such a way so that the code:
#
# will ask the user to enter an integer number;
# will use a while loop;
# will check whether the number entered by the user is the same as the number picked by the magician. If the number chosen by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, and the magician should say the following words: "Well done, muggle! You are free now."
# The magician is counting on you! Don't disappoint him.
# solution

secret_number = 777
num = int(input("enter a secret number: "))
while num:
    if num != secret_number:
        print("Ha ha! You're stuck in my loop!")
        num = int(input("enter a secret number: "))
        if num == secret_number:
            print("Well done, muggle! You are free now.")

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")


secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
# this line of code prints power of the iterated number
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

#
# Do you know what Mississippi is? Well, it's the name of one of the states and rivers in the United States. The Mississippi River is about 2,340 miles long, which makes it the second longest river in the United States (the longest being the Missouri River). It's so long that a single drop of water needs 90 days to travel its entire length!
#
# The word Mississippi is also used for a slightly different purpose: to count mississippily.
#
# If you're not familiar with the phrase, we're here to explain to you what it means: it's used to count seconds.
#
# The idea behind it is that adding the word Mississippi to a number when counting seconds aloud makes them sound closer to clock-time, and therefore "one Mississippi, two Mississippi, three Mississippi" will take approximately an actual three seconds of time! It's often used by children playing hide-and-seek to make sure the seeker does an honest count.
#
# Your task is very simple here: write a program that uses a for loop to "count mississippily" to five. Having counted to five, the program should print to the screen the final message "Ready or not, here I come!"
#
# Use the skeleton we've provided in the editor.

import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# Write a print function with the final message.

import time
for i in range(1, 5):
    print(i, "Mississippi")
# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# Write a print function with the final message.

# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end the program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


# the continue statement
largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end the program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")
#
# Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.
#
# Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.

secret_word = "chupacabra"
guess_word = input("enter a word ")
while True:
    if guess_word != secret_word:
        guess_word = input("enter a word ")
        continue
    if guess_word == secret_word:
        print("You've successfully left the loop.")
        break


# ask the user to enter a word;
# use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about string methods and the upper() method very soon – don't worry;
# use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
# print the uneaten letters to the screen, each one of them on a separate line.
# Test your program with the data we've provided for you.

# solution





# conventionally when iteration take place it also hold the last value after execusion
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)  # the i is 5

# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)        # only even number will be printed


text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")       # eat will x from the text variable

n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")

for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2

for i in range(0, 11):
    if i % 2 != 0:
        print(i)        # odd number will be printed

for i in range(0, 11):
    if i % 2:
        print(i)        # same as above

# alternatively
for i in range(11):
    if i % 2:
        print(i)

x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1


# Question 3: Create a program with a for loop and a break statement. The program should iterate over characters in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on one line. Use the skeleton below:
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

# Question 4: Create a program with a for loop and a continue statement. The program should iterate over a string of digits, replace each 0 with x, and print the modified string to the screen. Use the skeleton below:
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

n = 3

while n > 0:
    print(n + 1)  # 4 3 2
    n -= 1
else:
    print(n)  # 0

for i in range(0, 6, 3):
    print(i)   # 0, 3


# the statement below print all True
# Example 1:
var = 1
print(var > 0)
print(not (var <= 0))


# Example 2:
print(var != 0)
print(not (var == 0))

# bitwise operators
# & (ampersand) ‒ bitwise conjunction;
# | (bar) ‒ bitwise disjunction;
# ~ (tilde) ‒ bitwise negation;
# ^ (caret) ‒ bitwise exclusive or (xor).

# x = x & y	x &= y
# x = x | y	x |= y
# x = x ^ y	x ^= y

#
# Priority	Operator
# 1	~, +, -	unary
# 2	**
# 3	*, /, //, %
# 4	+, -	binary
# 5	<<, >>
# 6	<, <=, >, >=
# 7	==, !=
# 8	&
# 9	|
# 10	=, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=
#
# 1. Python supports the following logical operators:
#
# and → if both operands are true, the condition is true, e.g., (True and True) is True,
# or → if any of the operands are true, the condition is true, e.g., (True or False) is True,
# not → returns false if the result is true, and returns true if the result is false, e.g., not True is False.
# 2. You can use bitwise operators to manipulate single bits of data. The following sample data:
#
# x = 15, which is 0000 1111 in binary,
# y = 16, which is 0001 0000 in binary.
# will be used to illustrate the meaning of bitwise operators in Python. Analyze the examples below:
#
# & does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary,
# | does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary,
# ˜  does a bitwise not, e.g., ˜ x = 240*, which is 1111 0000 in binary,
# ^ does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
# >> does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary,
# << does a bitwise left shift, e.g., y << 3 = , which is 1000 0000 in binary.
# * -16 (decimal from signed 2's complement) -- read more about the Two's complement operation.

x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))   # false

x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)    # 0 5 -5 1 1 16 respectively

numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.

numbers[0] = 111
print("\nPrevious list contents:", numbers)  # Printing previous list contents.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list contents:", numbers)  # Printing current list contents.

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
n = int(input("enter a number: "))
# to replace the middle number with an integer number entered by the user.
hat_list[3] = n

# Step 2: write a line of code that removes the last element from the list.
del hat_list[4]

# Step 3: write a line of code that prints the length of the existing list.
len(hat_list)
print(hat_list)

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)      # list.insert(location, value)
print(len(numbers))
print(numbers)

#
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)


my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)# output: [5, 4, 3, 2, 1]   You should get the same sequence, but in reverse order (this is the merit of using the insert() method).


# to calculate the sum of all the values stored in the my_list list.
# You need a variable whose sum will be stored and initially assigned a value of 0 ‒ its name will be total. (Note: we're not going to name it sum as Python uses the same name for one of its built-in functions: sum(). Using the same name would generally be considered bad practice.) Then you add to it all the elements of the list using the for loop. Take a look at the snippet in the editor.

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)  # output: 27


# alternatively
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)  # output: 27

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)  # output: [5, 3, 8, 1, 10]


length = [3, 5, 6,8,9]
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

# step 1: create an empty list named beatles;
# step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# step 5: use the insert() method to add Ringo Starr to the beginning of the list.

# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
user1 = input("enter another name: ")
user2 = input("enter another name: ")
users = []
users.append(user1)
users.append(user2)
for name in users:
    beatles.append(name)
print("Step 3:", beatles)


# step 4
del beatles[4]
del beatles[3]
print("Step 4:", beatles)

# step 5
beatles.insert(3, "Ringo Starr")
print("Step 5:", beatles)

# testing list legth
print("The Fab", len(beatles))

my_list = [1, None, True, 'I am a string', 256, 0]
print(my_list[3])  # outputs: I am a string
print(my_list[-1])  # outputs: 0

my_list[1] = '?'
print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]

my_list.insert(0, "first")
my_list.append("last")
print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']

my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # outputs: [1, 2, 4]

del my_list  # deletes the whole list

# List elements and lists can be deleted, e.g.:
my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # outputs: [1, 2, 4]

del my_list  # deletes the whole list

lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)

# sorting
my_list = [8, 10, 6, 2, 4]  # list to sort

for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]:  # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # If we end up here, we have to swap the elements.
        print(my_list)
print(my_list)

my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            print(my_list)  # here is the steps of the sorting items

print(my_list)

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

# built in sort
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)  # [2, 4, 6, 8, 10]


lst = [5, 3, 1, 2, 4]
print(lst)

lst.sort()
print(lst)  # outputs: [1, 2, 3, 4, 5]

lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst)  # outputs: [4, 2, 1, 3, 5]

a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort()

print(lst)  # 1 2 3


a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort()

print(lst)  # [' ', 'C', 'B', 'A']


# the inner life of a list: equivalence action of python list
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2) # 2


list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)   # 1 : the slice[:] makes list_2 to copy only the content not list_1 as in memory location

# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)  # 1

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)  # 8, 6

# my_list[start:end]

# start is the index of the first element included in the slice;
# end is the index of the first element not included in the slice.
# This is how negative indices work with the slice:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list) # 8, 6, 4

# finding the largest number

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest) # 17 | instead of using max() function to check for the largest numbber

# alternatively
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)

# Now let's find the location of a given element inside a list:
# to check for which index an element belong to in a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i) # Element found at index 4
else:
    print("absent")


# to check for largest number
my_list = [17, 3, 11, 5, 1, 9, 60, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print("the largest number is ", largest)  # largest number is 60

print("""object and value| two object referencing single value""")
vehicles_one = ['car', 'bicycle', 'motor']
print(vehicles_one) # outputs: ['car', 'bicycle', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0] # deletes 'car'
print(vehicles_two) # outputs: ['bicycle', 'motor']

# 2. If you want to copy a list or part of the list, you can do it by performing slicing:
colors = ['red', 'green', 'orange']

copy_whole_colors = colors[:]  # copy the entire list
copy_part_colors = colors[0:2]  # copy part of the list

# 3. You can use negative indices to perform slices, too. For example:
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']

# 4. The start and end parameters are optional when performing a slice: list[start:end], e.g.:
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]

print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]

# You can delete slices using the del instruction:
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # outputs: [3, 4, 5]

del my_list[:]
print(my_list)  # deletes the list content, outputs: []

# 6. You can test if some items exist in a list or not using the keywords in and not in, e.g.:
my_list = ["A", "B", 1, 2]

print("A" in my_list)  # outputs: True
print("C" not in my_list)  # outputs: True
print(2 not in my_list)  # outputs: False

# what is the output of this code
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)  # output| C

# what is the  output of the ff snippet
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)  # output | ["B", "C"]

# what is the  output of the ff snippet
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3) # output  | []

# Question 4: What is the output of the following snippet?
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3) # output | ["A", "B", "C"]

# Question 5: Insert in or not in instead of ??? so that the code outputs the expected result.
my_list = [1, 2, "in", True, "ABC"]

print(1 in my_list)  # outputs True
print("A" not in my_list)  # outputs True
print(3 not in my_list)  # outputs True
print(False in my_list)  # outputs False
# my_list = [1, 2, "in", True, "ABC"] print(1 in my_list) # outputs True print("A" not in my_list) # outputs True print(3 not in my_list) # outputs True print(False in my_list) # outputs False


# start is the index of the first element included in the slice;
# end is the index of the first element not included in the slice.

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)  # output | [8, 6, 4]  | index 1 "START" is included which is 8 | index -1 "END" is not included which is 2 the index stops at 2

# list comprehension
squares = [x ** 2 for x in range(10)]
twos = [2 ** i for i in range(8)]
odds = [x for x in range(20) if x % 2 != 0 ]

# if we want to create a list of lists representing the whole chessboard, it may be done in the following way:
board = []

for i in range(8):
    row = [8 * 8 for i in range(8)]
    board.append(row)

# alternatively
board = [[8 * 8 for i in range(8)] for j in range(8)]
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
print(ROOK)

board[4][2] = KNIGHT
print(KNIGHT)

board[3][4] = PAWN
print(PAWN)


print("""
Imagine that you're developing a piece of software for an automatic weather station. The device records the air temperature on an hourly basis and does it throughout the month. This gives you a total of 24 × 31 = 744 values. Let's try to design a list capable of storing all these results.

First, you have to decide which data type would be adequate for this application. In this case, a float would be best, since this thermometer is able to measure the temperature with an accuracy of 0.1 ℃.

Then you take an arbitrary decision that the rows will record the readings every hour on the hour (so the row will have 24 elements) and each of the rows will be assigned to one day of the month (let's assume that each month has 31 days, so you need 31 rows). Here's the appropriate pair of comprehensions (h is for hour, d for day):
""")

temps = [[0.0 for h in range(24)] for d in range(31)]

"""
The whole matrix is filled with zeros now. You can assume that it's updated automatically using special hardware agents. The thing you have to do is to wait for the matrix to be filled with measurements.
Now it's time to determine the monthly average noon temperature. Add up all 31 readings recorded at noon and divide the sum by 31. You can assume that the midnight temperature is stored first. Here's the relevant code:
"""
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)

print("""
Note: the day variable used by the for loop is not a scalar ‒ each pass through the temps matrix assigns it with the subsequent rows of the matrix; hence, it's a list. It has to be indexed with 11 to access the temperature value measured at noon.
""")

# Now find the highest temperature during the whole month
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

"""the day variable iterates through all the rows in the temps matrix;
the temp variable iterates through all the measurements taken in one day."""

# Now count the days when the temperature at noon was at least 20 ℃:
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "days were hot.")

print("""
Imagine a hotel. It's a huge hotel consisting of three buildings, 15 floors each. There are 20 rooms on each floor. For this, you need an array which can collect and process information on the occupied/free rooms.

First step ‒ the type of the array's elements. In this case, a Boolean value (True/False) would fit.

Step two ‒ calm analysis of the situation. Summarize the available information: three buildings, 15 floors, 20 rooms.

Now you can create the array:
""")


rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

print("""
The first index (0 through 2) selects one of the buildings; the second (0 through 14) selects the floor, the third (0 through 19) selects the room number. All rooms are initially free.

Now you can book a room for two newlyweds: in the second building, on the tenth floor, room 14:
""")
rooms[1][9][13] = True

# and release the second room on the fifth floor located in the first building:
rooms[0][4][1] = False

# Check if there are any vacancies on the 15th floor of the third building:
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1


print("""
The vacancy variable contains 0 if all the rooms are occupied, or the number of available rooms otherwise.

Congratulations! You've made it to the end of the module. Keep up the good work!
""")

cubed = [num ** 3 for num in range(5)]
print(cubed)  # outputs: [0, 1, 8, 27, 64]

# A four-column/four-row table ‒ a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'

# Cube - a three-dimensional array (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'

# functions
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)

def introduction(first_name, last_name="Smith"):
     print("Hello, my name is", first_name, last_name)

introduction("James", "Doe")

introduction("Henry")

introduction(first_name="William")

# This makes the following invocation absolutely valid:
def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction()
introduction(last_name="Hopkins")

def hi(name):
    print("Hi,", name)

hi("Greg")

# alternatively
def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)

hi_all("Sebastian", "Konrad")

def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")
address(s, c, p_c)

# Ex. 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # outputs: 3
subtra(2, 5)    # outputs: -3


# Ex. 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # outputs: 3
subtra(b=2, a=5)    # outputs: 3

# Ex. 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(5, 2)    # outputs: 3

def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(a=5, 2)    # Syntax Error

def name(first_name, last_name="Smith"):
    print(first_name, last_name)

name("Andy")    # outputs: Andy Smith
name("Betty", "Johnson")    # outputs: Betty Johnson (the keyword argument replaced by "Johnson")

def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro(b="Sean Connery") # output:  My name is Sean Connery. James Bond.

def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")

intro("Susan") # Bond. Susan.

def add_numbers(a, b=2, c):
    print(a + b + c)

add_numbers(a=1, c=3)  # SyntaxError: non-default argument follows default argument


print("""function with return value""")
def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return  # return without an expression

    print("Happy New Year!")
happy_new_year()
print("""output:
Three...
Two...
One...
Happy New Year!""")

happy_new_year(False)
print("""output:
Three...
Two...
One...""")


def boring_function():
    return 123


x = boring_function()

print("The boring_function has returned its result. It's:", x)


def boring_function():
    print("'Boredom Mode' ON.")
    return 123


print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")


# None type
def strange_function(n):
    if (n % 2 == 0):
        return "True"


x = strange_function(8)
print(x)  # True
x = strange_function(8)
print(x)  # None


def strange_function(n):
    if (n % 2 == 0):
        return True


print(strange_function(2))  # True
print(strange_function(1))  # None


# may a list be sent to a function as an argument?
# So, if you pass a list to a function, the function has to handle it like a list.
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s


print(list_sum([5, 4, 3]))  # 12
print(list_sum(range(5)))  # 10


# may a list be a function result?
def strange_list_fun(n):
    strange_list = []

    for i in range(0, n):
        strange_list.insert(0, i)

    return strange_list


print(strange_list_fun(5))




