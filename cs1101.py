# # Discussion Assignment
# # Welcome to Unit 3 Discussion Forum. 

# # Describe the difference between a chained conditional and a nested conditional. Give your own example of each. Do not copy examples from the textbook.

# >>> # chain conditional
# >>> 
# >>> name = 'salma'
# >>> if name == 'adamu':
# ...     print('he is a male')
# ... elif name == 'labaran':
# ...     print('he is our dad')
# ... elif name == 'afra':
# ...     print('she is our young baby')
# ... else:
# ...     print(f"the name is {name}")
# ...
# output: 
# the name is salma
# >>> 

# nested conditional
# >>> age = 18
# >>> if age == age:
# ...     print('he can drink')
# ... else:
# ...     if age < age:
# ...             print('he cannot drink!')
# ...     else:
# ...             print('we dont want trouble!, send him back')
# ...
# he can drink
# >>>


# # Deeply nested conditionals can become difficult to read. Describe a strategy for avoiding nested conditionals. Give your own example of a nested conditional that can be modified to become a single conditional, and show the equivalent single conditional. Do not copy the example from the textbook.

# name1 = 'adamu'
# name2 = 'labaran'
# name3 = 'salma'
# name4 = 'usman'

# if name1 == name2: # not True 
#     print(name1) 
# else:
#     if name1 == name3:  # not True
#         print(name2)
#     else:
#         if name1 == name4: # not True
#             print(name3)
#         else:
#             if name3 == name1:  # not True
#                print(name4)
#             else:
#                 print("options not true")
                
# if name1 == name2:
#     print(name1)
# elif name1 == name3:
#     print(name2)
# elif name1 == name4:
#     print(name3)
# elif name3 == name1:
#     print(name4)
# else:
#     print("options are not true")
             

# # Write a new recursive function countup that expects a negative argument and counts “up” from that number. Output from running the function should look something like this:

# # >>> countup(-3)
# # -3
# # -2
# # -1
# # Blastoff!

# # Write a Python program that gets a number using keyboard input. (Remember to use input for Python 3 but raw_input for Python 2.)

# # If the number is positive, the program should call countdown. If the number is negative, the program should call countup. Choose for yourself which function to call (countdown or countup) for input of zero.

# def countdown(n):
#     if n <= 0:
#         print("Blastoff!")
#     else:
#         print(n)
#         countdown(n-1)

# countdown(9)

# def countup(n):
#     if n >= 0:
#         print("Blasstoff!")
#     else:
#         print(n)
#         countup(n+1)
        
# countup(-9)

# def coutntuodown(n):
#     if n <= 0 or n >= 0:
#         countdown(n)
#         countup(n)
#     else:
#         countdown(n)
#         countup(n)
# coutntuodown(0)



# def countup(n):
#     if n >= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countup(n+1)
        
# countup(-3)

# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)
        
# countdown(3)

# def countup_or_countdown(n):
#     if n >= 0 or n <= 0:
#         countup(n)
#         countdown(n)
#     else:
#         countup(n+1)
#         countdown(n-1)
  

# countup_or_countdown(6) 
# countup_or_countdown(-6) 
# countup_or_countdown(0) 

# x = 5
# y = 4

# def or_logic():
#     if x > y or x < y:
#         print("since one of the if condition is true\nI'll first execute")
#     elif x < y or x > y:
#         print("since one of the if condition is true\nI'll first execute")
#     else:
#         print("i wouldn't execute! ")
        
# or_logic()

# def and_logic():
#     if x > y and x < y:
#         print("both condition must be true! or else will print")
#     elif x < y and x > y:
#          print("both condition must be true! or else will print")
#     else:
#         print("I'll execute because one of the condition above is not true!")
        
# and_logic()


# import math

# def area(radius):
#     a = math.pi * radius**2
#     return a
# num = input('value:')
# a = int(num)
# print(area(a))
# def area(radius):
#     return math.pi * radius**2



# def absolute_value(x):
#     if x < 0:
#         return -x
#     else:
#         return x
    
# print(absolute_value(9))

# def countdown(n):
#     if n <= 0:
#         print("Blastoff!")
#     else:
#         print(n)
#         countdown(n-1)

# # countdown(9)

# def countup(n):
#     if n >= 0:
#         print("Blasstoff!")
#     else:
#         print(n)
#         countup(n+1)
        
# # countup(-9)

# def coutntuodown(n):
#     if n <= 0 or n >= 0:
#         countdown(n)
#         countup(n)
#     else:
#         countdown(n)
#         countup(n)
# coutntuodown(7)


# # correct solution
# def countup(n):
#     if n >= 0:
#         print("Blasstoff!")
#     else:
#         print(n)
#         countup(n+1)
        
# countup(-9)


# def countdown(n):
#     if n <= 0:
#         print("Blastoff!")
#     else:
#         print(n)
#         countdown(n-1)
# countdown(9)

# def coutup_or_countdown(n):
#     # n = int(input('enter a value:\n'))
#     if n <= 0:
#         countup(n)
#         countdown(n)
#     elif n >= 0:
#         countdown(n)
#         countup(n)
        
# coutup_or_countdown(0)


# x = "There are %d types of people." % 10
# binary = "binary"
# do_not = "don't"
# y = "Those who know %s and those who %s." % (binary, do_not)

# print x
# print y

# print "I said: %r." % x
# print "I also said: '%s'." % y

# hilarious = False
# joke_evaluation = "Isn't that joke so funny?! %r"

# print joke_evaluation % hilarious

# w = "This is the left side of..."
# e = "a string with a right side."

# print w + e

# def main():
#     print("\n" + "-" * 40)
#     print("\nWelcome to the Letter Grade Program")

#     grade = int(input("Enter a grade: "))
#     letter = ""

#     if grade > 89:
#         letter += "A"
#     elif grade > 79:
#         letter += "B"
#     elif grade > 69:
#         letter += "C"
#     else:
#         letter += "F"

#     print("\nThe grade is " + str(grade) + ".")
#     print("The letter grade is " + letter + ".\n")
#     print("-" * 40)

# main()

# def main():
#     print("\n" + "-" * 60)
#     print("Divisibility By Six Program")
#     print("A number is divisible by 6 is it is divisible by 2 and 3.")

#     number = int(input("\nEnter a number: "))

#     if number % 2 == 0 or number % 3 == 0:
#         if number % 6 == 0:
#             print("\nThe number " + str(number) + " is divisible by 2,")
#             print("divisible by 3, and divisible by 6. \n")
#         else:
#             for factor in range(2, 4):
#                 if number % factor == 0:
#                     print("\nThe number " + str(number) + " is only divisible by " + str(factor) + ".")
#                 else:
#                     print("\nThe number " + str(number) + " is not divisible by 6.")

#     print("-" * 60 + "\n")

# main()


# def factorial(n):
#     space = ' ' * (4 * n)
#     print(space, 'factorial', n)
#     if n == 0:
#         print(space, 'returning 1')
#         return 1
#     else:
#         recurse = factorial(n-1)
#         result = n * recurse
#         print(space, 'returning', result)
#         return result
# factorial(4)


# import math
# def sphere(r):   
#     mass = 95
#     volume = 4/3 * math.pi * r ** 3
#     surface_area = 4 * math.pi * r ** 2
#     density = mass / volume
#     print(volume)
#     print(surface_area)
#     print(density)
#     return volume

# print(sphere(4))
# print(sphere(7))
# sphere(8)


# import math
# def sphere(r):   
#     mass = 95
#     volume = 4/3 * math.pi * r ** 3
#     surface_area = 4 * math.pi * r ** 2
#     density = mass / volume
#     print(volume)
#     print(surface_area)
#     print(density)
#     return r

# sphere(8)
# sphere(4)
# sphere(-3)


# def factorial(n):
#     space = ' ' * (4 * n)
#     print(space, 'factorial', n)
#     if n == 0:
#         print(space, 'returning 1')
#         return 1
#     else:
#         recurse = factorial(n-1)
#         result = n * recurse
#         print(space, 'returning', result)
#         return result
# factorial(4)

# def factorial(n):
#     if not isinstance(n, int):
#         print('Factorial is only defined for integers.')
#         return None
#     elif n < 0:
#         print('Factorial is not defined for negative integers.')
#         return None
#     elif n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial('fred'))

# print(factorial(-2))


# import math

# # step 1 defining hypodenus

# #mathematically, hypotanus (c) is the sum of square of base (b) and height(a) 
# # By pythagorean theorem: c**2 = a**2 + b**2
# # c = math.sqrt(a**2 + b**2) 

# def hypotenus(a, b):
#     return 0.0              #The  return value is the distance represented by a floating-point value.(Downey, 2015)

# hypotenus(6, 8)            # calling the function to check if it is syntetically correct



# # step 2 by computing the sum of square of the base (b) and height (a)


# def hypotenus(a, b):
#     height = a ** 2
#     base = b ** 2
#     c = height + base
#     print("the value of height is: ", height)
#     print("the value of base is: ", base)
#     print("The c variable is the corresponding hypotenus")
#     return 0.0


# hypotenus(6, 8)            # to check if the funxction is bug free



# # step 3 by using math.sqrt() function to compute and return the lenght

# def hypotenus(a, b):
#     c = (a**2) + (b**2)
#     length = math.sqrt(c)
#     return length

# print("the hypotenuse of a right triangle is equal to:", hypotenus(6, 8))

# print("\nThe output of two additional calls to hypotenuse with different arguments.\n")

# print("the hypotenuse of a right triangle is equal to:", hypotenus(5, 6))

# print("\nthe hypotenuse of a right triangle is equal to:", hypotenus(3, 2))



# # part 2

# # definining sphere: the surface of sphere is perfectly ROUND.
# # where Volume = (4/3)*math.pi*r**3, Sufacwe area = 4**pi*r**2
# # finding the 
# # 1. volume of the spere, 
# # 2. the surface area and 
# # 3. the density
# # 4. a sphere of radius(r) 4cm is of mass 95g 

# # step 1: defining the sphere

# def sphere(r):
#     return 0.0

# sphere(4)         # verifying the flow of execussion


# # step 2
# # computing and returning the value for Volume

# def sphere(r):
#     volume = 4/3 * math.pi * r ** 3
#     print(f"\nThe Volume of a sphere = {volume}cm3")
#     return volume

# sphere(4)       


# # step 3
# # computing and returning the value for Surface area
# def sphere(r):
#     surface_area = 4 * math.pi * r ** 2
#     print(f"\nthe Surface area =  {surface_area}cm2")
#     return surface_area

# sphere(4)

# # step 4 
# # computing and returning the value for density
# #the mass of the sphere in gram(g)

# def sphere(r):   
#     mass = 95
#     volume = 4/3 * math.pi * r ** 3
#     density = mass / volume
#     print(f"\nthe density of the sphere = {density}gcm-3")
#     return density

# sphere(4)
# sphere(7)
# sphere(1)


# import math

# e = math.exp(1.0)
# height = radius * math.sin(radians)

# def area(radius):
# a = math.pi * radius**2
# return a

# def area(radius):
# return math.pi * radius**2


# def absolute_value(x):
# if x < 0:
# return -x
# else:
# return x

# def absolute_value(x):
# if x < 0:
# return -x
# if x > 0:
# return x

# # As an exercise, write a compare function takes two values, x and y, and returns 1 if x > y,
# # 0 if x == y, and -1 if x < y


# def distance(x1, y1, x2, y2):
# return 0.0

# distance(1, 2, 4, 6)


# def distance(x1, y1, x2, y2):
# dx = x2 - x1
# dy = y2 - y1
# print('dx is', dx)
# print('dy is', dy)
# return 0.0

# def distance(x1, y1, x2, y2):
# dx = x2 - x1
# dy = y2 - y1
# dsquared = dx**2 + dy**2
# print('dsquared is: ', dsquared)
# return 0.0

# def distance(x1, y1, x2, y2):
# dx = x2 - x1
# dy = y2 - y1
# dsquared = dx**2 + dy**2
# result = math.sqrt(dsquared)
# return result

# # As an exercise, use incremental development to write a function called hypotenuse that
# # returns the length of the hypotenuse of a right triangle given the lengths of the other two
# # legs as arguments. Record each stage of the development process as you go.

# import math

# def area(radius):
#     a = math.pi * radius**2
#     return a

# def area(radius):
#     return math.pi * radius**2

# def absolute_value(x):
#     if x < 0:
#         return -x
#     else:
#         return x
    
# print(absolute_value(0))

# # As an exercise, write a compare function takes two values, x and y, and returns 1 if x > y,
# # 0 if x == y, and -1 if x < y.


# # incremental development


# # suppose you want to find the distance between two points, given by the
# # coordinates (x1, y1) and (x2, y2). By the Pythagorean theorem, the distance is:

# # In this case, the inputs are two points, which you can represent using four numbers. The return value is the distance represented by a floating-point value. Immediately you can write an outline of the function:


# def distance(x1, y1, x2, y2):
#     return 0.0

# distance(1, 2, 4, 6)


# # step 2 find the difference b/w x2-x1 & y2-y1
# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     print('dx is', dx)
#     print('dy is', dy)
#     return 0.0


# distance(1, 2, 4, 6)

# # step 3 compute the sum of squares of dx and dy

# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquared = dx**2 + dy**2
#     print('dsquared is: ', dsquared)
#     return 0.0

# distance(1, 2, 4, 6)


# # step 3 use math.sqrt function to compute and return the result:

# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquared = dx**2 + dy**2
#     result = math.sqrt(dsquared)
#     return result


# print(distance(1, 2, 4, 6))


# #  a function that takes two points, the center of the circle and a point on the perimeter, and computes the area of the circleAssume that the center point is stored in the variables xc and yc, and the perimeter point is in xp and yp. The first step is to find the radius of the circle, which is the distance between the two points.  We just wrote a function, distance, that does that: radius = distance(xc, yc, xp, yp)


# radius = distance(xc, yc, xp, yp)

# result = area(radius)

# def circle_area(xc, yc, xp, yp):
#     radius = distance(xc, yc, xp, yp)
#     result = area(radius)
#     return result


# def circle_area(xc, yc, xp, yp):
#     return area(distance(xc, yc, xp, yp))


# def is_divisible(x, y):
#     if x % y == 0:
#     return True
#     else:
#     return False


# is_divisible(6, 4)
# is_divisible(6, 3)


# def is_divisible(x, y):
# return x % y == 0
# Boolean functions are often used in conditional statements:
# if is_divisible(x, y):
# print('x is divisible by y')
# It might be tempting to write something like:
# if is_divisible(x, y) == True:
# print('x is divisible by y')
# But the extra comparison is unnecessary.
# As an exercise, write a function is_between(x, y, z) that returns True if x  y  z or
# False otherwise.


# def factorial(n):
# if n == 0:
# return 1



# def factorial(n):
# if n == 0:
# return 1
# else:
# recurse = factorial(n-1)
# result = n * recurse
# return result

# # fibonacci

# def fibonacci(n):
# if n == 0:
# return 0
# elif n == 1:
# return 1
# else:
# return fibonacci(n-1) + fibonacci(n-2)


# def factorial(n):
# if not isinstance(n, int):
# print('Factorial is only defined for integers.')
# return None
# elif n < 0:
# print('Factorial is not defined for negative integers.')
# return None
# elif n == 0:
# return 1
# else:
# return n * factorial(n-1)

# print(factorial('fred'))

# print(factorial(-2))

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')





# # part 2
# # example 1

# a = "adamu labaran computer science student at uopeople"
# print(a)

# print(len(a))

# # the inbuilt function len() was used to check the length of character in variable "a"
# # output: 50

# print(a[:])

# # a[:] print the entire character in "a" variable
# #output: 'adamu labaran computer science student at uopeople'

# print(a[0:0])

# # return empty string 
# # output: ' '


# print(a[0])

# # this print first character in the string
# # output: 'a'

# print(a[49])

# # last character in the string
# # output:  'e'

