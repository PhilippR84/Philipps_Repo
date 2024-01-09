"""
def get_Grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(get_Grade(85))

a = "100"
b = "300"

print("A") if a > b else print("=") if a == b else print("B")


a = 200
b = 33
c = 500
if c < a and a > b or b < c:
    print("At least one of the conditions is True")


# Truth-Table

def XOR (a, b):
    if (a == 0 and b == 0) or (a == 1 and b == 1):
        print("0")
    else:
        print("1")
    #elif (a == 0 or b == 0) and (a == 1 or b == 1):
    #  print("1")

def AND (a, b):
    if a == 1 and b == 1:
        print("1")
    else:
        print(0)

def OR (a, b):
    if a == 0 and b == 0:
        print("0")
    else:
        print("1")

def NAND (a, b):
    if a == 1 and b == 1:
        print("0")
    else:
        print("1")

def NOR (a, b):
    if a == 0 and b == 0:
        print("1")
    else:
        print("0")

def XNOR (a, b):
    if (a == 1 and b == 1) or (a == 0 and b == 0):
        print("1")
    else:
        print("0")

a = 1 
b = 0

print((a,b))
"""


def Draw(a):
    i = 1
    while i <= a:
        numbers = ""
        for x in range (1, i+1):
            numbers += str(i)
        i += 1
        print(numbers)
Draw(5)

def PrimeNumbers(a)
    