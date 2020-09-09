c = "Geoergr"
from math import *

print(c[(c.__len__() - 1)])
print(c[len(c) - 1])

d = "Python is bad"
d = d.replace("bad", "super cool")
print(d)
print("----------------------------------------")
nr = 1
st = "2.9"

nrr = 1 + float(st)

print(nrr)
print(sqrt(36))

name = input("Enter your name: ")
age = int(input ("Please provide your name: "))
print("Hello " + name)
if age > 18:
    print("you are accepted !")
else:
    print("sorry you are not accepted !")
