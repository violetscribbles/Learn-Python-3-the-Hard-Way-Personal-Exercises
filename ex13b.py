from sys import argv

script, first, second, third = argv

print("Lets talk about:", first)
memory = input("What's something that reminds you of it? ")
print(f"It's really interesting that you said {memory}, thanks for sharing.")
print("It seems you also typed:", second)
game = input('''
\tQUICK!\n\tTell me the first association that pops into your head!
''')
print(f"So you associate {second} with {game}? Odd... but interesting!")
print(f"We're not even gonna touch {third}, that's just... eugh.")
print("Thanks for joining me!")
