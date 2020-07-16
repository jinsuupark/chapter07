import random

start = 1
end = 6


def rand(start, end):
    return int(random.random() * (end-start+1)) + start

# main 함수 -> 프로그램의 entry Point0
def main():
    start = 1
    end = 6
    number = rand(start,end)
    print(number)


for n in range(5):
    main()



