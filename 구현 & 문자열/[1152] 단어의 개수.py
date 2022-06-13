'''
[1152] 단어의 개수 | https://www.acmicpc.net/problem/1152
영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오.
'''
str = input()
cnt = 0
isWord = False
for i in range(len(str)) :
    if str[i] == ' ' and not isWord :
        continue
    elif str[i] != ' ' and not isWord :
        cnt += 1
        isWord = True
    elif str[i] != ' ' and isWord :
        continue
    elif str[i] == ' ' and isWord :
        isWord = False

print(cnt)

'''
a = input()

count = 0
for char in a:
    if char == ' ':
        count += 1
if ' ' == a[0]:
    count -= 1
if ' ' == a[-1]:
    count -= 1

print(count+1)
'''