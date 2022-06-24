'''
[16968] 차량 번호판 1 / Bronze 1 / 조합론
상도시의 차량 번호판 형식이 주어졌을 때, 가능한 차량 번호판의 개수를 구해보자.
예를 들어, 형식이 "cd"이면, a1, d4, h5, k4 등이 가능하다. 형식이 "dd"인 경우에 01, 10, 34, 69는 가능하지만, 
00, 11, 55, 66은 같은 숫자가 2번 연속해서 불가능하다.
'''
def Calculator(s) :
    res = 26 if s[0] == 'c' else 10 # 알파벳은 26가지, 숫자는 10가지를 조합할 수 있다.
    for i in range(1, len(s)) :
        if s[i] == s[i-1] : # 앞의 번호와 같은 종류(알파벳 또는 숫자)의 번호인 경우, 중복을 제외한 경우의 수를 조합
            if s[i] == 'c' : res *= 25
            else : res *= 9
        else : 
            if s[i] == 'c' : res *= 26
            else : res *= 10

    return res

s = list(input().rstrip())
print(Calculator(s))