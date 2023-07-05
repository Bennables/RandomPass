import random;
import numpy
lower_letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_chars = "`~!@#$%^&*()_+-=}{[]\|;':./>?,<\""
numbers = "1234567890"

def lower():
    lower = random.randint(0, len(lower_letters))
    return lower_letters[lower: lower+1]

def upper():
    upper = random.randint(0, len(upper_letters))
    return upper_letters[upper: upper+1]

def spec():
    spec = random.randint(0, len(special_chars))
    return special_chars[spec: spec+1]

def number():
    number = random.randint(0,len(numbers))
    return numbers[number: number+1]




def create_pass(a, b, c, d):
    passs = ""
    for i in range(a):
        passs += lower()
    for i in range(b):
        passs += upper()
    for i in range(c):
        passs += spec()
    for i in range(d):
        passs += number()
    print(passs)
    passs = list(passs)
    print(passs)
    numpy.random.shuffle(passs)
    x = ''.join(passs)
    print(x)

a = int(input("lowers"))
b = int(input("uppers"))
c = int(input("specs"))
d = int(input("numbers"))

create_pass(a,b,c,d)

