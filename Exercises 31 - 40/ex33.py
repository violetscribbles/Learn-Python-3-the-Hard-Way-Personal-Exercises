# The purpose of this code is to return a list of numbers, counting up in a
# while-loop, until it reaches 8, then append the list of numbers.

def counting(limit):
    i = 0
    numbers = []

    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

counting(8)
