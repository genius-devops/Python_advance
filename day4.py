import random
from func_module import p   # the p is the function of from func_module
ran_int = random.randint(1, 100)
print(ran_int)

print(p()) # this func is fetch from func_module file

ran_f = random.random() * 2
print(ran_f * 5)

love_score = random.randint(1, 100)
print(f"your love score is {love_score}")

nig_state = ["Abia", "Adamawa", "Benue", "Akwa Ibom", "Kano", "Kaduna", "Katsina"  ]
num = len(nig_state)
print(num)

usa = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
num2 = len(usa)
print(num2)
print(usa[30])


dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

for state in usa:
    print(state)

