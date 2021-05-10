# Defines variable "tabby_cat" as a string and uses the escape sequence \t to
# tab it in when displayed.
tabby_cat = "\tI'm tabbed in."
# Defines variable "persian_cat" as a string and uses the escape sequence \n
# to display the second half on a new line.
persian_cat = "I'm split\non a line."
# Defines variable "backslash_cat" as a string and uses a simple \ escape to
# display one single \ in the text without potentially causing formatting
# issues.
backslash_cat = "I'm \\ a \\ cat."

# Defines variable "fat_cat" as a multi-line string and uses \t escape
# sequences to tab in the items on the list for formatting. Also demonstrates
# the usage of \n to form a new line.
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

# Each of these simply prints the defined variables.
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
