import random

def getLotto():
    lottoNums = []
    while len(lottoNums) < 6:
        new_number = random.randrange(1, 46)
        if new_number not in lottoNums :
            lottoNums.append(new_number)

    bonusNums = random.randrange(1, 46)
    while bonusNums in lottoNums:
        bonusNums = random.randrange(1, 46)

    lottoNums.sort()
    return[tuple(lottoNums), bonusNums]

if __name__ == "__main__":
    l = getLotto()
    print(l)