# print(a[14:22])

# # this print 14 - 22 character in the string
# # 'computer'


# print(a[12:22:5])

# # return every 5th  character from 12 to 22
# # output: 'np'

# print(a[12:50:5])

# # return every 5th  character from 12 to 50
# # output: 'np nttup'

# print(a[0:50:5])

# # return every 5th  character from 0 to 50
# # output: 'a roei ete'

# print(a[0:50:3])

# # return every 3th  character from 0 to 50
# # output: 'a roei ete'

# # example 2

# b = 'welcome to python course'

# print(b[0:7])

# # return the first 7th character 
# # output: 'welcome'

# print(b[7:10])

# # Return from 7th to 10 character
# # output: ' to'

# print(b[10:17])

# # return from 10th to 17th character
# # output: ' python'

# print(b[17:24])

# # return 17th to 24th character
# # output: ' course'

# print(b[:24])

# # return everything
# # output:'welcome to python course'

# print(b[24:])

# # return empty string
# # output: ''


# print(b[10:24])

# # return 10th to 24 character
# # output: ' python course'

# # example 3
# c = 'python a programmin foundamental course at uopeople'


# print(c[ : -8])

# # The -8 corresponding to [n:-m] where the negative m-eth (-m) value return anticlockwise. in this case it return the n-eth value and delete the last value. 
# # output: 'python a programmin foundamental course at '

# print(c[-8:])

# # at the other hand the [-n:m] where the -n-eth count from last and the 8th most value which "uopeople"
# # output: 'uopeople'

# print(c[-19:])

# # -n-eth term return last most value
# # output: ' course at uopeople'

# print(c[:-19])
# # -m-eth return first value cut off last value 
# # output: 'python a programmin foundamental'


# epsilon = 0.00000000001

# def my_sqrt(a):
#     x =  a / 2
#     while True:
#         y = (x + a / x) / 2
#         if abs(y - x) < epsilon:
#             print(y)
#             return y
#             break
#         x = y
# my_sqrt(9)


# def right_digit(n):
#     trunc = f'{n:.11f}'
#     dig = trunc[len(trunc)-1]
#     print(dig)
#     return dig
# right_digit(9)


# def test_sqrt(n):
#     print('a', ' '*1, 'mysqrt(a)', ' '*3, 'math.sqrt(a)', 'diff')
#     print('_', ' '*1, '_'*9, ' '*3, '_'*12, ' ' + '_'*4)
    
#     for i in range(9):
#         x = i + 1
        
#         print(f'{x:0.1f}', end=' ')
        
#         if my_sqrt(x) - int(my_sqrt(x)) < 0.001:
#             y = 1
#         elif right_digit(my_sqrt(x)) == '0':
#             y = 0
#         else:
#             y = 11
            
#         print(f'{my_sqrt(x): < 13.{y}}', end=' ')
#         print(f'{my_sqrt(x): < 13.{y}}', end=' ')
        
#         diff = math.sqrt(x) - my_sqrt(x)
#         print(f'{diff:.12g}')
        
        
# test_sqrt(9)

# import math
# a  = 9
# x = 2
# def mysqrt(a):
#     x = a / 2
#     while True:
#         y = (x + a / x) / 2
#         if x - y < 0.00001:
#             break
#         x = y
#     print(y)
#     return y

# mysqrt(9)


# def diff(a):
#     d = mysqrt(a) - math.sqrt(a)
#     print(d)

# diff(9)


# def test_sqrt(a):
#     print(
#         'a', ' '*2,
#         'mysqrt(a)', ' '*11,
#         'math.sqrt(a)', ' '*8,
#         'diff'
#     )
#     while a > 1:
#         a = a-1
#         len_a = 3 - len(str(a))
#         len_my = 20 - len(str(mysqrt(a)))
#         len_ma = 20 - len(str(math.sqrt(a)))
#         print(
#             a, ' '* len_a,
#             mysqrt(a), ' '* len_my,
#             math.sqrt(a), ' '*len_ma,
#             diff(a)
#         )
#     return

# test_sqrt(10)


# a = 9
# x = 2
# while True:
#     print(x)
#     y = (x + a/x) / 2.0
#     if y == x:
#             break
#     x = y


# def my_sqrt(a):
#     x = a / 2
#     while True:
#         print(x)
#         y = (x + a / x) / 2.0
#         if y == x:
#             break
#         x = y
        
# my_sqrt(9)


# def find(word, letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1

# print(find("adamslabaran","a"))

# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

# word = 'banana'
# print(word.upper())

# new_word = word.upper()
# print(new_word)

# index = word.find('a')
# print(index)

# print(word.find('na', 3))

# def in_both(word1, word2):
#     for letter in word1:
#         if letter in word2:
#             print(letter)
            
            
# in_both('adams', 'labaran')
# in_both('apples', 'oranges')


# if word < 'banana':
#     print('Your word, ' + word + ', comes before banana.')
# elif word > 'banana':
#     print('Your word, ' + word + ', comes after banana.')
# else:
#     print('All right, bananas.')
    
    
# # def is_reverse(word1, word2):
# # if len(word1) != len(word2):
# # return False
# # i = 0
# # j = len(word2)
# # while j > 0:
# # if word1[i] != word2[j]:
# # return False
# # i = i+1
# # j = j-1
# # return 

# # Discussion Assignment
# # Welcome to Unit 3 Discussion Forum. 

# # Describe the difference between a chained conditional and a nested conditional. Give your own example of each. Do not copy examples from the textbook.

# >>> # chain conditional
# >>> 
# >>> name = 'salma'
# >>> if name == 'adamu':
# ...     print('he is a male')
# ... elif name == 'labaran':
# ...     print('he is our dad')
# ... elif name == 'afra':
# ...     print('she is our young baby')
# ... else:
# ...     print(f"the name is {name}")
# ...
# output: 
# the name is salma
# >>> 

# nested conditional
# >>> age = 18
# >>> if age == age:
# ...     print('he can drink')
# ... else:
# ...     if age < age:
# ...             print('he cannot drink!')
# ...     else:
# ...             print('we dont want trouble!, send him back')
# ...
# he can drink
# >>>


# # Deeply nested conditionals can become difficult to read. Describe a strategy for avoiding nested conditionals. Give your own example of a nested conditional that can be modified to become a single conditional, and show the equivalent single conditional. Do not copy the example from the textbook.

# name1 = 'adamu'
# name2 = 'labaran'
# name3 = 'salma'
# name4 = 'usman'

# if name1 == name2: # not True 
#     print(name1) 
# else:
#     if name1 == name3:  # not True
#         print(name2)
#     else:
#         if name1 == name4: # not True
#             print(name3)
#         else:
#             if name3 == name1:  # not True
#                print(name4)
#             else:
#                 print("options not true")
                
# if name1 == name2:
#     print(name1)
# elif name1 == name3:
#     print(name2)
# elif name1 == name4:
#     print(name3)
# elif name3 == name1:
#     print(name4)
# else:
#     print("options are not true")
             

# # Write a new recursive function countup that expects a negative argument and counts “up” from that number. Output from running the function should look something like this:

# # >>> countup(-3)
# # -3
# # -2
# # -1
# # Blastoff!

# # Write a Python program that gets a number using keyboard input. (Remember to use input for Python 3 but raw_input for Python 2.)

# # If the number is positive, the program should call countdown. If the number is negative, the program should call countup. Choose for yourself which function to call (countdown or countup) for input of zero.

# def countdown(n):
#     if n <= 0:
#         print("Blastoff!")
#     else:
#         print(n)
#         countdown(n-1)

# countdown(9)

# def countup(n):
#     if n >= 0:
#         print("Blasstoff!")
#     else:
#         print(n)
#         countup(n+1)
        
# countup(-9)

# def coutntuodown(n):
#     if n <= 0 or n >= 0:
#         countdown(n)
#         countup(n)
#     else:
#         countdown(n)
#         countup(n)
# coutntuodown(0)



# def countup(n):
#     if n >= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countup(n+1)
        
# countup(-3)

# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)
        
# countdown(3)

# def countup_or_countdown(n):
#     if n >= 0 or n <= 0:
#         countup(n)
#         countdown(n)
#     else:
#         countup(n+1)
#         countdown(n-1)
  

# countup_or_countdown(6) 
# countup_or_countdown(-6) 
# countup_or_countdown(0) 

# x = 5
# y = 4

# def or_logic():
#     if x > y or x < y:
#         print("since one of the if condition is true\nI'll first execute")
#     elif x < y or x > y:
#         print("since one of the if condition is true\nI'll first execute")
#     else:
#         print("i wouldn't execute! ")
        
# or_logic()

# def and_logic():
#     if x > y and x < y:
#         print("both condition must be true! or else will print")
#     elif x < y and x > y:
#          print("both condition must be true! or else will print")
#     else:
#         print("I'll execute because one of the condition above is not true!")
        
# and_logic()


# import math

# def area(radius):
#     a = math.pi * radius**2
#     return a
# num = input('value:')
# a = int(num)
# print(area(a))
# def area(radius):
#     return math.pi * radius**2



# def absolute_value(x):
#     if x < 0:
#         return -x
#     else:
#         return x
    
# print(absolute_value(9))

# def countdown(n):
#     if n <= 0:
#         print("Blastoff!")
#     else:
#         print(n)
#         countdown(n-1)

# # countdown(9)

# def countup(n):
#     if n >= 0:
#         print("Blasstoff!")
#     else:
#         print(n)
#         countup(n+1)
        
# # countup(-9)

# def coutntuodown(n):
#     if n <= 0 or n >= 0:
#         countdown(n)
#         countup(n)
#     else:
#         countdown(n)
#         countup(n)
# coutntuodown(7)


# # correct solution
# def countup(n):
#     if n >= 0:
#         print("Blasstoff!")
#     else:
#         print(n)
#         countup(n+1)
        
# countup(-9)


# def countdown(n):
#     if n <= 0:
#         print("Blastoff!")
#     else:
#         print(n)
#         countdown(n-1)
# countdown(9)

# def coutup_or_countdown(n):
#     # n = int(input('enter a value:\n'))
#     if n <= 0:
#         countup(n)
#         countdown(n)
#     elif n >= 0:
#         countdown(n)
#         countup(n)
        
# coutup_or_countdown(0)


# x = "There are %d types of people." % 10
# binary = "binary"
# do_not = "don't"
# y = "Those who know %s and those who %s." % (binary, do_not)

# print x
# print y

# print "I said: %r." % x
# print "I also said: '%s'." % y

# hilarious = False
# joke_evaluation = "Isn't that joke so funny?! %r"

# print joke_evaluation % hilarious

# w = "This is the left side of..."
# e = "a string with a right side."

# print w + e

# def main():
#     print("\n" + "-" * 40)
#     print("\nWelcome to the Letter Grade Program")

#     grade = int(input("Enter a grade: "))
#     letter = ""

#     if grade > 89:
#         letter += "A"
#     elif grade > 79:
#         letter += "B"
#     elif grade > 69:
#         letter += "C"
#     else:
#         letter += "F"

#     print("\nThe grade is " + str(grade) + ".")
#     print("The letter grade is " + letter + ".\n")
#     print("-" * 40)

# main()

# def main():
#     print("\n" + "-" * 60)
#     print("Divisibility By Six Program")
#     print("A number is divisible by 6 is it is divisible by 2 and 3.")

#     number = int(input("\nEnter a number: "))

#     if number % 2 == 0 or number % 3 == 0:
#         if number % 6 == 0:
#             print("\nThe number " + str(number) + " is divisible by 2,")
#             print("divisible by 3, and divisible by 6. \n")
#         else:
#             for factor in range(2, 4):
#                 if number % factor == 0:
#                     print("\nThe number " + str(number) + " is only divisible by " + str(factor) + ".")
#                 else:
#                     print("\nThe number " + str(number) + " is not divisible by 6.")

#     print("-" * 60 + "\n")

# main()


# def factorial(n):
#     space = ' ' * (4 * n)
#     print(space, 'factorial', n)
#     if n == 0:
#         print(space, 'returning 1')
#         return 1
#     else:
#         recurse = factorial(n-1)
#         result = n * recurse
#         print(space, 'returning', result)
#         return result
# factorial(4)


# import math
# def sphere(r):   
#     mass = 95
#     volume = 4/3 * math.pi * r ** 3
#     surface_area = 4 * math.pi * r ** 2
#     density = mass / volume
#     print(volume)
#     print(surface_area)
#     print(density)
#     return volume

# print(sphere(4))
# print(sphere(7))
# sphere(8)


# import math
# def sphere(r):   
#     mass = 95
#     volume = 4/3 * math.pi * r ** 3
#     surface_area = 4 * math.pi * r ** 2
#     density = mass / volume
#     print(volume)
#     print(surface_area)
#     print(density)
#     return r

# sphere(8)
# sphere(4)
# sphere(-3)


# def factorial(n):
#     space = ' ' * (4 * n)
#     print(space, 'factorial', n)
#     if n == 0:
#         print(space, 'returning 1')
#         return 1
#     else:
#         recurse = factorial(n-1)
#         result = n * recurse
#         print(space, 'returning', result)
#         return result
# factorial(4)

# def factorial(n):
#     if not isinstance(n, int):
#         print('Factorial is only defined for integers.')
#         return None
#     elif n < 0:
#         print('Factorial is not defined for negative integers.')
#         return None
#     elif n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial('fred'))

# print(factorial(-2))


# import math

# # step 1 defining hypodenus

# #mathematically, hypotanus (c) is the sum of square of base (b) and height(a) 
# # By pythagorean theorem: c**2 = a**2 + b**2
# # c = math.sqrt(a**2 + b**2) 

# def hypotenus(a, b):
#     return 0.0              #The  return value is the distance represented by a floating-point value.(Downey, 2015)

# hypotenus(6, 8)            # calling the function to check if it is syntetically correct



# # step 2 by computing the sum of square of the base (b) and height (a)


# def hypotenus(a, b):
#     height = a ** 2
#     base = b ** 2
#     c = height + base
#     print("the value of height is: ", height)
#     print("the value of base is: ", base)
#     print("The c variable is the corresponding hypotenus")
#     return 0.0


# hypotenus(6, 8)            # to check if the funxction is bug free



# # step 3 by using math.sqrt() function to compute and return the lenght

# def hypotenus(a, b):
#     c = (a**2) + (b**2)
#     length = math.sqrt(c)
#     return length

# print("the hypotenuse of a right triangle is equal to:", hypotenus(6, 8))

# print("\nThe output of two additional calls to hypotenuse with different arguments.\n")

# print("the hypotenuse of a right triangle is equal to:", hypotenus(5, 6))

# print("\nthe hypotenuse of a right triangle is equal to:", hypotenus(3, 2))



# # part 2

# # definining sphere: the surface of sphere is perfectly ROUND.
# # where Volume = (4/3)*math.pi*r**3, Sufacwe area = 4**pi*r**2
# # finding the 
# # 1. volume of the spere, 
# # 2. the surface area and 
# # 3. the density
# # 4. a sphere of radius(r) 4cm is of mass 95g 

# # step 1: defining the sphere

# def sphere(r):
#     return 0.0

# sphere(4)         # verifying the flow of execussion


# # step 2
# # computing and returning the value for Volume

# def sphere(r):
#     volume = 4/3 * math.pi * r ** 3
#     print(f"\nThe Volume of a sphere = {volume}cm3")
#     return volume

# sphere(4)       


# # step 3
# # computing and returning the value for Surface area
# def sphere(r):
#     surface_area = 4 * math.pi * r ** 2
#     print(f"\nthe Surface area =  {surface_area}cm2")
#     return surface_area

# sphere(4)

# # step 4 
# # computing and returning the value for density
# #the mass of the sphere in gram(g)

# def sphere(r):   
#     mass = 95
#     volume = 4/3 * math.pi * r ** 3
#     density = mass / volume
#     print(f"\nthe density of the sphere = {density}gcm-3")
#     return density

