import random

# This is a print statement
print("hi")

# Integers
intNum = 1
print("This is an int: ", intNum)

# Doubles
doubleNum = 1.11
print("This is a double: ", doubleNum)

# Booleans
boolTF = True
print("This is a boolean: ", boolTF)

# If statement
if boolTF:
    print("The statement is true")
else:
    print("The statement is false")

# While Loop
count = 0
while boolTF:
    count += 1
    if count == 3:
        boolTF = False
    print("Counting while loop")

# For Loop counting
for x in range(3):
    print(x)

# For loop array display
arrNames = ["Dylan", "Dom", "Alex"]
for names in arrNames:
    print(names)

# For Loop counting with array
arrNames1 = ["Dylan", "Dom", "Alex"]
for x in range(len(arrNames1)):
    print(arrNames1[x])

# User input
uName = input("Enter your name: ")
print("Your name is: " + uName)

# Check if your name is in the array above
if uName in arrNames:
    print("Your name " + uName + " is in the array")
else:
    print("Your name " + uName + " is not in the array")

# Try Catch statement
try:
    print(uName in arrNames)
except:
    print("Nope")

# Random number generator
randNum = random.randint(0, 99999999)
print("Random number: ", randNum)

# Adding values to an array
arrAdd = []
for x in range(3):
    randNum1 = random.randint(0, 99999999)
    arrAdd.append(randNum1)
print(arrAdd)

# Remove values
arrAdd.pop(1)
print(arrAdd)

# Find index of a value in an array
print("Your name is in index: ", arrNames1.index(uName))

# NESTED ARRAYS 2D
# it will look like this 3 x 3
# Index 0: |0, 1, 2|
# Index 1: |0, 1, 2|
# Index 2: |0, 1, 2|
size2d = 3
arrNest2d = [[x for x in range(size2d)] for y in range(size2d)]
print(arrNest2d)

# NESTED ARRAYS 3D
# it will look like this 3 x 3 x 3
# Index 0:
    # Index 0: |0, 1, 2|
    # Index 1: |0, 1, 2|
    # Index 2: |0, 1, 2|
# Index 1:
    # Index 0: |0, 1, 2|
    # Index 1: |0, 1, 2|
    # Index 2: |0, 1, 2|
# Index 2:
    # Index 0: |0, 1, 2|
    # Index 1: |0, 1, 2|
    # Index 2: |0, 1, 2|
size3d = 3
arrNest3d = [[[x for x in range(size3d)] for y in range(size3d)] for z in range(size3d)]
print(arrNest3d)

# Reverse array
print("Before: ", arrAdd)
arrAdd.reverse()
print("After: ", arrAdd)
