
N1 =
N2 =
N3 =
N4 =

def n_b(a ,b ,c ,d):
    num = (N1, N2, N3, N4)
    result = []
    if(a == N2 or a == N3 or a == N4):
        result.append("B")
    if(b == N1 or b == N3 or b == N4):
        result.append("B")
    if(c == N1 or c == N2 or c == N4):
        result.append("B")
    if(d == N1 or d == N2 or d == N3):
        result.append("B")
    return result
def n_b_S(a, b, c, d):
    num = (N1, N2, N3, N4)
    result = []
    if (a == N1):
        result.append("S")
    if (b == N2):
        result.append("S")
    if (c == N3):
        result.append("S")
    if (d == N4):
        result.append("S")
    return result


while True:
    numbers = input("숫자 네개를 입력: ").split()
    n1 = int(numbers[0])
    n2 = int(numbers[1])
    n3 = int(numbers[2])
    n4 = int(numbers[3])
    n_b(n1, n2, n3, n4)
    n_b_S(n1, n2, n3 , n4)
    def NS():
        if (len(n_b_S(n1,n2,n3,n4)) == 1):
            return "1s"
        if (len(n_b_S(n1,n2,n3,n4)) == 2):
            return "2s"
        if (len(n_b_S(n1,n2,n3,n4)) == 3):
            return "3s"
        if (len(n_b_S(n1,n2,n3,n4)) == 4):
            return "4s"
        else:
            return "0s"

    def NB():
        if (len(n_b(n1,n2,n3,n4)) == 1):
            return "1b"
        if (len(n_b(n1,n2,n3,n4)) == 2):
            return "2b"
        if (len(n_b(n1,n2,n3,n4)) == 3):
            return "3b"
        if (len(n_b(n1,n2,n3,n4)) == 4):
            return "4b"
        else:
            return "0b"
    NS()
    NB()
    print(f"{NS()} {NB()}")
































