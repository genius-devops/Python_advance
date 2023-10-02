print("welcome to roller coaster!")
height = int(input("what is your height in cm? "))
bill = 0

if height > 120:
    print("you can ride the roller coaster!")
else:
    print("sorry, you may have to grow taller before you can ride")

# nested if else statement
# when age is < 12 (pay $5.) when age is bwt 12 - 18 (pay $7) and > 18 (pay $12)
if height >= 120:
    print("you can ride the roller coaster!")

    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("sorry, you have to grow taller before you can ride!")


# multiple if statement
if height >= 120:
    print("you can ride the roller coaster!")

    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("sorry, you have to grow taller before you can ride!")