# sphere(4)
# sphere(7)
# sphere(1)


# import math

# e = math.exp(1.0)
# height = radius * math.sin(radians)

# def area(radius):
# a = math.pi * radius**2
# return a

# def area(radius):
# return math.pi * radius**2


# def absolute_value(x):
# if x < 0:
# return -x
# else:
# return x

# def absolute_value(x):
# if x < 0:
# return -x
# if x > 0:
# return x

# # As an exercise, write a compare function takes two values, x and y, and returns 1 if x > y,
# # 0 if x == y, and -1 if x < y


# def distance(x1, y1, x2, y2):
# return 0.0

# distance(1, 2, 4, 6)


# def distance(x1, y1, x2, y2):
# dx = x2 - x1
# dy = y2 - y1
# print('dx is', dx)
# print('dy is', dy)
# return 0.0

# def distance(x1, y1, x2, y2):
# dx = x2 - x1
# dy = y2 - y1
# dsquared = dx**2 + dy**2
# print('dsquared is: ', dsquared)
# return 0.0

# def distance(x1, y1, x2, y2):
# dx = x2 - x1
# dy = y2 - y1
# dsquared = dx**2 + dy**2
# result = math.sqrt(dsquared)
# return result

# # As an exercise, use incremental development to write a function called hypotenuse that
# # returns the length of the hypotenuse of a right triangle given the lengths of the other two
# # legs as arguments. Record each stage of the development process as you go.

# import math

# def area(radius):
#     a = math.pi * radius**2
#     return a

# def area(radius):
#     return math.pi * radius**2

# def absolute_value(x):
#     if x < 0:
#         return -x
#     else:
#         return x
    
# print(absolute_value(0))

# # As an exercise, write a compare function takes two values, x and y, and returns 1 if x > y,
# # 0 if x == y, and -1 if x < y.


# # incremental development


# # suppose you want to find the distance between two points, given by the
# # coordinates (x1, y1) and (x2, y2). By the Pythagorean theorem, the distance is:

# # In this case, the inputs are two points, which you can represent using four numbers. The return value is the distance represented by a floating-point value. Immediately you can write an outline of the function:


# def distance(x1, y1, x2, y2):
#     return 0.0

# distance(1, 2, 4, 6)


# # step 2 find the difference b/w x2-x1 & y2-y1
# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     print('dx is', dx)
#     print('dy is', dy)
#     return 0.0


# distance(1, 2, 4, 6)

# # step 3 compute the sum of squares of dx and dy

# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquared = dx**2 + dy**2
#     print('dsquared is: ', dsquared)
#     return 0.0

# distance(1, 2, 4, 6)


# # step 3 use math.sqrt function to compute and return the result:

# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquared = dx**2 + dy**2
#     result = math.sqrt(dsquared)
#     return result


# print(distance(1, 2, 4, 6))


# #  a function that takes two points, the center of the circle and a point on the perimeter, and computes the area of the circleAssume that the center point is stored in the variables xc and yc, and the perimeter point is in xp and yp. The first step is to find the radius of the circle, which is the distance between the two points.  We just wrote a function, distance, that does that: radius = distance(xc, yc, xp, yp)


# radius = distance(xc, yc, xp, yp)

# result = area(radius)

# def circle_area(xc, yc, xp, yp):
#     radius = distance(xc, yc, xp, yp)
#     result = area(radius)
#     return result


# def circle_area(xc, yc, xp, yp):
#     return area(distance(xc, yc, xp, yp))


# def is_divisible(x, y):
#     if x % y == 0:
#     return True
#     else:
#     return False


# is_divisible(6, 4)
# is_divisible(6, 3)


# def is_divisible(x, y):
# return x % y == 0
# Boolean functions are often used in conditional statements:
# if is_divisible(x, y):
# print('x is divisible by y')
# It might be tempting to write something like:
# if is_divisible(x, y) == True:
# print('x is divisible by y')
# But the extra comparison is unnecessary.
# As an exercise, write a function is_between(x, y, z) that returns True if x  y  z or
# False otherwise.


# def factorial(n):
# if n == 0:
# return 1



# def factorial(n):
# if n == 0:
# return 1
# else:
# recurse = factorial(n-1)
# result = n * recurse
# return result

# # fibonacci

# def fibonacci(n):
# if n == 0:
# return 0
# elif n == 1:
# return 1
# else:
# return fibonacci(n-1) + fibonacci(n-2)


# def factorial(n):
# if not isinstance(n, int):
# print('Factorial is only defined for integers.')
# return None
# elif n < 0:
# print('Factorial is not defined for negative integers.')
# return None
# elif n == 0:
# return 1
# else:
# return n * factorial(n-1)

# print(factorial('fred'))

# print(factorial(-2))

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')





# # part 2
# # example 1

# a = "adamu labaran computer science student at uopeople"
# print(a)

# print(len(a))

# # the inbuilt function len() was used to check the length of character in variable "a"
# # output: 50

# print(a[:])

# # a[:] print the entire character in "a" variable
# #output: 'adamu labaran computer science student at uopeople'

# print(a[0:0])

# # return empty string 
# # output: ' '


# print(a[0])

# # this print first character in the string
# # output: 'a'

# print(a[49])

# # last character in the string
# # output:  'e'

# print(a[14:22])

# # this print 14 - 22 character in the string
# # 'computer'


# print(a[12:22:5])

# # return every 5th  character from 12 to 22
# # output: 'np'

# print(a[12:50:5])

# # return every 5th  character from 12 to 50
# # output: 'np nttup'

# print(a[0:50:5])

# # return every 5th  character from 0 to 50
# # output: 'a roei ete'

# print(a[0:50:3])

# # return every 3th  character from 0 to 50
# # output: 'a roei ete'

# # example 2

# b = 'welcome to python course'

# print(b[0:7])

# # return the first 7th character 
# # output: 'welcome'

# print(b[7:10])

# # Return from 7th to 10 character
# # output: ' to'

# print(b[10:17])

# # return from 10th to 17th character
# # output: ' python'

# print(b[17:24])

# # return 17th to 24th character
# # output: ' course'

# print(b[:24])

# # return everything
# # output:'welcome to python course'

# print(b[24:])

# # return empty string
# # output: ''


# print(b[10:24])

# # return 10th to 24 character
# # output: ' python course'

# # example 3
# c = 'python a programmin foundamental course at uopeople'


# print(c[ : -8])

# # The -8 corresponding to [n:-m] where the negative m-eth (-m) value return anticlockwise. in this case it return the n-eth value and delete the last value. 
# # output: 'python a programmin foundamental course at '

# print(c[-8:])

# # at the other hand the [-n:m] where the -n-eth count from last and the 8th most value which "uopeople"
# # output: 'uopeople'

# print(c[-19:])

# # -n-eth term return last most value
# # output: ' course at uopeople'

# print(c[:-19])
# # -m-eth return first value cut off last value 
# # output: 'python a programmin foundamental'


# epsilon = 0.00000000001

# def my_sqrt(a):
#     x =  a / 2
#     while True:
#         y = (x + a / x) / 2
#         if abs(y - x) < epsilon:
#             print(y)
#             return y
#             break
#         x = y
# my_sqrt(9)


# def right_digit(n):
#     trunc = f'{n:.11f}'
#     dig = trunc[len(trunc)-1]
#     print(dig)
#     return dig
# right_digit(9)


# def test_sqrt(n):
#     print('a', ' '*1, 'mysqrt(a)', ' '*3, 'math.sqrt(a)', 'diff')
#     print('_', ' '*1, '_'*9, ' '*3, '_'*12, ' ' + '_'*4)
    
#     for i in range(9):
#         x = i + 1
        
#         print(f'{x:0.1f}', end=' ')
        
#         if my_sqrt(x) - int(my_sqrt(x)) < 0.001:
#             y = 1
#         elif right_digit(my_sqrt(x)) == '0':
#             y = 0
#         else:
#             y = 11
            
#         print(f'{my_sqrt(x): < 13.{y}}', end=' ')
#         print(f'{my_sqrt(x): < 13.{y}}', end=' ')
        
#         diff = math.sqrt(x) - my_sqrt(x)
#         print(f'{diff:.12g}')
        
        
# test_sqrt(9)

# import math
# a  = 9
# x = 2
# def mysqrt(a):
#     x = a / 2
#     while True:
#         y = (x + a / x) / 2
#         if x - y < 0.00001:
#             break
#         x = y
#     print(y)
#     return y

# mysqrt(9)


# def diff(a):
#     d = mysqrt(a) - math.sqrt(a)
#     print(d)

# diff(9)


# def test_sqrt(a):
#     print(
#         'a', ' '*2,
#         'mysqrt(a)', ' '*11,
#         'math.sqrt(a)', ' '*8,
#         'diff'
#     )
#     while a > 1:
#         a = a-1
#         len_a = 3 - len(str(a))
#         len_my = 20 - len(str(mysqrt(a)))
#         len_ma = 20 - len(str(math.sqrt(a)))
#         print(
#             a, ' '* len_a,
#             mysqrt(a), ' '* len_my,
#             math.sqrt(a), ' '*len_ma,
#             diff(a)
#         )
#     return

# test_sqrt(10)


# a = 9
# x = 2
# while True:
#     print(x)
#     y = (x + a/x) / 2.0
#     if y == x:
#             break
#     x = y


# def my_sqrt(a):
#     x = a / 2
#     while True:
#         print(x)
#         y = (x + a / x) / 2.0
#         if y == x:
#             break
#         x = y
        
# my_sqrt(9)


# def find(word, letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1

# print(find("adamslabaran","a"))

# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

# word = 'banana'
# print(word.upper())

# new_word = word.upper()
# print(new_word)

# index = word.find('a')
# print(index)

# print(word.find('na', 3))

# def in_both(word1, word2):
#     for letter in word1:
#         if letter in word2:
#             print(letter)
            
            
# in_both('adams', 'labaran')
# in_both('apples', 'oranges')


# if word < 'banana':
#     print('Your word, ' + word + ', comes before banana.')
# elif word > 'banana':
#     print('Your word, ' + word + ', comes after banana.')
# else:
#     print('All right, bananas.')
    
    
# # def is_reverse(word1, word2):
# # if len(word1) != len(word2):
# # return False
# # i = 0
# # j = len(word2)
# # while j > 0:
# # if word1[i] != word2[j]:
# # return False
# # i = i+1
# # j = j-1
# # return 


# from decimal import *
# import math
# # this function compute square root of 9 using newton's method

# def my_sqrt(a):
#     x = 2
#     while True:
#         y = (x + a/x)/2
#         if x == y:
#             break
#         x = y
#     print(y)
#     return x

# # my_sqrt(9)

# # this function compute square root of 9 using math.sqrt()
# def math_sqrt(a):
#     x = math.sqrt(a)
#     print(x)
#     return x

# # math_sqrt(9)

# # this function compute the difference between the newton's method and math.sqrt()

# def diff(a):
#     p = my_sqrt(a)
#     q = math_sqrt(a)
#     d = p - q 
#     print(d)
#     return d
    
# # diff(9)


# # this function compute the table

# def test_square_root():
#     for a in range(1, 10):
#         print(float(a), " "*20, f"{my_sqrt(a)}", " "*20, f"{math_sqrt(a)}", " "*20, f"{diff(a)}")
#         # print('a', ' '*1, 'mysqrt(a)', ' '*3, 'math.sqrt(a)', 'diff')
#         # print('_', ' '*1, '_'*9, ' '*3, '_'*12, ' ' + '_'*4)
        
# test_square_root()


# def dec_1(a):
#     decOne = Decimal(my_sqrt(a))
#     # print(dec)
#     decTwo = round(decOne, 9)
#     print(decTwo)
#     return Decimal(decTwo)

# dec_1(9)


# def dec_2(a):
#     decOne = Decimal(math_sqrt(a))
#     # print(dec)
#     decTwo = round(decOne, 9)
#     print(decTwo)
#     return Decimal(decTwo)

# dec_2(9)


# def table():
#     for a in range(1, 10):
#         print(float(a), " "*20, f"{dec_2(a)}", " "*9, f"{dec_2(a)}", " "*9, f"{diff(a)}")
    
# table()


# from decimal import *
# import math

# def my_sqrt(a):
#     x = 2
#     while True:
#         y = (x + a/x)/2
#         if x == y:
#             break
#         x = y
#     print(y)
#     return x

# my_sqrt(9)

# # Discussion Assignment
# # Welcome to Unit 3 Discussion Forum. 

# # Describe the difference between a chained conditional and a nested conditional. Give your own example of each. Do not copy examples from the textbook.

# >>> # chain conditional
# >>> 
# >>> name = 'salma'
# >>> if name == 'adamu':
# ...     print('he is a male')
# ... elif name == 'labaran':
# ...     print('he is our dad')
# ... elif name == 'afra':
# ...     print('she is our young baby')
# ... else:
# ...     print(f"the name is {name}")
# ...
# output: 
# the name is salma
# >>> 

# nested conditional
# >>> age = 18
# >>> if age == age:
# ...     print('he can drink')
# ... else:
# ...     if age < age:
# ...             print('he cannot drink!')
# ...     else:
# ...             print('we dont want trouble!, send him back')
# ...
# he can drink
# >>>


# # Deeply nested conditionals can become difficult to read. Describe a strategy for avoiding nested conditionals. Give your own example of a nested conditional that can be modified to become a single conditional, and show the equivalent single conditional. Do not copy the example from the textbook.

# name1 = 'adamu'
# name2 = 'labaran'
# name3 = 'salma'
# name4 = 'usman'

# if name1 == name2: # not True 
#     print(name1) 
# else:
#     if name1 == name3:  # not True
#         print(name2)
#     else:
#         if name1 == name4: # not True
#             print(name3)
#         else:
#             if name3 == name1:  # not True
#                print(name4)
#             else:
#                 print("options not true")
                
# if name1 == name2:
#     print(name1)
# elif name1 == name3:
#     print(name2)
# elif name1 == name4:
#     print(name3)
# elif name3 == name1:
#     print(name4)
# else:
#     print("options are not true")
             

# # Write a new recursive function countup that expects a negative argument and counts “up” from that number. Output from running the function should look something like this:

# # >>> countup(-3)
# # -3
# # -2
# # -1
# # Blastoff!

# # Write a Python program that gets a number using keyboard input. (Remember to use input for Python 3 but raw_input for Python 2.)

# # If the number is positive, the program should call countdown. If the number is negative, the program should call countup. Choose for yourself which function to call (countdown or countup) for input of zero.

# def countdown(n):
#     if n <= 0:
#         print("Blastoff!")
#     else:
#         print(n)
#         countdown(n-1)

# countdown(9)

# def countup(n):
#     if n >= 0:
#         print("Blasstoff!")
#     else:
#         print(n)
#         countup(n+1)
        
# countup(-9)

# def coutntuodown(n):
#     if n <= 0 or n >= 0:
#         countdown(n)
#         countup(n)
#     else:
#         countdown(n)
#         countup(n)
# coutntuodown(0)



# def countup(n):
#     if n >= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countup(n+1)
        
# countup(-3)

# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)
        
# countdown(3)

# def countup_or_countdown(n):
#     if n >= 0 or n <= 0:
#         countup(n)
#         countdown(n)
#     else:
#         countup(n+1)
#         countdown(n-1)
  

# countup_or_countdown(6) 
# countup_or_countdown(-6) 
# countup_or_countdown(0) 

# x = 5
# y = 4

# def or_logic():
#     if x > y or x < y:
#         print("since one of the if condition is true\nI'll first execute")
#     elif x < y or x > y:
#         print("since one of the if condition is true\nI'll first execute")
#     else:
#         print("i wouldn't execute! ")
        
# or_logic()

# def and_logic():
#     if x > y and x < y:
#         print("both condition must be true! or else will print")
#     elif x < y and x > y:
#          print("both condition must be true! or else will print")
#     else:
#         print("I'll execute because one of the condition above is not true!")
        
