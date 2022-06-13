# [1316] 그룹 단어 체커
# Silver 5 >> 구현, 문자열

import sys ; input = sys.stdin.readline

N = int(input())
res = N

for _ in range(N) :
    word = input().rstrip()
    for i in range(len(word)) :
        if word[i] == word[i+1] :
            continue
        elif word[i] in word[i+1:] :
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