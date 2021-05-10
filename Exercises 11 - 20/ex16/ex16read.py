from sys import argv

script, filename = argv

print(f"Here is your file {filename}: \n")

txt = open(filename)

print(txt.read())

print("Closing the file now...")
txt.close()
