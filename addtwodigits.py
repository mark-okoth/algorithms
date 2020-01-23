def AddTwodigits(a):
    count = 0
    for i in str(a):
        mark = int(i)
        count = count + mark
    return count
       
print(AddTwodigits(15893))    