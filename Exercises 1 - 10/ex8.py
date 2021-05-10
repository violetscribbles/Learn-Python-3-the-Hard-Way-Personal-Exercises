# Defines "formatter" variable as a sequence of four open format() arguments
# in a string.
formatter = "{} {} {} {}"

# Tells Python to print the "formatter" variable using format() to send four
# arguments into the string, replacing the open arguments first defined.
print(formatter.format(1, 2, 3, 4))
# See above
print(formatter.format("one", "two", "three", "four"))
# See above, also to note is that Python recognises 'True' and 'False'
# as keywords directly representing their concepts. Due to this, we do not
# put them in quotations as they do not need to be part of a string.
print(formatter.format(True, False, False, True))
# See above, but formatter simply reads the variable defined and prints them -
# there are no arguments present to fill the gaps.
print(formatter.format(formatter, formatter, formatter, formatter))
# See above. Here, format() reads four strings as arguments and uses them
# to fill the gaps in the variable.
print(formatter.format(
    "Get a load of the kid in the Gangrene tshirt:",
    "They were the gateway band, a Pastor and a teacher to me.",
    "I always want to be real with the things they believe in,",
    "But since we've been talking I'm not sure if I believe anything."
))