# and_logic()


# import math

# def area(radius):
#     a = math.pi * radius**2
#     return a
# num = input('value:')
# a = int(num)
# print(area(a))
# def area(radius):
#     return math.pi * radius**2



# def absolute_value(x):
#     if x < 0:
#         return -x
#     else:
#         return x
    
# print(absolute_value(9))

# def countdown(n):
#     if n <= 0:
#         print("Blastoff!")
#     else:
#         print(n)
#         countdown(n-1)

# # countdown(9)

# def countup(n):
#     if n >= 0:
#         print("Blasstoff!")
#     else:
#         print(n)
#         countup(n+1)
        
# # countup(-9)

# def coutntuodown(n):
#     if n <= 0 or n >= 0:
#         countdown(n)
#         countup(n)
#     else:
#         countdown(n)
#         countup(n)
# coutntuodown(7)


# # correct solution
# def countup(n):
#     if n >= 0:
#         print("Blasstoff!")
#     else:
#         print(n)
#         countup(n+1)
        
# countup(-9)


# def countdown(n):
#     if n <= 0:
#         print("Blastoff!")
#     else:
#         print(n)
#         countdown(n-1)
# countdown(9)

# def coutup_or_countdown(n):
#     # n = int(input('enter a value:\n'))
#     if n <= 0:
#         countup(n)
#         countdown(n)
#     elif n >= 0:
#         countdown(n)
#         countup(n)
        
# coutup_or_countdown(0)


# x = "There are %d types of people." % 10
# binary = "binary"
# do_not = "don't"
# y = "Those who know %s and those who %s." % (binary, do_not)

# print x
# print y

# print "I said: %r." % x
# print "I also said: '%s'." % y

# hilarious = False
# joke_evaluation = "Isn't that joke so funny?! %r"

# print joke_evaluation % hilarious

# w = "This is the left side of..."
# e = "a string with a right side."

# print w + e

# def main():
#     print("\n" + "-" * 40)
#     print("\nWelcome to the Letter Grade Program")

#     grade = int(input("Enter a grade: "))
#     letter = ""

#     if grade > 89:
#         letter += "A"
#     elif grade > 79:
#         letter += "B"
#     elif grade > 69:
#         letter += "C"
#     else:
#         letter += "F"

#     print("\nThe grade is " + str(grade) + ".")
#     print("The letter grade is " + letter + ".\n")
#     print("-" * 40)

# main()

# def main():
#     print("\n" + "-" * 60)
#     print("Divisibility By Six Program")
#     print("A number is divisible by 6 is it is divisible by 2 and 3.")

#     number = int(input("\nEnter a number: "))

#     if number % 2 == 0 or number % 3 == 0:
#         if number % 6 == 0:
#             print("\nThe number " + str(number) + " is divisible by 2,")
#             print("divisible by 3, and divisible by 6. \n")
#         else:
#             for factor in range(2, 4):
#                 if number % factor == 0:
#                     print("\nThe number " + str(number) + " is only divisible by " + str(factor) + ".")
#                 else:
#                     print("\nThe number " + str(number) + " is not divisible by 6.")

#     print("-" * 60 + "\n")

# main()


# def factorial(n):
#     space = ' ' * (4 * n)
#     print(space, 'factorial', n)
#     if n == 0:
#         print(space, 'returning 1')
#         return 1
#     else:
#         recurse = factorial(n-1)
#         result = n * recurse
#         print(space, 'returning', result)
#         return result
# factorial(4)


# import math
# def sphere(r):   
#     mass = 95
#     volume = 4/3 * math.pi * r ** 3
#     surface_area = 4 * math.pi * r ** 2
#     density = mass / volume
#     print(volume)
#     print(surface_area)
#     print(density)
#     return volume

# print(sphere(4))
# print(sphere(7))
# sphere(8)


# import math
# def sphere(r):   
#     mass = 95
#     volume = 4/3 * math.pi * r ** 3
#     surface_area = 4 * math.pi * r ** 2
#     density = mass / volume
#     print(volume)
#     print(surface_area)
#     print(density)
#     return r

# sphere(8)
# sphere(4)
# sphere(-3)


# def factorial(n):
#     space = ' ' * (4 * n)
#     print(space, 'factorial', n)
#     if n == 0:
#         print(space, 'returning 1')
#         return 1
#     else:
#         recurse = factorial(n-1)
#         result = n * recurse
#         print(space, 'returning', result)
#         return result
# factorial(4)

# def factorial(n):
#     if not isinstance(n, int):
#         print('Factorial is only defined for integers.')
#         return None
#     elif n < 0:
#         print('Factorial is not defined for negative integers.')
#         return None
#     elif n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial('fred'))

# print(factorial(-2))


# import math

# # step 1 defining hypodenus

# #mathematically, hypotanus (c) is the sum of square of base (b) and height(a) 
# # By pythagorean theorem: c**2 = a**2 + b**2
# # c = math.sqrt(a**2 + b**2) 

# def hypotenus(a, b):
#     return 0.0              #The  return value is the distance represented by a floating-point value.(Downey, 2015)

# hypotenus(6, 8)            # calling the function to check if it is syntetically correct



# # step 2 by computing the sum of square of the base (b) and height (a)


# def hypotenus(a, b):
#     height = a ** 2
#     base = b ** 2
#     c = height + base
#     print("the value of height is: ", height)
#     print("the value of base is: ", base)
#     print("The c variable is the corresponding hypotenus")
#     return 0.0


# hypotenus(6, 8)            # to check if the funxction is bug free



# # step 3 by using math.sqrt() function to compute and return the lenght

# def hypotenus(a, b):
#     c = (a**2) + (b**2)
#     length = math.sqrt(c)
#     return length

# print("the hypotenuse of a right triangle is equal to:", hypotenus(6, 8))

# print("\nThe output of two additional calls to hypotenuse with different arguments.\n")

# print("the hypotenuse of a right triangle is equal to:", hypotenus(5, 6))

# print("\nthe hypotenuse of a right triangle is equal to:", hypotenus(3, 2))



# # part 2

# # definining sphere: the surface of sphere is perfectly ROUND.
# # where Volume = (4/3)*math.pi*r**3, Sufacwe area = 4**pi*r**2
# # finding the 
# # 1. volume of the spere, 
# # 2. the surface area and 
# # 3. the density
# # 4. a sphere of radius(r) 4cm is of mass 95g 

# # step 1: defining the sphere

# def sphere(r):
#     return 0.0

# sphere(4)         # verifying the flow of execussion


# # step 2
# # computing and returning the value for Volume

# def sphere(r):
#     volume = 4/3 * math.pi * r ** 3
#     print(f"\nThe Volume of a sphere = {volume}cm3")
#     return volume

# sphere(4)       


# # step 3
# # computing and returning the value for Surface area
# def sphere(r):
#     surface_area = 4 * math.pi * r ** 2
#     print(f"\nthe Surface area =  {surface_area}cm2")
#     return surface_area

# sphere(4)

# # step 4 
# # computing and returning the value for density
# #the mass of the sphere in gram(g)

# def sphere(r):   
#     mass = 95
#     volume = 4/3 * math.pi * r ** 3
#     density = mass / volume
#     print(f"\nthe density of the sphere = {density}gcm-3")
#     return density

# sphere(4)
# sphere(7)
# sphere(1)


# import math

# e = math.exp(1.0)
# height = radius * math.sin(radians)

# def area(radius):
# a = math.pi * radius**2
# return a

# def area(radius):
# return math.pi * radius**2


# def absolute_value(x):
# if x < 0:
# return -x
# else:
# return x

# def absolute_value(x):
# if x < 0:
# return -x
# if x > 0:
# return x

# # As an exercise, write a compare function takes two values, x and y, and returns 1 if x > y,
# # 0 if x == y, and -1 if x < y


# def distance(x1, y1, x2, y2):
# return 0.0

# distance(1, 2, 4, 6)


# def distance(x1, y1, x2, y2):
# dx = x2 - x1
# dy = y2 - y1
# print('dx is', dx)
# print('dy is', dy)
# return 0.0

# def distance(x1, y1, x2, y2):
# dx = x2 - x1
# dy = y2 - y1
# dsquared = dx**2 + dy**2
# print('dsquared is: ', dsquared)
# return 0.0

# def distance(x1, y1, x2, y2):
# dx = x2 - x1
# dy = y2 - y1
# dsquared = dx**2 + dy**2
# result = math.sqrt(dsquared)
# return result

# # As an exercise, use incremental development to write a function called hypotenuse that
# # returns the length of the hypotenuse of a right triangle given the lengths of the other two
# # legs as arguments. Record each stage of the development process as you go.

# import math

# def area(radius):
#     a = math.pi * radius**2
#     return a

# def area(radius):
#     return math.pi * radius**2

# def absolute_value(x):
#     if x < 0:
#         return -x
#     else:
#         return x
    
# print(absolute_value(0))

# # As an exercise, write a compare function takes two values, x and y, and returns 1 if x > y,
# # 0 if x == y, and -1 if x < y.


# # incremental development


# # suppose you want to find the distance between two points, given by the
# # coordinates (x1, y1) and (x2, y2). By the Pythagorean theorem, the distance is:

# # In this case, the inputs are two points, which you can represent using four numbers. The return value is the distance represented by a floating-point value. Immediately you can write an outline of the function:


# def distance(x1, y1, x2, y2):
#     return 0.0

# distance(1, 2, 4, 6)


# # step 2 find the difference b/w x2-x1 & y2-y1
# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     print('dx is', dx)
#     print('dy is', dy)
#     return 0.0


# distance(1, 2, 4, 6)

# # step 3 compute the sum of squares of dx and dy

# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquared = dx**2 + dy**2
#     print('dsquared is: ', dsquared)
#     return 0.0

# distance(1, 2, 4, 6)


# # step 3 use math.sqrt function to compute and return the result:

# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquared = dx**2 + dy**2
#     result = math.sqrt(dsquared)
#     return result


# print(distance(1, 2, 4, 6))


# #  a function that takes two points, the center of the circle and a point on the perimeter, and computes the area of the circleAssume that the center point is stored in the variables xc and yc, and the perimeter point is in xp and yp. The first step is to find the radius of the circle, which is the distance between the two points.  We just wrote a function, distance, that does that: radius = distance(xc, yc, xp, yp)


# radius = distance(xc, yc, xp, yp)

# result = area(radius)

# def circle_area(xc, yc, xp, yp):
#     radius = distance(xc, yc, xp, yp)
#     result = area(radius)
#     return result


# def circle_area(xc, yc, xp, yp):
#     return area(distance(xc, yc, xp, yp))


# def is_divisible(x, y):
#     if x % y == 0:
#     return True
#     else:
#     return False


# is_divisible(6, 4)
# is_divisible(6, 3)


# def is_divisible(x, y):
# return x % y == 0
# Boolean functions are often used in conditional statements:
# if is_divisible(x, y):
# print('x is divisible by y')
# It might be tempting to write something like:
# if is_divisible(x, y) == True:
# print('x is divisible by y')
# But the extra comparison is unnecessary.
# As an exercise, write a function is_between(x, y, z) that returns True if x  y  z or
# False otherwise.


# def factorial(n):
# if n == 0:
# return 1



# def factorial(n):
# if n == 0:
# return 1
# else:
# recurse = factorial(n-1)
# result = n * recurse
# return result

# # fibonacci

# def fibonacci(n):
# if n == 0:
# return 0
# elif n == 1:
# return 1
# else:
# return fibonacci(n-1) + fibonacci(n-2)


# def factorial(n):
# if not isinstance(n, int):
# print('Factorial is only defined for integers.')
# return None
# elif n < 0:
# print('Factorial is not defined for negative integers.')
# return None
# elif n == 0:
# return 1
# else:
# return n * factorial(n-1)

# print(factorial('fred'))

# print(factorial(-2))

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')





# # part 2
# # example 1

# a = "adamu labaran computer science student at uopeople"
# print(a)

# print(len(a))

# # the inbuilt function len() was used to check the length of character in variable "a"
# # output: 50

# print(a[:])

# # a[:] print the entire character in "a" variable
# #output: 'adamu labaran computer science student at uopeople'

# print(a[0:0])

# # return empty string 
# # output: ' '


# print(a[0])

# # this print first character in the string
# # output: 'a'

# print(a[49])

# # last character in the string
# # output:  'e'

# print(a[14:22])

# # this print 14 - 22 character in the string
# # 'computer'


# print(a[12:22:5])

# # return every 5th  character from 12 to 22
# # output: 'np'

# print(a[12:50:5])

# # return every 5th  character from 12 to 50
# # output: 'np nttup'

# print(a[0:50:5])

# # return every 5th  character from 0 to 50
# # output: 'a roei ete'

# print(a[0:50:3])

# # return every 3th  character from 0 to 50
# # output: 'a roei ete'

# # example 2

# b = 'welcome to python course'

# print(b[0:7])

# # return the first 7th character 
# # output: 'welcome'

# print(b[7:10])

# # Return from 7th to 10 character
# # output: ' to'

# print(b[10:17])

# # return from 10th to 17th character
# # output: ' python'

# print(b[17:24])

# # return 17th to 24th character
# # output: ' course'

# print(b[:24])

# # return everything
# # output:'welcome to python course'

# print(b[24:])

# # return empty string
# # output: ''


# print(b[10:24])

# # return 10th to 24 character
# # output: ' python course'

# # example 3
# c = 'python a programmin foundamental course at uopeople'


# print(c[ : -8])

# # The -8 corresponding to [n:-m] where the negative m-eth (-m) value return anticlockwise. in this case it return the n-eth value and delete the last value. 
# # output: 'python a programmin foundamental course at '

# print(c[-8:])

# # at the other hand the [-n:m] where the -n-eth count from last and the 8th most value which "uopeople"
# # output: 'uopeople'

# print(c[-19:])

# # -n-eth term return last most value
# # output: ' course at uopeople'

# print(c[:-19])
# # -m-eth return first value cut off last value 
# # output: 'python a programmin foundamental'


# epsilon = 0.00000000001

# def my_sqrt(a):
#     x =  a / 2
#     while True:
#         y = (x + a / x) / 2
#         if abs(y - x) < epsilon:
#             print(y)
#             return y
#             break
#         x = y
# my_sqrt(9)


# def right_digit(n):
#     trunc = f'{n:.11f}'
#     dig = trunc[len(trunc)-1]
#     print(dig)
#     return dig
# right_digit(9)


# def test_sqrt(n):
#     print('a', ' '*1, 'mysqrt(a)', ' '*3, 'math.sqrt(a)', 'diff')
#     print('_', ' '*1, '_'*9, ' '*3, '_'*12, ' ' + '_'*4)
    
#     for i in range(9):
#         x = i + 1
        
#         print(f'{x:0.1f}', end=' ')
        
#         if my_sqrt(x) - int(my_sqrt(x)) < 0.001:
#             y = 1
#         elif right_digit(my_sqrt(x)) == '0':
#             y = 0
#         else:
#             y = 11
            
#         print(f'{my_sqrt(x): < 13.{y}}', end=' ')
#         print(f'{my_sqrt(x): < 13.{y}}', end=' ')
        
#         diff = math.sqrt(x) - my_sqrt(x)
#         print(f'{diff:.12g}')
        
        
# test_sqrt(9)

# import math
# a  = 9
# x = 2
# def mysqrt(a):
#     x = a / 2
#     while True:
#         y = (x + a / x) / 2
#         if x - y < 0.00001:
#             break
#         x = y
#     print(y)
#     return y

# mysqrt(9)


# def diff(a):
#     d = mysqrt(a) - math.sqrt(a)
#     print(d)

# diff(9)


