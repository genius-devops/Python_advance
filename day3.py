# printing multiple argument from print function
myName = input("What's your name? ")
myLunch = input("What are you having for lunch? ")
print(myName, "is going to be chowing down on", myLunch, "very soon!")
number = input("Give me a number: ")
group = input("Give me a collective noun for a group of things: ")
thing = input("Give me the name of a weird or wacky thing: ")
print("No I don't think that", number, "is a", group, "of", thing,". That's just odd.")

# debugging | fixing some errors relate to this code
yourName = input("Name: ")
whatYear = input("What year is it?: ")
print("yourName, thinks it is, whatYear")
print("=== Your Song Generator ===")
print("""You'll be asked a bunch of questions
then we'll make you up an amazing
song, totally copyright free 😭""")
print()

# debugging | fixing some errors related to this code
person = input("Name a person famous for something good: ")
thing = input("Name a thing they did: ")
place = input("Name a place you like: ")
rhyme = input("Give me a verb that rhymes with your person's name: ")
print()
print("There was a person called", person)
print("Who did something cool like", thing, "at the wonderful", place, "where you'll find me", rhyme)
print()

# 👉 Day 3 Challenge | variable manipulation
food = input("Name a type of food: ")
plant = input("Name a plant: ")
cookingType = input("What is a way to cook something?")
burntFood = input("How do you describe burnt food?")
householdItem = input("Name something in your house: ")

print()
print("Tonight's dinner:")

print("For dinner you should make", cookingType, food, "with", burntFood, plant, "on a plate of", householdItem)print()

# coaster  roller project
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
