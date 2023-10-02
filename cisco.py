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

