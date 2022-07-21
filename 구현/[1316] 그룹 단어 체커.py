'''
[1316] 그룹 단어 체커 / Silver 5 / 구현, 문자열
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
'''

import sys ; input = sys.stdin.readline

N = int(input())
res = N

for _ in range(N) :
    word = input().rstrip()
    for i in range(len(word)) :
        if word[i] == word[i+1] : # 다음 단어와 동일, 일단 그룹 단어의 조건이 깨지지 X
            continue
        elif word[i] in word[i+1:] : # 다음 단어와 다른데 같은 단어가 그 다음에 또 나오는 경우, 그룹 단어의 조건이 깨짐
            res -= 1
            break
print(res)

'''
res = 0

for _ in range(int(input())) :
    word = input().rstrip()
    if len(word) == 1 : 
        res += 1
    else :
        check = True
        alphabet = []
        for i in range(len(word)) :
            if i == 0 :
                prev = word[i]
                alphabet.append(word[i])
            else :
                if word[i] != prev :
                    if word[i] in alphabet :
                        check = False
                        break
                    else :
                        alphabet.append(word[i])
                        prev = word[i]
        if check : 
            res += 1

print(res)
'''