# def test_sqrt(a):
#     print(
#         'a', ' '*2,
#         'mysqrt(a)', ' '*11,
#         'math.sqrt(a)', ' '*8,
#         'diff'
#     )
#     while a > 1:
#         a = a-1
#         len_a = 3 - len(str(a))
#         len_my = 20 - len(str(mysqrt(a)))
#         len_ma = 20 - len(str(math.sqrt(a)))
#         print(
#             a, ' '* len_a,
#             mysqrt(a), ' '* len_my,
#             math.sqrt(a), ' '*len_ma,
#             diff(a)
#         )
#     return

# test_sqrt(10)


# a = 9
# x = 2
# while True:
#     print(x)
#     y = (x + a/x) / 2.0
#     if y == x:
#             break
#     x = y


# def my_sqrt(a):
#     x = a / 2
#     while True:
#         print(x)
#         y = (x + a / x) / 2.0
#         if y == x:
#             break
#         x = y
        
# my_sqrt(9)


# def find(word, letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1

# print(find("adamslabaran","a"))

# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

# word = 'banana'
# print(word.upper())

# new_word = word.upper()
# print(new_word)

# index = word.find('a')
# print(index)

# print(word.find('na', 3))

# def in_both(word1, word2):
#     for letter in word1:
#         if letter in word2:
#             print(letter)
            
            
# in_both('adams', 'labaran')
# in_both('apples', 'oranges')


# if word < 'banana':
#     print('Your word, ' + word + ', comes before banana.')
# elif word > 'banana':
#     print('Your word, ' + word + ', comes after banana.')
# else:
#     print('All right, bananas.')
    
    
# # def is_reverse(word1, word2):
# # if len(word1) != len(word2):
# # return False
# # i = 0
# # j = len(word2)
# # while j > 0:
# # if word1[i] != word2[j]:
# # return False
# # i = i+1
# # j = j-1
# # return 

# # Discussion Assignment
# # Welcome to Unit 3 Discussion Forum. 

# # Describe the difference between a chained conditional and a nested conditional. Give your own example of each. Do not copy examples from the textbook.

# >>> # chain conditional
# >>> 
# >>> name = 'salma'
# >>> if name == 'adamu':
# ...     print('he is a male')
# ... elif name == 'labaran':
# ...     print('he is our dad')
# ... elif name == 'afra':
# ...     print('she is our young baby')
# ... else:
# ...     print(f"the name is {name}")
# ...
# output: 
# the name is salma
# >>> 

# nested conditional
# >>> age = 18
# >>> if age == age:
# ...     print('he can drink')
# ... else:
# ...     if age < age:
# ...             print('he cannot drink!')
# ...     else:
# ...             print('we dont want trouble!, send him back')
# ...
# he can drink
# >>>


# # Deeply nested conditionals can become difficult to read. Describe a strategy for avoiding nested conditionals. Give your own example of a nested conditional that can be modified to become a single conditional, and show the equivalent single conditional. Do not copy the example from the textbook.

# name1 = 'adamu'
# name2 = 'labaran'
# name3 = 'salma'
# name4 = 'usman'

# if name1 == name2: # not True 
#     print(name1) 
# else:
#     if name1 == name3:  # not True
#         print(name2)
#     else:
#         if name1 == name4: # not True
#             print(name3)
#         else:
#             if name3 == name1:  # not True
#                print(name4)
#             else:
#                 print("options not true")
                
# if name1 == name2:
#     print(name1)
# elif name1 == name3:
#     print(name2)
# elif name1 == name4:
#     print(name3)
# elif name3 == name1:
#     print(name4)
# else:
#     print("options are not true")
             

# # Write a new recursive function countup that expects a negative argument and counts “up” from that number. Output from running the function should look something like this:

# # >>> countup(-3)
# # -3
# # -2
# # -1
# # Blastoff!

# # Write a Python program that gets a number using keyboard input. (Remember to use input for Python 3 but raw_input for Python 2.)

# # If the number is positive, the program should call countdown. If the number is negative, the program should call countup. Choose for yourself which function to call (countdown or countup) for input of zero.

# def countdown(n):
#     if n <= 0:
#         print("Blastoff!")
#     else:
#         print(n)
#         countdown(n-1)

# countdown(9)

# def countup(n):
#     if n >= 0:
#         print("Blasstoff!")
#     else:
#         print(n)
#         countup(n+1)
        
# countup(-9)

# def coutntuodown(n):
#     if n <= 0 or n >= 0:
#         countdown(n)
#         countup(n)
#     else:
#         countdown(n)
#         countup(n)
# coutntuodown(0)



# def countup(n):
#     if n >= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countup(n+1)
        
# countup(-3)

# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)
        
# countdown(3)

# def countup_or_countdown(n):
#     if n >= 0 or n <= 0:
#         countup(n)
#         countdown(n)
#     else:
#         countup(n+1)
#         countdown(n-1)
  

# countup_or_countdown(6) 
# countup_or_countdown(-6) 
# countup_or_countdown(0) 

# x = 5
# y = 4

# def or_logic():
#     if x > y or x < y:
#         print("since one of the if condition is true\nI'll first execute")
#     elif x < y or x > y:
#         print("since one of the if condition is true\nI'll first execute")
#     else:
#         print("i wouldn't execute! ")
        
# or_logic()

# def and_logic():
#     if x > y and x < y:
#         print("both condition must be true! or else will print")
#     elif x < y and x > y:
#          print("both condition must be true! or else will print")
#     else:
#         print("I'll execute because one of the condition above is not true!")
        
# and_logic()


# import math

# def area(radius):
#     a = math.pi * radius**2
#     return a
# num = input('value:')
# a = int(num)
# print(area(a))
# def area(radius):
#     return math.pi * radius**2



# def absolute_value(x):
#     if x < 0:
#         return -x
#     else:
#         return x
    
# print(absolute_value(9))

# def countdown(n):
#     if n <= 0:
#         print("Blastoff!")
#     else:
#         print(n)
#         countdown(n-1)

# # countdown(9)

# def countup(n):
#     if n >= 0:
#         print("Blasstoff!")
#     else:
#         print(n)
#         countup(n+1)
        
# # countup(-9)

# def coutntuodown(n):
#     if n <= 0 or n >= 0:
#         countdown(n)
#         countup(n)
#     else:
#         countdown(n)
#         countup(n)
# coutntuodown(7)


# # correct solution
# def countup(n):
#     if n >= 0:
#         print("Blasstoff!")
#     else:
#         print(n)
#         countup(n+1)
        
# countup(-9)


# def countdown(n):
#     if n <= 0:
#         print("Blastoff!")
#     else:
#         print(n)
#         countdown(n-1)
# countdown(9)

# def coutup_or_countdown(n):
#     # n = int(input('enter a value:\n'))
#     if n <= 0:
#         countup(n)
#         countdown(n)
#     elif n >= 0:
#         countdown(n)
#         countup(n)
        
# coutup_or_countdown(0)


# x = "There are %d types of people." % 10
# binary = "binary"
# do_not = "don't"
# y = "Those who know %s and those who %s." % (binary, do_not)

# print x
# print y

# print "I said: %r." % x
# print "I also said: '%s'." % y

# hilarious = False
# joke_evaluation = "Isn't that joke so funny?! %r"

# print joke_evaluation % hilarious

# w = "This is the left side of..."
# e = "a string with a right side."

# print w + e

# def main():
#     print("\n" + "-" * 40)
#     print("\nWelcome to the Letter Grade Program")

#     grade = int(input("Enter a grade: "))
#     letter = ""

#     if grade > 89:
#         letter += "A"
#     elif grade > 79:
#         letter += "B"
#     elif grade > 69:
#         letter += "C"
#     else:
#         letter += "F"

#     print("\nThe grade is " + str(grade) + ".")
#     print("The letter grade is " + letter + ".\n")
#     print("-" * 40)

# main()

# def main():
#     print("\n" + "-" * 60)
#     print("Divisibility By Six Program")
#     print("A number is divisible by 6 is it is divisible by 2 and 3.")

#     number = int(input("\nEnter a number: "))

#     if number % 2 == 0 or number % 3 == 0:
#         if number % 6 == 0:
#             print("\nThe number " + str(number) + " is divisible by 2,")
#             print("divisible by 3, and divisible by 6. \n")
#         else:
#             for factor in range(2, 4):
#                 if number % factor == 0:
#                     print("\nThe number " + str(number) + " is only divisible by " + str(factor) + ".")
#                 else:
#                     print("\nThe number " + str(number) + " is not divisible by 6.")

#     print("-" * 60 + "\n")

# main()


# def factorial(n):
#     space = ' ' * (4 * n)
#     print(space, 'factorial', n)
#     if n == 0:
#         print(space, 'returning 1')
#         return 1
#     else:
#         recurse = factorial(n-1)
#         result = n * recurse
#         print(space, 'returning', result)
#         return result
# factorial(4)


# import math
# def sphere(r):   
#     mass = 95
#     volume = 4/3 * math.pi * r ** 3
#     surface_area = 4 * math.pi * r ** 2
#     density = mass / volume
#     print(volume)
#     print(surface_area)
#     print(density)
#     return volume

# print(sphere(4))
# print(sphere(7))
# sphere(8)


# import math
# def sphere(r):   
#     mass = 95
#     volume = 4/3 * math.pi * r ** 3
#     surface_area = 4 * math.pi * r ** 2
#     density = mass / volume
#     print(volume)
#     print(surface_area)
#     print(density)
#     return r

# sphere(8)
# sphere(4)
# sphere(-3)


# def factorial(n):
#     space = ' ' * (4 * n)
#     print(space, 'factorial', n)
#     if n == 0:
#         print(space, 'returning 1')
#         return 1
#     else:
#         recurse = factorial(n-1)
#         result = n * recurse
#         print(space, 'returning', result)
#         return result
# factorial(4)

# def factorial(n):
#     if not isinstance(n, int):
#         print('Factorial is only defined for integers.')
#         return None
#     elif n < 0:
#         print('Factorial is not defined for negative integers.')
#         return None
#     elif n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial('fred'))

# print(factorial(-2))


# import math

# # step 1 defining hypodenus

# #mathematically, hypotanus (c) is the sum of square of base (b) and height(a) 
# # By pythagorean theorem: c**2 = a**2 + b**2
# # c = math.sqrt(a**2 + b**2) 

# def hypotenus(a, b):
#     return 0.0              #The  return value is the distance represented by a floating-point value.(Downey, 2015)

# hypotenus(6, 8)            # calling the function to check if it is syntetically correct



# # step 2 by computing the sum of square of the base (b) and height (a)


# def hypotenus(a, b):
#     height = a ** 2
#     base = b ** 2
#     c = height + base
#     print("the value of height is: ", height)
#     print("the value of base is: ", base)
#     print("The c variable is the corresponding hypotenus")
#     return 0.0


# hypotenus(6, 8)            # to check if the funxction is bug free



# # step 3 by using math.sqrt() function to compute and return the lenght

# def hypotenus(a, b):
#     c = (a**2) + (b**2)
#     length = math.sqrt(c)
#     return length

# print("the hypotenuse of a right triangle is equal to:", hypotenus(6, 8))

# print("\nThe output of two additional calls to hypotenuse with different arguments.\n")

# print("the hypotenuse of a right triangle is equal to:", hypotenus(5, 6))

# print("\nthe hypotenuse of a right triangle is equal to:", hypotenus(3, 2))



# # part 2

# # definining sphere: the surface of sphere is perfectly ROUND.
# # where Volume = (4/3)*math.pi*r**3, Sufacwe area = 4**pi*r**2
# # finding the 
# # 1. volume of the spere, 
# # 2. the surface area and 
# # 3. the density
# # 4. a sphere of radius(r) 4cm is of mass 95g 

# # step 1: defining the sphere

# def sphere(r):
#     return 0.0

# sphere(4)         # verifying the flow of execussion


# # step 2
# # computing and returning the value for Volume

# def sphere(r):
#     volume = 4/3 * math.pi * r ** 3
#     print(f"\nThe Volume of a sphere = {volume}cm3")
#     return volume

# sphere(4)       


# # step 3
# # computing and returning the value for Surface area
# def sphere(r):
#     surface_area = 4 * math.pi * r ** 2
#     print(f"\nthe Surface area =  {surface_area}cm2")
#     return surface_area

# sphere(4)

# # step 4 
# # computing and returning the value for density
# #the mass of the sphere in gram(g)

# def sphere(r):   
#     mass = 95
#     volume = 4/3 * math.pi * r ** 3
#     density = mass / volume
#     print(f"\nthe density of the sphere = {density}gcm-3")
#     return density

# sphere(4)
# sphere(7)
# sphere(1)


# import math

# e = math.exp(1.0)
# height = radius * math.sin(radians)

# def area(radius):
# a = math.pi * radius**2
# return a

# def area(radius):
# return math.pi * radius**2


# def absolute_value(x):
# if x < 0:
# return -x
# else:
# return x

# def absolute_value(x):
# if x < 0:
# return -x
# if x > 0:
# return x

# # As an exercise, write a compare function takes two values, x and y, and returns 1 if x > y,
# # 0 if x == y, and -1 if x < y


# def distance(x1, y1, x2, y2):
# return 0.0

# distance(1, 2, 4, 6)


# def distance(x1, y1, x2, y2):
# dx = x2 - x1
# dy = y2 - y1
# print('dx is', dx)
# print('dy is', dy)
# return 0.0

# def distance(x1, y1, x2, y2):
# dx = x2 - x1
# dy = y2 - y1
# dsquared = dx**2 + dy**2
# print('dsquared is: ', dsquared)
# return 0.0

# def distance(x1, y1, x2, y2):
# dx = x2 - x1
# dy = y2 - y1
# dsquared = dx**2 + dy**2
# result = math.sqrt(dsquared)
# return result

# # As an exercise, use incremental development to write a function called hypotenuse that
# # returns the length of the hypotenuse of a right triangle given the lengths of the other two
# # legs as arguments. Record each stage of the development process as you go.

# import math

# def area(radius):
#     a = math.pi * radius**2
#     return a

# def area(radius):
#     return math.pi * radius**2

# def absolute_value(x):
#     if x < 0:
#         return -x
#     else:
#         return x
    
# print(absolute_value(0))

# # As an exercise, write a compare function takes two values, x and y, and returns 1 if x > y,
# # 0 if x == y, and -1 if x < y.


# # incremental development


# # suppose you want to find the distance between two points, given by the
# # coordinates (x1, y1) and (x2, y2). By the Pythagorean theorem, the distance is:

# # In this case, the inputs are two points, which you can represent using four numbers. The return value is the distance represented by a floating-point value. Immediately you can write an outline of the function:


# def distance(x1, y1, x2, y2):
#     return 0.0

# distance(1, 2, 4, 6)


# # step 2 find the difference b/w x2-x1 & y2-y1
# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     print('dx is', dx)
#     print('dy is', dy)
#     return 0.0


# distance(1, 2, 4, 6)

# # step 3 compute the sum of squares of dx and dy

# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquared = dx**2 + dy**2
#     print('dsquared is: ', dsquared)
#     return 0.0

# distance(1, 2, 4, 6)


# # step 3 use math.sqrt function to compute and return the result:

# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquared = dx**2 + dy**2
#     result = math.sqrt(dsquared)
#     return result


# print(distance(1, 2, 4, 6))


# #  a function that takes two points, the center of the circle and a point on the perimeter, and computes the area of the circleAssume that the center point is stored in the variables xc and yc, and the perimeter point is in xp and yp. The first step is to find the radius of the circle, which is the distance between the two points.  We just wrote a function, distance, that does that: radius = distance(xc, yc, xp, yp)


# radius = distance(xc, yc, xp, yp)

# result = area(radius)

# def circle_area(xc, yc, xp, yp):
#     radius = distance(xc, yc, xp, yp)
#     result = area(radius)
#     return result


# def circle_area(xc, yc, xp, yp):
#     return area(distance(xc, yc, xp, yp))


# def is_divisible(x, y):
#     if x % y == 0:
#     return True
#     else:
#     return False


# is_divisible(6, 4)
# is_divisible(6, 3)


