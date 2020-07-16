#문제
#컴퓨터가 1~100 사이의 정수값 중 하나를 랜덤하게 선택
# 사용자가 맞추는 게임 기회는 5회

import random

#랜덤함수 생성함수
def randomNumber(start, endnumber):
    return int(random.random()*(endnumber-start+1)+start)

#맞추기 게임
def quiz(questionNumber):
    print(questionNumber)
    for chance in range(1,6):

        # print(chance+1,end='')
        # guess = int(input("번째 추축값"))
        guess = int(input(str(chance)+ "번째 추측값 : "))

        if guess == questionNumber:
            print("정답입니다")
            break
        elif guess > questionNumber:
            print(guess," 보다는 작습니다")
        else:
            print(guess," 보다는 큽니다")

        if chance == 5:
            print("기회를 모두사용하였습니다 실패 정답은 ",questionNumber)

def main():

    num = randomNumber(1,100)
    quiz(num)

main()



"""

강사님 Version
def main():
    number = rand(1,100)
    for i in range(1,6):
    num = int(input(str(i) + "번째 추측값:"))
    result = number - num
    if result == 0 : #정답
        print("정답입니다")
        break
    elif result > 0 :
        print(num, "보다는 큽니다")
    else:
        print(num, "보다는 작습니다.")
        
    if result != 0 :
    print("실패했습니다. 정답은 ", number)

"""