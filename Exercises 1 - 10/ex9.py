# Here's some new strange stuff, remember type it exactly.

# Defines 'days' variable as a string
days = "Mon Tue Wed Thu Fri Sat Sun"
# Defines 'months' variable as a string. Each month is preceded by \n, which
# is an escape character that tells python to create a new line before the
# text.
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Prints a string and then variable 'days'
print("Here are the days: ", days)
# Prints a string and then variable 'months'
print("Here are the months: ", months)

# Prints a multi-line string using """, which achieves the same effect as
# /n but is more readable.
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
