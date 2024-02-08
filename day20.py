import random

answer = random.randint(1,100)
chance = 7

while chance != 0:
    num = int(input("1~100사이의 숫자를 입력하세요 : "))
    if(num == answer):
        print(f" 정답입니다.")
        break
    elif(num > answer):
        chance = chance - 1
        print("답이 더 작습니다.")

    else:
        chance = chance - 1
        print("답이 더 큽니다.")

else:
    print("ㅂㅅ")

