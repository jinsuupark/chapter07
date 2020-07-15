def calsum(n):
    total = 0

    for num in range(n+1):
        total += num

    return total

def calcrange(begin, end):
    total = 0
    for num in range(begin, end+1):
        total += num

    return total

def printsum(n):
    total =0
    for num in range(n+1):
        total += num
    print("~",n,"=",total)
printsum(4)
printsum(10)
print