def recusive_fuctorial(n):
    if n < 0:
        return -1

    elif n < 2:
        return 1

    else:
        return n * recusive_fuctorial(n-1)


print(recusive_fuctorial(10))

# sum of numbers
def recSumFirstN(n):
    if n == 0:
        return 0


    return recSumFirstN(n-1) + n

print(recSumFirstN(10))
