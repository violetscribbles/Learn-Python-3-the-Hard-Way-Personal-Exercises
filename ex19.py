# Defines function cheese_and_crackers as two variables and four print
# statements, which will display whenever the function is called. The print
# statements contain arguments which are formatted in later lines. The final
# statement contains the escape variable \n to ensure the next prints
# are added in newline.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# Prints a string
print("We can just give the function numbers directly:")
# Defines the arguments as numbers.
cheese_and_crackers(20, 30)


# Prints a string
print("OR, we can use variables from our script:")
# Defines two variables as numbers
amount_of_cheese = 10
amount_of_crackers = 50

# Injects the two variables into our function and runs it
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# Prints a string
print("We can even do math inside too:")
# Injects two equations as our arguments for our function, which are solved
# when the code is run
cheese_and_crackers(10 + 20, 5 + 6)



# Prints a string
print("And we can combine the two, variables and math:")
# Defines our function as our previously defined variables, then performs
# an equation which is solved on running the code.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
