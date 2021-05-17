from sys import argv

script, first, second = argv

def add(first, second):
    print(f"{first} + {second} is", end=' ')
    return first + second

def subtract(first, second):
    print(f"If we subtract {second} from {first} we get", end=' ')
    return first - second

def multiply(first, second):
    print(f"Multiplying {first} by {second} gets us", end=' ')
    return first * second

def divide(first, second):
    print(f"And dividing {first} by {second} equals", end=' ')
    return first / second

print(f"Let's do some quick maths using your inputted variables: {first} and {second}...")

print(f"\t{add}")
print(f"\t{subtract}")
print(f"\t{multiply}")
print(f"\t{divide}")

print("Thanks!")