# def is_divisible(x, y):
# return x % y == 0
# Boolean functions are often used in conditional statements:
# if is_divisible(x, y):
# print('x is divisible by y')
# It might be tempting to write something like:
# if is_divisible(x, y) == True:
# print('x is divisible by y')
# But the extra comparison is unnecessary.
# As an exercise, write a function is_between(x, y, z) that returns True if x  y  z or
# False otherwise.


# def factorial(n):
# if n == 0:
# return 1



# def factorial(n):
# if n == 0:
# return 1
# else:
# recurse = factorial(n-1)
# result = n * recurse
# return result

# # fibonacci

# def fibonacci(n):
# if n == 0:
# return 0
# elif n == 1:
# return 1
# else:
# return fibonacci(n-1) + fibonacci(n-2)


# def factorial(n):
# if not isinstance(n, int):
# print('Factorial is only defined for integers.')
# return None
# elif n < 0:
# print('Factorial is not defined for negative integers.')
# return None
# elif n == 0:
# return 1
# else:
# return n * factorial(n-1)

# print(factorial('fred'))

# print(factorial(-2))

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')





# # part 2
# # example 1

# a = "adamu labaran computer science student at uopeople"
# print(a)

# print(len(a))

# # the inbuilt function len() was used to check the length of character in variable "a"
# # output: 50

# print(a[:])

# # a[:] print the entire character in "a" variable
# #output: 'adamu labaran computer science student at uopeople'

# print(a[0:0])

# # return empty string 
# # output: ' '


# print(a[0])

# # this print first character in the string
# # output: 'a'

# print(a[49])

# # last character in the string
# # output:  'e'

# print(a[14:22])

# # this print 14 - 22 character in the string
# # 'computer'


# print(a[12:22:5])

# # return every 5th  character from 12 to 22
# # output: 'np'

# print(a[12:50:5])

# # return every 5th  character from 12 to 50
# # output: 'np nttup'

# print(a[0:50:5])

# # return every 5th  character from 0 to 50
# # output: 'a roei ete'

# print(a[0:50:3])

# # return every 3th  character from 0 to 50
# # output: 'a roei ete'

# # example 2

# b = 'welcome to python course'

# print(b[0:7])

# # return the first 7th character 
# # output: 'welcome'

# print(b[7:10])

# # Return from 7th to 10 character
# # output: ' to'

# print(b[10:17])

# # return from 10th to 17th character
# # output: ' python'

# print(b[17:24])

# # return 17th to 24th character
# # output: ' course'

# print(b[:24])

# # return everything
# # output:'welcome to python course'

# print(b[24:])

# # return empty string
# # output: ''


# print(b[10:24])

# # return 10th to 24 character
# # output: ' python course'

# # example 3
# c = 'python a programmin foundamental course at uopeople'


# print(c[ : -8])

# # The -8 corresponding to [n:-m] where the negative m-eth (-m) value return anticlockwise. in this case it return the n-eth value and delete the last value. 
# # output: 'python a programmin foundamental course at '

# print(c[-8:])

# # at the other hand the [-n:m] where the -n-eth count from last and the 8th most value which "uopeople"
# # output: 'uopeople'

# print(c[-19:])

# # -n-eth term return last most value
# # output: ' course at uopeople'

# print(c[:-19])
# # -m-eth return first value cut off last value 
# # output: 'python a programmin foundamental'


# epsilon = 0.00000000001

# def my_sqrt(a):
#     x =  a / 2
#     while True:
#         y = (x + a / x) / 2
#         if abs(y - x) < epsilon:
#             print(y)
#             return y
#             break
#         x = y
# my_sqrt(9)


# def right_digit(n):
#     trunc = f'{n:.11f}'
#     dig = trunc[len(trunc)-1]
#     print(dig)
#     return dig
# right_digit(9)


# def test_sqrt(n):
#     print('a', ' '*1, 'mysqrt(a)', ' '*3, 'math.sqrt(a)', 'diff')
#     print('_', ' '*1, '_'*9, ' '*3, '_'*12, ' ' + '_'*4)
    
#     for i in range(9):
#         x = i + 1
        
#         print(f'{x:0.1f}', end=' ')
        
#         if my_sqrt(x) - int(my_sqrt(x)) < 0.001:
#             y = 1
#         elif right_digit(my_sqrt(x)) == '0':
#             y = 0
#         else:
#             y = 11
            
#         print(f'{my_sqrt(x): < 13.{y}}', end=' ')
#         print(f'{my_sqrt(x): < 13.{y}}', end=' ')
        
#         diff = math.sqrt(x) - my_sqrt(x)
#         print(f'{diff:.12g}')
        
        
# test_sqrt(9)

# import math
# a  = 9
# x = 2
# def mysqrt(a):
#     x = a / 2
#     while True:
#         y = (x + a / x) / 2
#         if x - y < 0.00001:
#             break
#         x = y
#     print(y)
#     return y

# mysqrt(9)


# def diff(a):
#     d = mysqrt(a) - math.sqrt(a)
#     print(d)

# diff(9)


# def test_sqrt(a):
#     print(
#         'a', ' '*2,
#         'mysqrt(a)', ' '*11,
#         'math.sqrt(a)', ' '*8,
#         'diff'
#     )
#     while a > 1:
#         a = a-1
#         len_a = 3 - len(str(a))
#         len_my = 20 - len(str(mysqrt(a)))
#         len_ma = 20 - len(str(math.sqrt(a)))
#         print(
#             a, ' '* len_a,
#             mysqrt(a), ' '* len_my,
#             math.sqrt(a), ' '*len_ma,
#             diff(a)
#         )
#     return

# test_sqrt(10)


# a = 9
# x = 2
# while True:
#     print(x)
#     y = (x + a/x) / 2.0
#     if y == x:
#             break
#     x = y


# def my_sqrt(a):
#     x = a / 2
#     while True:
#         print(x)
#         y = (x + a / x) / 2.0
#         if y == x:
#             break
#         x = y
        
# my_sqrt(9)


# def find(word, letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1

# print(find("adamslabaran","a"))

# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

# word = 'banana'
# print(word.upper())

# new_word = word.upper()
# print(new_word)

# index = word.find('a')
# print(index)

# print(word.find('na', 3))

# def in_both(word1, word2):
#     for letter in word1:
#         if letter in word2:
#             print(letter)
            
            
# in_both('adams', 'labaran')
# in_both('apples', 'oranges')


# if word < 'banana':
#     print('Your word, ' + word + ', comes before banana.')
# elif word > 'banana':
#     print('Your word, ' + word + ', comes after banana.')
# else:
#     print('All right, bananas.')
    
    
# # def is_reverse(word1, word2):
# # if len(word1) != len(word2):
# # return False
# # i = 0
# # j = len(word2)
# # while j > 0:
# # if word1[i] != word2[j]:
# # return False
# # i = i+1
# # j = j-1
# # return 


# from decimal import *
# import math
# # this function compute square root of 9 using newton's method

# def my_sqrt(a):
#     x = 2
#     while True:
#         y = (x + a/x)/2
#         if x == y:
#             break
#         x = y
#     print(y)
#     return x

# # my_sqrt(9)

# # this function compute square root of 9 using math.sqrt()
# def math_sqrt(a):
#     x = math.sqrt(a)
#     print(x)
#     return x

# # math_sqrt(9)

# # this function compute the difference between the newton's method and math.sqrt()

# def diff(a):
#     p = my_sqrt(a)
#     q = math_sqrt(a)
#     d = p - q 
#     print(d)
#     return d
    
# # diff(9)


# # this function compute the table

# def test_square_root():
#     for a in range(1, 10):
#         print(float(a), " "*20, f"{my_sqrt(a)}", " "*20, f"{math_sqrt(a)}", " "*20, f"{diff(a)}")
#         # print('a', ' '*1, 'mysqrt(a)', ' '*3, 'math.sqrt(a)', 'diff')
#         # print('_', ' '*1, '_'*9, ' '*3, '_'*12, ' ' + '_'*4)
        
# test_square_root()


# def dec_1(a):
#     decOne = Decimal(my_sqrt(a))
#     # print(dec)
#     decTwo = round(decOne, 9)
#     print(decTwo)
#     return Decimal(decTwo)

# dec_1(9)


# def dec_2(a):
#     decOne = Decimal(math_sqrt(a))
#     # print(dec)
#     decTwo = round(decOne, 9)
#     print(decTwo)
#     return Decimal(decTwo)

# dec_2(9)


# def table():
#     for a in range(1, 10):
#         print(float(a), " "*20, f"{dec_2(a)}", " "*9, f"{dec_2(a)}", " "*9, f"{diff(a)}")
    
# table()


# from decimal import *
# import math

# def my_sqrt(a):
#     x = 2
#     while True:
#         y = (x + a/x)/2
#         if x == y:
#             break
#         x = y
#     print(y)
#     return x

# my_sqrt(9)


# # string sequence
# # len is a built-in function that returns the number of characters in a string:
# # To get the last letter of a string, you might be tempted to try something like this:
# # >>> length = len(fruit)
# # >>> last = fruit[length]

# # to print the last character of the string "banana"
# fruit = 'Banana'
# len(fruit)
# length = len(fruit)
# last = fruit[length - 1]

# print(last)

# names = 'adamu labaran'
# #  to print backward
# print(names[-1])
# print(names[-2])
# print(names[-3])
# print(names[-4])
# print(names[-5])
# print(names[-6])
# print(names[-7])
# print(names[-8])
# print(names[-9])

# index = 0
# while index < len(names):
#     letter = names[index]
#     print(names)
#     print(letter)
#     index+= 1
    
# fruit = 'Banana'
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index+= 1
    
# # As an exercise, write a function that takes a string as an argument and displays the letters backward, one per line.

# for letter in fruit:
#     print(letter)
    
    
    
    
# prefixes = 'JKLMNOPQ'
# suffix = 'ack'

# for letter in prefixes:
    
#     print(letter + suffix)
    


# # Of course, that’s not quite right because “Ouack” and “Quack” are misspelled. As an exercise, modify the program to fix this error.


# # string slicing

# s = 'adams labaran'
# print(s[0:5])
# print(s[6:12])


# print(fruit[3:3])
# print(fruit[:])


# # string immutability
# greeting = 'Hello, world!'
# new_greeting = 'J' + greeting[1:]
# print(new_greeting)
# # 'Jello, world!'

# def countdown(n):
#     while n > 0:
#         print(n)
#         n = n - 1
#     print('Blastoff!')
    
# countdown(4)


# def sequence(n):
#     while n != 1:
#         print(n)
#         if n % 2 == 0: # n is even
#             n = n / 2
#         else: # n is odd
#             n = n*3 + 1
            
# sequence(3)


# def print_n(s, n):
#     if n <= 0:
#         return
#     print(s)
#     print_n(s, n-1)
# print_n('adams', 4)
    
# def print_n(s, n):
#     while n <= 0:
#         print(n)
#         print_n(s, n-1)
#         n = n - 1
    
# print_n("Labaran", 5)

# a = 4
# x = 3
# while True:
#     print(x)
#     y = (x + a/x) / 2
#     if y == x:
#         break
#     x = y
    
    
    
#     # >>> a = 4
# # >>> x = 3
# # >>> y = (x + a/x) / 2
# # >>> y
# # 2.16666666667
# # >>> x = y
# # >>> y = (x + a/x) / 2
# # >>> y
# # 2.00641025641

# # >>> x = y
# # >>> y = (x + a/x) / 2
# # >>> y
# # 2.00641025641
# # After a few more updates, the estimate is almost exact:
# # >>> x = y
# # >>> y = (x + a/x) / 2
# # >>> y
# # 2.00001024003
# # >>> x = y
# # >>> y = (x + a/x) / 2
# # >>> y
# # 2.00000000003
# # In general we don’t know ahead of time how many steps it takes to get to the right answer,
# # but we know when we get there because the estimate stops changing:
# # >>> x = y
# # >>> y = (x + a/x) / 2
# # >>> y
# # 2.0
# # >>> x = y
# # >>> y = (x + a/x) / 2
# # >>> y
# # 2.0

# # As an exercise, modify find so that it has a third parameter, the index in word where it should start looking.
# # With well-chosen variable names, Python sometimes reads like English. You could read
# # this loop, “for (each) letter in (the first) word, if (the) letter (appears) in (the second) word,
# # print (the) letter.”

# # for loop is based on the sequence, while loop is based on the condition



# # def any_lowercase1(s):
# # for c in s:
# # if c.islower():
# # return True
# # else:
# # return False
# # def any_lowercase2(s):
# # for c in s:
# # if 'c'.islower():
# # return 'True'
# # else:
# # return 'False'
# # def any_lowercase3(s):
# # for c in s:
# # flag = c.islower()
# # return flag
# # def any_lowercase4(s):
# # flag = False
# # for c in s:
# # flag = flag or c.islower()
# # return flag
# # def any_lowercase5(s):
# # for c in s:
# # if not c.islower():
# # return False
# # return True


# # Topics
# # List features
# # Traversing lists
# # List operations and methods
# # List slices
# # Map, filter, and reduce
# # Deleting list elements
# # Objects, values, and aliasing
# # Lists as function arguments


# # Discussion Assignment
# # Welcome to the Unit 6 Discussion Forum!

# # Use the terms "equivalent" and "identical" to distinguish between objects and values. Illustrate the difference further using your own examples with Python lists and the “is” operator.  

# # Using your own Python list examples, explain how objects, references, and aliasing relate to one another.

# # Finally, create your own example of a function that modifies a list passed in as an argument. Hence, describe what your function does in terms of arguments, parameters, objects, and references. 

# # Create your own unique examples for this assignment. Do not copy them from the textbook or any other source.


# # The code and its output must be explained technically whenever asked. The explanation can be provided before or after the code, or in the form of code comments within the code. For any descriptive type question, Your answer must be at least 150 words.


# # Use the terms "equivalent" and "identical" to distinguish between objects and values. Illustrate the difference further using your own examples with Python lists and the “is” operator.  
# # A value is what an object holds “smallest unit of data that a program manipulates”. (Downey, 2015). The ‘is’ keyword is used for identity; it checks if two different objects are identical. If the objects are identical, the interpreter returns True.
# # >>> str1 = 'xyz' 
# # >>> str2 = 'xyz' 
# # >>> str1 is str2
# # True
# # >>>  
# # However, in python list if different variables refer to the same objects, they are not identical but equivalents (Downey, 2015). If the ‘is’ operator is used in this case, the python interpreter returns False.
# # >>> lst1 = ['x', 'y', 'z']
# # >>> lst2 = ['x', 'y', 'z'] 
# # >>> lst1 is lst2
# # False
# # >>>  
# # When two different objects have the same value object1 is identical to object2. When using ‘==’ operator to check if obj1 is identical to obj2 the interpreter returns True.
# # False
# # >>> obj1 = [1, 2, 3] 
# # >>> obj2 = [1, 2, 3] 
# # >>> obj1 == obj2
# # True
# # >>>
# # However, it is equivalence when obj1 is assign to obj3.
# # >>> obj3 = obj1
# # >>> obj1 is obj3
# # True
# # >>># in this scenario when obj3 is updated obj1 will automatically be updated.
# # >>> obj3.append(4)
# # >>> obj1
# # [1, 2, 3, 4]
# # >>> obj3
# # [1, 2, 3, 4]
# # >>>because obj1 and obj3 are equivalent in terms of id and memory location.
# # >>> print(id(obj1), '|', id(obj3))
# # 2174340844352 | 2174340844352
# # >>>
# # # Using your own Python list examples, explain how objects, references, and aliasing relate to one another.
# # When the value of obj1 is assign to another variable (obj3), then both variables are referred to as the same object. Thus, “the association of both variables with an object is called reference” (Downey, 2015).
# # >>> obj3 = obj1
# # >>> obj1 is obj3
# # True
# #  Aliasing occur when two or more different variables are reference to the same memory location.
# # >>> x = [1, 2, 3]
# # >>> y = x
# # >>> y
# # [1, 2, 3]
# # >>> z = y
# # >>> z
# # [1, 2, 3]
# # >>> # x, y, z are aliased to one another, when z is modified x and will also be affected.
# # >>> z.append([4,5]) 
# # >>> y[0] = ['adams'] 
# # >>> x
# # [['adams'], 2, 3, [4, 5]]
# # >>> y
# # [['adams'], 2, 3, [4, 5]]
# # >>> z
# # [['adams'], 2, 3, [4, 5]]
# # >>>  


