# logical operator
height = int(input("what is your height? "))

bill = 0

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
    elif age >= 45 & age <= 55:
        print("Everything is going to be ok! have a free ride with us")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("sorry, you have to grow taller before you can ride!")
