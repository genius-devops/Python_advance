import math
# typecasting
print("Hello!"[2::3]);

num_char = len(input("what is your name?\n"));

# fstring
print(f"your name has {num_char} number of character")

# typecasting
num = str(num_char)

print("your name has " + num + " number of character")

int_a = 1234
print(int_a)

float_b = float(int_a)
print(float_b)

# alternatively
a = 1234
b = float(123)
print(b)
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight)/float(height) ** 2
print(f"your height is {height}m and weight is {weight}kg bmi value is {bmi}")

# converting into int
bmi_as_int = int(bmi)
print(f"your bmi value in int format is {bmi_as_int}")
age = input("what is your current age?\n")
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = f"you have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left."
print(message)

# project tip calculator
print("welcome to tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give?  10, 12, or 15?"))
people = int(input("how many people to split the bill"))
bill_with_tip = tip / 100 * bill + bill
bill_with_tip2 = bill * int((1 + tip / 100))  # another method
bill_with_tip3 = bill * (1 + tip // 100)  # alternatively
# another step
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)  # this is another method instead of using round() function
print(f"Each person should pay: ${final_amount}")
print(bill_with_tip)
print(bill_with_tip2)
print(bill_with_tip3)