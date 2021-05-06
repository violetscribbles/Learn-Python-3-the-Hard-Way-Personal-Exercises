# Notes:
# Study Drill 1 - Notation added to each line
#
# Study Drill 2 - # used to identify lines where strings are put inside
# other strings
#
# Study Drill 3 - Perhaps I'm wrong, but I feel using format() to input
# a variable into a previous line counts as a singular usage of a string
# inside a string. Within that context, I believe there are only four examples.
#
# Study Drill 4 - Using the + operator on two strings, defined here as "w"
# and "e", tells python to join them as a method of Concatenation, rather
# than reading them as mathematical variables.


# Defines variable "types_of_people" as 10
types_of_people = 10
# Defines variable "x" as a string including a string
x = f"There are {types_of_people} types of people." #

# Defines variable "binary" as "binary"
binary = "binary"
# Defines variable "do_not" as "don't"
do_not = "don't"
# Defines variable "y" as a string including two strings
y = f"Those who know {binary} and those who {do_not}." #

# Prints variable "x"
print(x)
# Prints variable "y"
print(y)

# Prints string including a string
print(f"I said: {x}") #
# Prints string including a string
print(f"I also said: '{y}'") #

# Defines variable "hilarious" as "False"
hilarious = False
# Defines variable "joke_evaluation" as a string with empty call for variable
joke_evaluation = "Isn't that joke so funny?! {}" #

# Prints variable "joke_evaluation" inputting variable "hilarious" using
# format()
print(joke_evaluation.format(hilarious)) #* pt. 2 of variable before

# Defines variable "w" as a string
w = "This is the left side of..."
# Defines variable "e" as a string
e = "a string with a right side."

# Prints variables "w" and "e" together to form a coherent sentence
print(w + e)
