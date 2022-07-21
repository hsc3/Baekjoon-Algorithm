'''
[10798] 세로 읽기 / Bronze 1 / 구현, 문자열
칠판에 붙여진 단어들이 주어질 때, 영석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline
data = [input().rstrip() for _ in range(5)]

for j in range(15) :
    for i in range(5) :
        if j < len(data[i]) :
            print(data[i][j], end='')
'''
import sys
input = sys.stdin.readline

def ReadVertical(data) :
    check = [False] * 5
    i = 0
    while False in check :
        if data[i] : 
            print(data[i].pop(0), end='')
        else : 
            check[i] = True
    
        i += 1
        if i == 5 : 
            i = 0

data = []
for _ in range(5) :
    data.append(list(input().rstrip()))

ReadVertical(data)
'''
'''
words = [input() for _ in range(5)]
maxLen = 0
for word in words:
    maxLen = max(maxLen, len(word))

for j in range(maxLen):
    for i in range(5):
        if j > len(words[i])-1:
            continue
        print(words[i][j], end='')
'''