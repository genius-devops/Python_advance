import math
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