# # # Finally, create your own example of a function that modifies a list passed in as an argument. Hence, describe what your function does in terms of arguments, parameters, objects, and references.
# # >>>
# # >>> def names(name):
# # ...     x = 'adams'
# # ...     myname = []
# # ...     for name in x:
# # ...             myname.append(name)
# # ...             print(myname)
# # ... 
# # >>> # for loop iterate through ‘x’ and stored in a variable ‘name’, then myname.append(name) received value from iterated ‘name’ which stored in an ‘empty’ list variable ‘myname’
# # >>> names(myname) 
# # ['a']
# # ['a', 'd']
# # ['a', 'd', 'a']
# # ['a', 'd', 'a', 'm']
# # ['a', 'd', 'a', 'm', 's'] 
# # >>> # at the other hand ‘name’ can be declared globally as in
# # >>> name = ‘adamu’
# # >>> names(name)
# # ['a']
# # ['a', 'd']
# # ['a', 'd', 'a']
# # ['a', 'd', 'a', 'm']
# # ['a', 'd', 'a', 'm', 's'] 
# # >>> # ourname is referenced to ‘name’, below the argument changed from ‘name’ to ‘ourname’ 
# # >>> ourname = name
# # >>> names(ourname)
# # ['a']
# # ['a', 'd']
# # ['a', 'd', 'a']
# # ['a', 'd', 'a', 'm']
# # ['a', 'd', 'a', 'm', 's']

# # Reference: 
# # Downey, A. (2015). Think python: How to think like a computer scientist. (2nd. Ed.). Green Tea press





# # PS C:\Users\LENOVO YOGA 11E\Documents\code-factory-> python
# # Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
# # Type "help", "copyright", "credits" or "license" for more information.
# # >>> fav_food = 'danwake dambu kallaba kwado waina kosai alale taliya dambunNama paroparo awara doyaDaKwai'
# # >>> # typecasting the string into list
# # >>> 
# # >>> my_fav_food = list(fav_food)
# # >>> fav_food
# # 'danwake dambu kallaba kwado waina kosai alale taliya dambunNama paroparo awara doyaDaKwai'
# # >>> my_fav_food
# # ['d', 'a', 'n', 'w', 'a', 'k', 'e', ' ', 'd', 'a', 'm', 'b', 'u', ' ', 'k', 'a', 'l', 'l', 'a', 'b', 'a', ' ', 'k', 'w', 'a', 'd', 'o', ' ', 'w', 'a', 'i', 'n', 'a', ' ', 'k', 'o', 's', 'a', 'i', ' ', 'a', 'l', 'a', 'l', 'e', ' ', 't', 'a', 'l', 'i', 'y', 'a', ' ', 'd', 'a', 'm', 'b', 'u', 'n', 'N', 'a', 'm', 'a', ' ', 'p', 'a', 'r', 'o', 'p', 'a', 'r', 'o', ' ', 'a', 'w', 'a', 'r', 'a', ' ', 'd', 'o', 'y', 'a', 'D', 'a', 'K', 'w', 'a', 'i']
# # >>> fav_food.split()
# # ['danwake', 'dambu', 'kallaba', 'kwado', 'waina', 'kosai', 'alale', 'taliya', 'dambunNama', 'paroparo', 'awara', 'doyaDaKwai']
# # >>> fav_food.pop(0)
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # AttributeError: 'str' object has no attribute 'pop'
# # >>> my_fav_food = fav_food.split()
# # >>> my_fav_food
# # ['danwake', 'dambu', 'kallaba', 'kwado', 'waina', 'kosai', 'alale', 'taliya', 'dambunNama', 'paroparo', 'awara', 'doyaDaKwai']
# # >>> my_fav_food
# # ['danwake', 'dambu', 'kallaba', 'kwado', 'waina', 'kosai', 'alale', 'taliya', 'dambunNama', 'paroparo', 'awara', 'doyaDaKwai']
# # >>> my_fav_food.pop(0)
# # 'danwake'
# # >>> my_fav_food       
# # ['dambu', 'kallaba', 'kwado', 'waina', 'kosai', 'alale', 'taliya', 'dambunNama', 'paroparo', 'awara', 'doyaDaKwai']
# # >>> my_fav_food.pop()
# # 'doyaDaKwai'
# # >>> my_fav_food      
# # ['dambu', 'kallaba', 'kwado', 'waina', 'kosai', 'alale', 'taliya', 'dambunNama', 'paroparo', 'awara']
# # >>> my_fav_food.pop(6) 
# # 'taliya'
# # >>> my_fav_food       
# # ['dambu', 'kallaba', 'kwado', 'waina', 'kosai', 'alale', 'dambunNama', 'paroparo', 'awara']
# # >>> # using index and del operator
# # >>> 
# # >>> del my_fav_food[4] 
# # >>> my_fav_food
# # ['dambu', 'kallaba', 'kwado', 'waina', 'alale', 'dambunNama', 'paroparo', 'awara']
# # >>> # using index 0 throgh n-1 with del operetor
# # >>> del my_fav_food[0:4]
# # >>> my_fav_food
# # ['alale', 'dambunNama', 'paroparo', 'awara']
# # >>> my_fav_food.remove('paroparo') 
# # >>> my_fav_food                   
# # ['alale', 'dambunNama', 'awara']
# # >>> my_fav_food.sort()
# # >>> my_fav_food       
# # ['alale', 'awara', 'dambunNama']
# # >>> my_fav_food.append('rice', 'beans', 'suya') 
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # TypeError: list.append() takes exactly one argument (3 given)
# # >>> my_fav_food.append('rice')                 
# # >>> my_fav_food               
# # ['alale', 'awara', 'dambunNama', 'rice']
# # >>> my_fav_food.add('suya')
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # AttributeError: 'list' object has no attribute 'add'
# # >>> my_fav_foods = my_fav_Food + fav_food
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # NameError: name 'my_fav_Food' is not defined. Did you mean: 'my_fav_food'?
# # >>> my_fav_foods = my_fav_food + fav_food 
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # TypeError: can only concatenate list (not "str") to list

# # >>> 
# # >>> my_fav_food
# # ['alale', 'awara', 'dambunNama', 'rice']
# # >>> my_fav_food.insert(0, 'chicken')
# # >>> my_fav_food                     
# # ['chicken', 'alale', 'awara', 'dambunNama', 'rice']
# # >>> my_fav_food.insert(5, 'burgger') 
# # >>> my_fav_food                     
# # ['chicken', 'alale', 'awara', 'dambunNama', 'rice', 'burgger']
# # >>> my_fav_food.append(fav_food)
# # >>> my_fav_food
# # ['chicken', 'alale', 'awara', 'dambunNama', 'rice', 'burgger', 'danwake dambu kallaba kwado waina kosai alale taliya dambunNama paroparo awara doyaDaKwai']
# # >>> my_fav_food.extend('shawarma')
# # >>> my_fav_food                   
# # ['chicken', 'alale', 'awara', 'dambunNama', 'rice', 'burgger', 'danwake dambu kallaba kwado waina kosai alale taliya dambunNama paroparo awara doyaDaKwai', 's', 'h', 'a', 'w', 'a', 'r', 'm', 'a']
# # >>> my_fav_food.extend(fav_food)
# # >>> my_fav_food                 
# # ['chicken', 'alale', 'awara', 'dambunNama', 'rice', 'burgger', 'danwake dambu kallaba kwado waina kosai alale taliya dambunNama paroparo awara doyaDaKwai', 's', 'h', 'a', 'w', 'a', 'r', 'm', 'a', 'd', 'a', 'n', 'w', 'a', 'k', 'e', ' ', 'd', 'a', 'm', 'b', 'u', ' ', 'k', 'a', 'l', 'l', 'a', 'b', 'a', ' ', 'k', 'w', 'a', 'd', 'o', ' ', 'w', 'a', 'i', 'n', 'a', ' ', 'k', 'o', 's', 'a', 'i', ' ', 'a', 'l', 'a', 'l', 'e', ' ', 't', 'a', 'l', 'i', 'y', 'a', ' ', 'd', 'a', 'm', 'b', 'u', 'n', 'N', 'a', 'm', 'a', ' ', 'p', 'a', 'r', 'o', 'p', 'a', 'r', 'o', ' ', 'a', 'w', 'a', 'r', 'a', ' ', 'd', 'o', 'y', 'a', 'D', 'a', 'K', 'w', 'a', 'i']
# # >>> my_fav_food.reverse()
# # >>> my_fav_food          
# # ['i', 'a', 'w', 'K', 'a', 'D', 'a', 'y', 'o', 'd', ' ', 'a', 'r', 'a', 'w', 'a', ' ', 'o', 'r', 'a', 'p', 'o', 'r', 'a', 'p', ' ', 'a', 'm', 'a', 'N', 'n', 'u', 'b', 'm', 'a', 'd', ' ', 'a', 'y', 'i', 'l', 'a', 't', ' ', 'e', 'l', 'a', 'l', 'a', ' ', 'i', 'a', 's', 'o', 'k', ' ', 'a', 'n', 'i', 'a', 'w', ' ', 'o', 'd', 'a', 'w', 'k', ' ', 'a', 'b', 'a', 'l', 'l', 'a', 'k', ' ', 'u', 'b', 'm', 'a', 'd', ' ', 'e', 'k', 'a', 'w', 'n', 'a', 'd', 'a', 'm', 'r', 'a', 'w', 'a', 'h', 's', 'danwake dambu kallaba kwado waina kosai alale taliya dambunNama paroparo awara doyaDaKwai', 'burgger', 'rice', 'dambunNama', 'awara', 'alale', 'chicken']
# # >>> delimiter = ' '
# # >>> fav_food = delimiter.join(my_fav_food)
# # >>> my_fav_food
# # ['i', 'a', 'w', 'K', 'a', 'D', 'a', 'y', 'o', 'd', ' ', 'a', 'r', 'a', 'w', 'a', ' ', 'o', 'r', 'a', 'p', 'o', 'r', 'a', 'p', ' ', 'a', 'm', 'a', 'N', 'n', 'u', 'b', 'm', 'a', 'd', ' ', 'a', 'y', 'i', 'l', 'a', 't', ' ', 'e', 'l', 'a', 'l', 'a', ' ', 'i', 'a', 's', 'o', 'k', ' ', 'a', 'n', 'i', 'a', 'w', ' ', 'o', 'd', 'a', 'w', 'k', ' ', 'a', 'b', 'a', 'l', 'l', 'a', 'k', ' ', 'u', 'b', 'm', 'a', 'd', ' ', 'e', 'k', 'a', 'w', 'n', 'a', 'd', 'a', 'm', 'r', 'a', 'w', 'a', 'h', 's', 'danwake dambu kallaba kwado waina kosai alale taliya dambunNama paroparo awara doyaDaKwai', 'burgger', 'rice', 'dambunNama', 'awara', 'alale', 'chicken']
# # >>> print(my_fav_food)
# # ['i', 'a', 'w', 'K', 'a', 'D', 'a', 'y', 'o', 'd', ' ', 'a', 'r', 'a', 'w', 'a', ' ', 'o', 'r', 'a', 'p', 'o', 'r', 'a', 'p', ' ', 'a', 'm', 'a', 'N', 'n', 'u', 'b', 'm', 'a', 'd', ' ', 'a', 'y', 'i', 'l', 'a', 't', ' ', 'e', 'l', 'a', 'l', 'a', ' ', 'i', 'a', 's', 'o', 'k', ' ', 'a', 'n', 'i', 'a', 'w', ' ', 'o', 'd', 'a', 'w', 'k', ' ', 'a', 'b', 'a', 'l', 'l', 'a', 'k', ' ', 'u', 'b', 'm', 'a', 'd', ' ', 'e', 'k', 'a', 'w', 'n', 'a', 'd', 'a', 'm', 'r', 'a', 'w', 'a', 'h', 's', 'danwake dambu kallaba kwado waina kosai alale taliya dambunNama paroparo awara doyaDaKwai', 'burgger', 'rice', 'dambunNama', 'awara', 'alale', 'chicken']
# # >>>   

# # element from a list:
# # def delete_head(t):
# # del t[0]
# # Here’s how it is used:
# # >>> letters = ['a', 'b', 'c']
# # >>> delete_head(letters)
# # >>> letters
# # ['b', 'c']cheeses = ['Cheddar', 'Edam', 'Gouda']
# numbers = [42, 123]
# empty = []
# print(cheeses, numbers, empty)
# # ['Cheddar', 'Edam', 'Gouda'] [42, 123] []

# for cheese in cheeses:
#     print(cheese)
    
#     # tranversing a list
    
#     for i in range(len(numbers)):
#         numbers[i] = numbers[i] * 2
#         print(numbers)
        
#     # nested list
    
# nested_list = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]

# # list operators
# # >>> a = [1, 2, 3]
# # >>> b = [4, 5, 6]
# # >>> c = a + b
# # >>> c
# # [1, 2, 3, 4, 5, 6]
# # The * operator repeats a list a given number of times:
# # >>> [0] * 4
# # [0, 0, 0, 0]
# # >>> [1, 2, 3] * 3
# # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# # The first example repeats [0] four times. The second example repeats the list [1, 2, 3]
# # three times.


# # list slices, append, extend, sort, sum, pop, del, remove 

# t = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# t.append('h')
# print(t)

# a = [1, 2, 3, 4, 5]
# b = sum(a)

# print(b)

# # map, filter and reduce
# t = [2,3,4]
# def add_all(t):
#     total = 0
#     for x in t:
#         total += x
#         return total
        
# def capitalize_all(t):
#     res = []
#     for s in t:
#         res.append(s.capitalize())
#         return res

# def only_upper(t):
#     res = []
#     for s in t:
#         if s.isupper():
#                 res.append(s)
#                 return res
            
# # list and string, delimeter, join, split, join, typecasting of list
# x = 'spam'
# y = list(x)
# print(y)

# s = 'adamu-labaran-salma-usman'
# delimiter = '-'
# t = s.split(delimiter)
# print(t)



# # join
# t = ['pining', 'for', 'the', 'fjords']
# delimiter = ' '
# s = delimiter.join(t)
# print(s)

# # object and vallue, 
# # 
# # aliasing => An object with more than one reference has more than one name, so we say that the object is aliased


# def delete_head(t):
#     del t[0]

# letters = ['a', 'b', 'c']
# delete_head(letters)
# print(letters)





# # 3. Make copies to avoid aliasing.
# # If you want to use a method like sort that modifies the argument, but you need to
# # keep the original list as well, you can make a copy.
# # >>> t = [3, 1, 2]
# # >>> t2 = t[:]
# # >>> t2.sort()
# # >>> t
# # [3, 1, 2]
# # >>> t2
# # [1, 2, 3]

# # >>> t2 = sorted(t)
# # >>> t
# # [3, 1, 2]
# # >>> t2
# # [1, 2, 3]

# # Topics
# # List features
# # Traversing lists
# # List operations and methods
# # List slices
# # Map, filter, and reduce
# # Deleting list elements
# # Objects, values, and aliasing
# # Lists as function arguments


# # Discussion Assignment
# # Welcome to the Unit 6 Discussion Forum!

# # Use the terms "equivalent" and "identical" to distinguish between objects and values. Illustrate the difference further using your own examples with Python lists and the “is” operator.  

