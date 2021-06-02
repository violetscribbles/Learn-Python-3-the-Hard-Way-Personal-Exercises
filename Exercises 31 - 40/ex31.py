print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Engage in a dance battle to establish dominance.")
    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    elif bear == "3":
        print("""The bear eyes you aggressively, awaiting your first move.
Pulling out your trusty vinyl collection, you assess your options.""")
        print("What record do you choose?")
        print('1. "Everybody" by the Backstreet Boys.')
        print('2. "Hey Ya!" by Outkast.')
        print('3. "The Less I Know the Better" by Tame Impala.')
        music = input("> ")

        if music == "1":
            print("""The bear's eyes fill with desperation as it realises the
mistake it made getting in your way. It claws at the walls,
unable to escape your vicious onslaught of early 2010's moves.
You finish the bear off with the Spongebob and he shuffles off
this mortal coil.""")
            print("Good job!")
        elif music == "2":
            print("""You break into a well rehearsed routine but the bear is
unaffected. It appears he has built up an immunity to this song
through repeated exposure. He spin-kicks your head in and you
die.""")
            print("Good job!")
        elif music == "3":
            print("""The bear is confused by your extremely underground taste
in music and perishes due to complications with stage 4 boogie fever.
You have won.""")
            print("Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
