# Notes:
# Study Drill 1 - "My_" removed from variables, successful program launch.
#
# Study Drill 2 - Measurements converted and implemented. Didn't figure out
# how to round my floating points in time before leaving.


name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
cm_height = height * 2.54
kg_weight = weight / 2.205

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall, or {cm_height} centimeters.")
print(f"He's {weight} pounds heavy, which is {kg_weight} in kilograms.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
metric_total = age + cm_height + kg_weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
print(f"Or, using my metric measurements: {age}, {cm_height}, and {kg_weight} gives me {metric_total}")
