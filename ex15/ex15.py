# Imports the argument variable from Python's system-specific functions module
from sys import argv

# Defines the name of this script and our filename as arguments to be read
# on running the script
script, filename = argv

# Defines variable 'txt' as the act of opening our filename defined in argv
txt = open(filename)

# Prints a string containing a format activator calling our filename
print(f"Here's your file {filename}:")
# Displays on screen our opened file by using the read() function
print(txt.read())

# Closes the file
txt.close()

# Prints another string
print("Type the filename again:")
# Prompts the user to input the filename and uses that to define it as a
# variable called 'file_again'
file_again = input("> ")

# Takes the user input and opens it using the open() function
txt_again = open(file_again)

# Displays the opened file on screen using read()
print(txt_again.read())

# Closes the file
txt_again.close()
