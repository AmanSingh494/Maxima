# 1
# write a function to find the roots of quadratic equation

# first taking in the inputs
import math

a = int(input("enter the coeffecient of x^2  "))
b = int(input("enter the coeffecient of x  "))
c = int(input("enter the last value  "))
d = math.sqrt((b**2) - (4 * a * c))
print("d", d)


def findRoots():
    root1 = (-b + d) / (2 * a)
    root2 = (-b - d) / (2 * a)
    if d == 0:
        print(root1, "Equation has same roots")
    elif d > 0:
        print(root1, root2, "Equation has real and unique roots")
    else:
        print("equation has no real roots")


findRoots()

# 2.1
import math

no = int(input("Enter a no.  "))


def checkPrime():
    flag = 0

    for i in range(2, math.ceil(no / 2)):
        if no % i == 0:
            print(i)
            flag += 1
            break
    if flag > 0:
        print("Given no. is not prime")
    else:
        print("Given no. is prime")


checkPrime()

#  2.2
import math

no = int(input("Enter a no.  "))
li = []


def generateNo():
    for a in range(2, no + 1):
        flag = 0
        for i in range(2, math.ceil(a / 2) + 1):
            if a % i == 0:
                flag += 1
                break

        if flag == 0:
            li.append(a)

    print(li)


generateNo()

# 2.3
import math

no = int(input("Enter a no.  "))
li = [2, 3]


def firstNPrimeNo():
    a = 4
    while len(li) < no:
        flag = 0
        for i in range(2, math.ceil(a / 2) + 1):
            if a % i == 0:
                flag += 1
                break

        if flag == 0:
            li.append(a)
        a += 1

    print(li)


firstNPrimeNo()

# 3
no = int(input("Enter no of rows  "))
space = " "


def printPatern():
    noOfStars = 1
    for i in range(no, 0, -1):
        print((i - 1) * space + "*" * noOfStars)
        noOfStars += 2
    noOfStars -= 2
    noOfStarsSpaces = noOfStars
    for i in range(1, no + 1):
        print((i - 1 + noOfStarsSpaces) * space + "*" * noOfStars)
        noOfStars -= 2


printPatern()

# 4
inp = input("Enter any fckin thing  ")


def check():
    if inp.isalpha():
        # print(inp + 'is an alphabet')
        if inp.isupper():
            print(inp + " is an uppercase alphabet")
        else:
            print(inp + " is a lowercase alphabet")
    elif inp.isnumeric():
        noToWord = [
            "zero",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]
        print(
            inp
            + " is a number and it is wrriten as "
            + noToWord[int(inp)]
            + " in words"
        )
    else:
        print(inp + " is a special character")


check()

# 5
string = input("enter any string ")


def checkFreq():
    char = input("enter any character to check its frequency ")
    freq = 0
    for i in string:
        if i == char:
            freq += 1
    print(f"The character '{char}' appears {freq} times in the string.")


def replace():
    oldChar = input("enter the character you want to replace  ")
    newChar = input("enter the character you want to replace the old character with  ")
    print(f"the new string is '{string.replace(oldChar,newChar)}' ")


def removeFirstCharAppearance():
    char = input("enter the character you want to remove the first appearance of  ")
    index = string.find(char)
    print(index)
    if index != -1:
        new_string = string[:index] + string[index + 1 :]
        print(
            f"The new string after removing the first occurrence of '{char}' is '{new_string}'."
        )
    else:
        print(f"The character '{char}' is not found in the string.")


def removeAllAppearances():
    char = input("enter the character you want to remove all appearances of  ")
    new_string = string.replace(char, "")
    print(
        f"The new string after removing all occurrences of '{char}' is '{new_string}'."
    )


# checkFreq()
# replace()
removeFirstCharAppearance()
# removeAllAppearances()

# 6
string1 = input("enter first string  ")
string2 = input("enter second string  ")
noOfChar = int(input("enter the number of characters to be swapped in the strings  "))


def swapChar(x, y):
    a = x
    x = y[: (noOfChar + 1)] + x[(noOfChar + 1) :]
    y = a[: (noOfChar + 1)] + y[(noOfChar + 1) :]
    print(f"string1 is '{x}' now")
    print(f"string2 is '{y}' now")


swapChar(string1, string2)

# 7
string1 = input("enter first string  ")
string2 = input("enter second string  ")
occurenceIndexList = []


def findOccurence():
    indices = []
    start = 0
    while True:
        index = string1.find(string2, start)
        if index == -1:
            break
        indices.append(index)
        start = index + len(string2)
    return indices if indices else -1


occurenceIndexList = findOccurence()
print(occurenceIndexList)

# 8
inputList = input("enter a list of numbers separated by space  ").split()
cubeList = []

# using for loop
# def findEvenCube():
#     for i in inputList:
#         if int(i) % 2 == 0:
#             cubeList.append(int(i) ** 3)
#     if cubeList:
#         print(f"The cubes of even numbers in the list are {cubeList}")
#     else:
#         print("No even numbers found in the list")


# using list comprehension
def findEvenCube(lis):
    def checkEven(x):
        if int(x) % 2 == 0:
            return int(x) ** 3

    cubeList = list(map(checkEven, lis))
    cubeList = [i for i in cubeList if i is not None]
    if cubeList:
        print(f"The cubes of even numbers in the list are {cubeList}")
    else:
        print("No even numbers found in the list")


findEvenCube(inputList)


# 9
def process_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    # Task a
    char_count = sum(len(line) for line in lines)
    word_count = sum(len(line.split()) for line in lines)
    line_count = len(lines)
    print(f"Characters: {char_count}, Words: {word_count}, Lines: {line_count}")

    # Task b
    char_freq = {}
    for line in lines:
        for char in line:
            char_freq[char] = char_freq.get(char, 0) + 1
    print(f"Character frequencies: {char_freq}")

    # Task c
    words = " ".join(lines).split()
    print("Words in reverse order:", " ".join(reversed(words)))

    # Task d
    with open("File1", "w") as file1, open("File2", "w") as file2:
        for i, line in enumerate(lines, start=1):
            if i % 2 == 0:  # even line
                file1.write(line)
            else:  # odd line
                file2.write(line)


# Usage
process_file("text.txt")


# 10
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print(f"({self.x},{self.y})")

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


p1 = Point(4, 5)
p2 = Point(6, 8)
p1.print()
p2.print()
distance = p1.distance(p2)
print(distance)

# 11
dictionary = {}


def printDic():
    for i in range(1, 6):
        dictionary[i] = i**3
    print(dictionary)


printDic()

# 12
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
# Print half the values of the tuple in one line and the other half in the next line.
print(t1[: (len(t1) // 2)])
print(t1[(len(t1) // 2) :])

# Print another tuple whose values are even numbers in the given tuple.
t2 = tuple(x for x in t1 if x % 2 == 0)
print(f"tuple with even values is {t2}")

#  Concatenate a tuple t2=(11,13,15) with t1.
t3 = (11, 13, 15)
ConcatenatedTuple = t1 + t3
print(f"this is Concatenated tuple {ConcatenatedTuple}")
#
maximum = max(ConcatenatedTuple)
minimum = min(ConcatenatedTuple)
print(f"the maximum value is {maximum}, the minimum value is {minimum}")

# 13
# WAP to accept a name from a user. Raise and handle appropriate exception(s) if the text entered by the user contains digits and/or special characters.
name = input("enter your name")


def validateName():
    for i in name:
        if i.isnumeric():
            print("Numeric values are not allowed in name")
        elif i.isalpha() or i == " ":
            pass
        else:
            print("special characters are not allowed in name")


validateName()