# # Using your own Python list examples, explain how objects, references, and aliasing relate to one another.

# # Finally, create your own example of a function that modifies a list passed in as an argument. Hence, describe what your function does in terms of arguments, parameters, objects, and references. 

# # Create your own unique examples for this assignment. Do not copy them from the textbook or any other source.


# # The code and its output must be explained technically whenever asked. The explanation can be provided before or after the code, or in the form of code comments within the code. For any descriptive type question, Your answer must be at least 150 words.


# # Use the terms "equivalent" and "identical" to distinguish between objects and values. Illustrate the difference further using your own examples with Python lists and the “is” operator.  
# # A value is what an object holds “smallest unit of data that a program manipulates”. (Downey, 2015). The ‘is’ keyword is used for identity; it checks if two different objects are identical. If the objects are identical, the interpreter returns True.
# # >>> str1 = 'xyz' 
# # >>> str2 = 'xyz' 
# # >>> str1 is str2
# # True
# # >>>  
# # However, in python list if different variables refer to the same objects, they are not identical but equivalents (Downey, 2015). If the ‘is’ operator is used in this case, the python interpreter returns False.
# # >>> lst1 = ['x', 'y', 'z']
# # >>> lst2 = ['x', 'y', 'z'] 
# # >>> lst1 is lst2
# # False
# # >>>  
# # When two different objects have the same value object1 is identical to object2. When using ‘==’ operator to check if obj1 is identical to obj2 the interpreter returns True.
# # False
# # >>> obj1 = [1, 2, 3] 
# # >>> obj2 = [1, 2, 3] 
# # >>> obj1 == obj2
# # True
# # >>>
# # However, it is equivalence when obj1 is assign to obj3.
# # >>> obj3 = obj1
# # >>> obj1 is obj3
# # True
# # >>># in this scenario when obj3 is updated obj1 will automatically be updated.
# # >>> obj3.append(4)
# # >>> obj1
# # [1, 2, 3, 4]
# # >>> obj3
# # [1, 2, 3, 4]
# # >>>because obj1 and obj3 are equivalent in terms of id and memory location.
# # >>> print(id(obj1), '|', id(obj3))
# # 2174340844352 | 2174340844352
# # >>>
# # # Using your own Python list examples, explain how objects, references, and aliasing relate to one another.
# # When the value of obj1 is assign to another variable (obj3), then both variables are referred to as the same object. Thus, “the association of both variables with an object is called reference” (Downey, 2015).
# # >>> obj3 = obj1
# # >>> obj1 is obj3
# # True
# #  Aliasing occur when two or more different variables are reference to the same memory location.
# # >>> x = [1, 2, 3]
# # >>> y = x
# # >>> y
# # [1, 2, 3]
# # >>> z = y
# # >>> z
# # [1, 2, 3]
# # >>> # x, y, z are aliased to one another, when z is modified x and will also be affected.
# # >>> z.append([4,5]) 
# # >>> y[0] = ['adams'] 
# # >>> x
# # [['adams'], 2, 3, [4, 5]]
# # >>> y
# # [['adams'], 2, 3, [4, 5]]
# # >>> z
# # [['adams'], 2, 3, [4, 5]]
# # >>>  


# # # Finally, create your own example of a function that modifies a list passed in as an argument. Hence, describe what your function does in terms of arguments, parameters, objects, and references.
# # >>>
# # >>> def names(name):
# # ...     x = 'adams'
# # ...     myname = []
# # ...     for name in x:
# # ...             myname.append(name)
# # ...             print(myname)
# # ... 
# # >>> # for loop iterate through ‘x’ and stored in a variable ‘name’, then myname.append(name) received value from iterated ‘name’ which stored in an ‘empty’ list variable ‘myname’
# # >>> names(myname) 
# # ['a']
# # ['a', 'd']
# # ['a', 'd', 'a']
# # ['a', 'd', 'a', 'm']
# # ['a', 'd', 'a', 'm', 's'] 
# # >>> # at the other hand ‘name’ can be declared globally as in
# # >>> name = ‘adamu’
# # >>> names(name)
# # ['a']
# # ['a', 'd']
# # ['a', 'd', 'a']
# # ['a', 'd', 'a', 'm']
# # ['a', 'd', 'a', 'm', 's'] 
# # >>> # ourname is referenced to ‘name’, below the argument changed from ‘name’ to ‘ourname’ 
# # >>> ourname = name
# # >>> names(ourname)
# # ['a']
# # ['a', 'd']
# # ['a', 'd', 'a']
# # ['a', 'd', 'a', 'm']
# # ['a', 'd', 'a', 'm', 's']

# # Reference: 
# # Downey, A. (2015). Think python: How to think like a computer scientist. (2nd. Ed.). Green Tea press


# # Part 1
# # Write a Python program that does the following. 

# # Construct a string that is a long series of words separated by spaces. The string is your own creative choice. It can be names, favorite foods, animals, anything. Just make it up yourself. Do not copy the string from another source. 
# fav_food = 'danwake dambu kallaba kwado waina kosai alale taliya dambunNama paroparo awara doyaDaKwai'

# # Turn the string into a list of words using split.

# my_fav_food = fav_food.split()
# print(my_fav_food)

# # ['danwake', 'dambu', 'kallaba', 'kwado', 'waina', 'kosai', 'alale', 'taliya', 'dambunNama', 'paroparo', 'awara', 'doyaDaKwai']


# # Delete three words from the list, but delete each one using a different kind of Python operation. 

# # Sort the list. 
# # Add new words to the list (three or more) using three different kinds of Python operations. 
# # Turn the list of words back into a single string using join. 
# # Print the string. 

# # Part 2
# # Provide your own examples of the following using Python lists. Do not copy them from another source. 

# # Nested lists 
# # The “*” operator 
# # List slices 
# # The “+=” operator 
# # A list filter 
# # A list operation that is legal but does the "wrong" thing, and not what the programmer expects 
# # Provide the Python code and output for your program and all your examples. 


# def only_upper(t):
#     res = []
#     for s in t:
#         if s.isupper():
#             res.append(s)
#         return res

# only_upper('adamu Labaran')

# print(list(filter((lambda x: x > 0), range(-5, 5))))

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_nums = list(filter(lambda x: x % 2==0, nums))
# print(even_nums)

# nums2 = [1, 2, 3, 4, 5, 6, 7, 8]
# sieve = [3, 5, 7, 8]
# ans = list(filter(lambda x: x not in sieve, nums2))
# print(ans)


# def c():
#     nums4 = [1, 2, 3, 4,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#     for even_num in filter(lambda x: x % 2 == 0, nums4):
#         print(even_num)

# c()

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, -6, -7, -8]

# a[2] = 'adams'
# print(a)

# a[0] = 26
# print(a)

# a[4] = ['adamu', 'labaran', 26, 2.6, -7]
# print(a)

# b = a       # b is equivalent to a
# print(b)

# c = a[:]       # c is identical to a
# print(c)

# a.append('salma usman')  #as a is appended so also b but not c cos a copy of a (identical) but not equavelent to a
# print(a)
# print(b)
# print(c)


# # list for loop (range())
# range(6)
# range(25)
# range(26)
# range(0, 8, 2) #start from 0 up to 8-1 but each num incremented by 2
# range(3, 31, 3) # same as above

# for i in range(26):
#     print(i)

# lst = ['adams', 'labaran', 'salma', 'usman']
# food = ['milk', 'eggs','bread']
# food.append('chocolate')
# print(food)

# # to change the index
# food[3] = 'sugar'
# print(food)

# # the 'in' operator is list
# 'milk' in food  # this is true
# 'suya' in food # this is false bcos suya doesnt exist


# # tranversing a list: this is used to modify or used to write or update a list built_in function (range) is used 
# names = ['adamu', 'labaran', 'salma', 'usman', 'abeh', 'musty', 'umar']
# for name in names:
#     print(name)


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2.3, 3.5, 6.8]
# print(f"the lenght of nums is: {len(nums)}")

# for num in range(len(nums)):
#     nums[num]*=2
#     print(nums)
#     # print(num)


# # nested list
# lst1 = ['add', 'sub', 'mult', 'div',['adams']]
# lst1.append(['math']) # this return None why?  find out more
# print(lst1)


# # list operation the + operator concatenate list, * repeat list in a given number of value
# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9]
# c = a + b   # addition of a list
# print(c)


# a = [1, 2, 3, 4, 5] * 3 # list multiplication: 12345 repeats three times
# b = [6, 7, 8, 9] * 3 # list multiplication: 6789 repeats three time
# c = a + b  # conctenating list multiplication: 12345 repest three times, 6789 threee times
# print(a)
# print(b)
# print(c)


# #  lsit slices
# t  = ['a', 'b', 'c', 'd', 'e', 'f']
# print(t[3])
# print(t[:3])
# print(t[3:])
# print(t[1:2]) # return from 1 up to two
# print(t[2:4]) # return from 2 up to 4
# print(t[2:2]) # return nothing


# # updating a slice
# t[0:2] = ['x', 'y']
# print(t)

# t = [1, 3, 4, 5, 6]
# def capitalize_all(t):
#     res = []
#     for s in t:
#         res.append(s.capitalize())
#         return res


# def only_upper(t):
#     res = []
#     for s in t:
#         if s.isupper():
#             res.append(s)
#         return res



# # Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
# # Type "help", "copyright", "credits" or "license" for more information.
# # >>> # tupple loop over dictionary. tranversing throgh dictionary ".items()" method can be use to return tuple then looping further to access dictionary elements. which is not accessable in dictionary tranversal method.
# # >>> dtn = { 'first_name' : 'adamu', 'last_name' : 'labaran', 'age' : 26, 'city' : 'keffi'}
# # >>> type(dtn)
# # <class 'dict'>
# # >>>
# # >>>
# # >>> tup = list(dtn.items())
# # >>> tup
# # [('first_name', 'adamu'), ('last_name', 'labaran'), ('age', 26), ('city', 'keffi')]
# # >>>
# # >>> type(tup)  #the  return type here is list
# # <class 'list'>
# # >>> type(tup[2]) # in accessing the index of tup the return type is tuple
# # <class 'tuple'>
# # >>>
# # >>>
# # >>> # looping through dictionary with ".items()" method
# # >>> for x, y in dtn.items():
# # ...     print(x, y)
# # ...
# # first_name adamu
# # last_name labaran
# # age 26
# # city keffi
# # >>>



# # >>> # two list can tranverse together with "zip" function, then loop throgh list of turple
# # >>> p = ['adamu', 'labaran', 'salma', 'usman']
# # >>> q = [26, 70, 16, 60]
# # >>>
# # >>>
# # >>> r = list(zip(p, q))
# # >>> r
# # [('adamu', 26), ('labaran', 70), ('salma', 16), ('usman', 60)]
# # >>>
# # >>> type(r)
# # <class 'list'>
# # >>> zip(p, q)
# # <zip object at 0x0000011FF39FFD80>
# # >>> type(zip(p, q))
# # <class 'zip'>
# # >>>
# # >>> # looping throgh zip items
# # >>> for x, y in r:
# # ...     print(x, y)
# # ...
# # adamu 26
# # labaran 70
# # salma 16
# # usman 60
# # >>>



# # >>> # looping through turple with enumerate function
# # >>> s = ['adamu', 'labaran', 'salma', 'usman']
# # >>> for i, s in enumerate(s, start = 1):
# # ...     print(i, s)
# # ...
# # 1 adamu
# # 2 labaran
# # 3 salma
# # 4 usman
# # >>>
# # >>>
# # >>> # enumerate will loop through i by assigning a serial number to it
# # >>>


# alphabet = "abcdefghijklmnopqrstuvwxyz"

# test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"]

# test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]

# def histogram(s):
#      d = dict()
#      for c in s:
#           if c not in d:
#                d[c] = 1
#           else:
#                d[c] += 1
#      return d

# # boolean string that has repeated characters.
# print("boolean string that has repeated characters.")
# def has_duplicates(s):
#     for x in histogram(s).values():
#         if x > 1:
#             return True
#         else:
#             return False

# def test_doops():
#     for s in test_dups:
#         print(s + ':', has_duplicates(s))

# test_doops()

# # return has duplicates or not
# print("\n\nreturn has duplicates or not\n")

# def has_duplicates(s):
#     dtn = histogram(s)
#     for key, value in dtn.items():
#         if value > 1:
#                 return True
#         else:
#                 return False
# # iterating through test_dups to check for duplicates           
# for x in test_dups:
#     if has_duplicates(x):
#         print(x, 'has duplicates')
#         print('_'*40)
#     else:
#         print(x, 'has no duplicates')
#         print('_'*40)

# # part 2
# # missing letter
# def missing_letters(s):
#     msl = []
#     dtn = histogram(s)
#     for letter in alphabet:
#         if letter not in dtn:
#             msl.append(letter)
#     msl.sort()
#     return ''.join(msl)

# #iterating through test_miss to check for missing letter
# for x in test_miss:
#     s = missing_letters(x.replace(' ', ''))
#     if s!= '':
#         print('\n', x, 'is missing letter', s)
#         print('_'*50)
#     else:
#         print('\n', x, 'uses all the letters')
#         print('_'*65)


# Implement your own Python code examples to describe how tuples can be useful with loops over lists and dictionaries. Do not copy code from the textbook or any other source. 

# Your descriptions and examples should include: the zip function, the enumerate function, and the items method. 

# The code and its output must be explained technically whenever asked. The explanation can be provided before or after the code, or in the form of code comments within the code. For any descriptive type question, Your answer must be at least 150 words.

# solution:
# tupple loop over dictionary. tranversing throgh dictionary ".items()" method can be use to return tuple then looping further to access dictionary elements. which is not accessable in dictionary tranversal method.

dtn = { 'first_name' : 'adamu', 'last_name' : 'labaran', 'age' : 26, 'city' : 'keffi'}
print(type(dtn))


#  the dtn is typecasts in two forms tuple and list
tup = list(dtn.items())
print(type(tup))  #the  return type here is list

print(type(tup[2])) # in accessing the index of tup the return type is tuple
print(tup)

# looping through dictionary with ".items()" method
for x, y in dtn.items():
    print(x, y)


# two list can tranverse together with "zip" function, then loop throgh list of turple
p = ['adamu', 'labaran', 'salma', 'usman']
q = [26, 70, 16, 60]

r = list(zip(p, q))
print(r)


for x, y in r:
    print(x, y)



# looping through turple with enumerate function

s = ['adamu', 'labaran', 'salma', 'usman']
for i, s in enumerate(s, start = 1):
    print(i, s)




# Implement your own Python code examples to describe how tuples can be useful with loops over lists and dictionaries. Do not copy code from the textbook or any other source. 

# Your descriptions and examples should include: the zip function, the enumerate function, and the items method. 

# The code and its output must be explained technically whenever asked. The explanation can be provided before or after the code, or in the form of code comments within the code. For any descriptive type question, Your answer must be at least 150 words.

# solution:
# tupple loop over dictionary. tranversing throgh dictionary ".items()" method can be use to return tuple then looping further to access dictionary elements. which is not accessable in dictionary tranversal method.
 
dtn = { 'first_name' : 'adamu', 'last_name' : 'labaran', 'age' : 26, 'city' : 'keffi'}
print(type(dtn))


#  the dtn is typecasts in two forms tuple and list
tup = list(dtn.items())
print(type(tup))  #the  return type here is list

print(type(tup[2])) # in accessing the index of tup the return type is tuple
print(tup)

# looping through dictionary with ".items()" method
for x, y in dtn.items():
    print(x, y)


# two list can tranverse together with "zip" function, then loop throgh list of turple
p = ['adamu', 'labaran', 'salma', 'usman']
q = [26, 70, 16, 60]

r = list(zip(p, q))
print(r)


for x, y in r:
    print(x, y)



# looping through turple with enumerate function

s = ['adamu', 'labaran', 'salma', 'usman']
for i, s in enumerate(s, start = 1):
    print(i, s)


