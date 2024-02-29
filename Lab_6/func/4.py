from time import sleep
from math import sqrt

def sleeep():
    x = int(input())
    sqx = sqrt(x)
    miliseconds = int(input())
    sleep(miliseconds/1000)
    print(f"Square root of {x} after {miliseconds} is {sqx}")

sleeep()