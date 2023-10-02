# check for leap year!
print("check for leap year!")
year = int(input("which year you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("NOT leap year")
    else:
        print("NOT leap year")
else:
    print("NOT leap year")