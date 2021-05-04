# Notes:
# Self-explanations included above each line.
#
# Used float() parameter to ensure all relevent numbers return as floating
# point numbers.
# 
# Mistake 1 - Closed bracket after "Roosters" before equation could execute,
# rendering program unable to run.
#
# Mistake 2 - Forgot , after "Is it greater or equal?": syntax error encountered
#
# Mistake 3 - Forgot ? within string "Is it less or equal(?)", simple grammatical
# error, code executed correctly.

# Prints a string
print("I will now count my chickens:")

# Prints the word 'Hens' followed by an equation
print("Hens", (float(25 + 30 / 6)))

# Same as above
print("Roosters", (float(100 - 25 * 3 % 4)))

# Simple string
print("Now I will count the eggs:")

# Prints an equation
print(float(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6))

# Simple string
print("Is it true that 3 + 2 < 5 - 7?")

# Prints an equation
print(3 + 2 < 5 - 7)

# Prints string and equation
print("What is 3 + 2?", (float(3 + 2)))
# See above
print("What is 5 - 7?", (float(5 - 7)))

# Simple string
print("Oh, that's why it's False.")
# Simple string
print("How about some more.")

# String plus equation
print("Is it greater?", (float(5 > -2)))
# String plus equation
print("Is it greater or equal?", (float(5 >= -2)))
# String plus equation
print("Is it less or equal?", (float(5 <= -2)))
