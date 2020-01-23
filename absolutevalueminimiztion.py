import math
def medium(a):
    isEven = len(a) % 2 == 0
    if(isEven):
        half = abs(len(a)/2)
        value = int(half)
        return ((a[value-1]))
    else:
        half = len(a)/2
        (math.floor(half)) 
        value = int(half)
        return (a[value]) 
print(medium([2,4,7]))
print(medium([2,4,7,6]))
print(medium([2,4,7,6,6]))


