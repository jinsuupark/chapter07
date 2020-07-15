def intsum(*ints):
    total = 0
    for num in ints:
        total += num
    return total


# print(intsum(1,2,3))
# print(intsum(5,7,9,11,13))
# print(intsum(8, 9, 6, 2, 9, 1,5,7))

# 인수의 기본값
# calcstep( begin=1,end,step=1) 안된다 인수 초기화는 뒤에서부터
def calcstep(begin, end, step=1):
    total = 0
    for num in range(begin, end + 1, step):
        total += num

    return total


print("1 ~ 10 =", calcstep(1, 10, 2))
print("2 ~ 10 =", calcstep(1, 100))



def kim():
    temp = "김과장의 함수"
    print(temp)

def lee():
    temp = 2**10
    return temp
def park(a):
    temp = a*2
    print(temp)

kim()
print(lee())
park(10)

#전역변수

salerate = 0.9

def kim():
    print("오늘의 할인율 :", salerate)
def lee():
    price = 1000
    print("가격:",price*salerate)

kim()
salerate = 1.1
lee()


price = 1000

def sale():

    global price
    price = 500

sale()
print(price)


######################################


def calcsum(n):
    ''' 1~n까지의 합계를 구해 리턴한다   '''
    total=0
    for i in range(n+1):
        total += i
    return total

help(calcsum)




def findMin(*ints):
    min = ints[0]
    for i in ints:
        print(i)
        if min >= i:
            min = i
        # else:
        #     pass
    return min

def findMax(*ints):
    max=-ints[0]

    for i in ints:
        if max <= i:
            max = i
    return max

min = findMin(5, 6, 4, -15, 7, -1, 2, 1)
max = findMax(5, 6, 4, -15, 7, -1, 2, 1)
print("최소값은",min)
print("최대값은",max)




