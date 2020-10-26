# This is an import it takes functions from the directory specified to be used
import random

# This is a variable. They are the soul of programming. They are like a piece of paper that hold a set of data. They can usually hold an infinite amount of data
# They can hold any data type available
varExample = "var"

# This is a print statement it writes to the output screen
print("hi")
# Print statements can both display hard coded text and variables
print("Hardcoded", varExample)

# Integers which is a normal number
intNum = 1
print("This is an int: ", intNum)

# Doubles which are decimal numbers
doubleNum = 1.11
print("This is a double: ", doubleNum)

# Strings which are just sentences
stringWord = "Im a string"
print(stringWord)

# Booleans are either true or false. They are used in verifying if statements are true or not
boolTF = True
print("This is a boolean: ", boolTF)

# If statement
if boolTF:
    # if the statement is meet then it does this
    print("The statement is true")
else:
    # if the statement is NOT meet then it does this
    print("The statement is false")

# While Loop
# Works by looping through its set of instructions until its
# This is a counting variable. These are used everywhere. They are used to stop a section of code when a threshold is meet
count = 0
while boolTF:
    # Incrementing the count by 1 
    count += 1
    if count == 3:
        # When the counter is at 3 the code stops
        boolTF = False
    print("Counting while loop")

# For Loop counting
# This is a loop that keeps going but increments itself unlike the while loop that needs a little help with a variable
# range() just hold a number that is the threshold
for x in range(3):
    print(x)

# For loop array display
# This is an array that holds strings, it could be any data type
arrNames = ["Dylan", "Dom", "Alex"]
# this loops throught the arrays indexes and displays each value of the array in order
for names in arrNames:
    print(names)

# For Loop counting with array
arrNames1 = ["Dylan", "Dom", "Alex"]
# len() gives back the length/size of the array for the range()/threshold
for x in range(len(arrNames1)):
    # This gets the index and then displays the data from that index
    print(arrNames1[x])

# User input and puts it into a variable
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

# NESTED ARRAYS 4D
# it will look like this 3 x 3 x 3 x 3
# Index 0:
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
# Index 1:
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
# Index 2:
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
size4d = 3
arrNest4d = [[[[x for x in range(size4d)] for y in range(size4d)] for z in range(size4d)] for w in range(size4d)]
print(arrNest4d)

# Reverse array
print("Before: ", arrAdd)
arrAdd.reverse()
print("After: ", arrAdd)
