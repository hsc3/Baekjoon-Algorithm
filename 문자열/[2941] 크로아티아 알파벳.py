'''
[2941] 크로아티아 알파벳 / Silver 5 / 문자열
단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
크로아티아 알파벳 목록에 있찌 않은 다른 알파벳은 한 글자씩 센다.
'''
import sys
input = sys.stdin.readline

croatiaAlphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
inputString = input().rstrip()

for i in croatiaAlphabet :
    inputString = inputString.replace(i, '*') # 문자열의 replace 메서드는 변경한 문자열을 반환해준다.

print(len(inputString))

'''
croatiaAlphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
inputString = input().rstrip()

res = 0
while inputString : 

    if len(inputString) >= 3 and inputString[:3] in croatiaAlphabet :
        inputString = inputString[3:]
    
    elif len(inputString) >= 2 and inputString[:2] in croatiaAlphabet :
        inputString = inputString[2:]
    
    else :
        inputString = inputString[1:]

    res += 1

print(res)
'''