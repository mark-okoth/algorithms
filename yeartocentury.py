import math

def centuryfromyear(year):
    century = year/100
    if(year % 100 == 0):
        return math.floor(century)
    else:
        return math.floor(century) + 1

print(centuryfromyear(1700))
print(centuryfromyear(1995))
    
    