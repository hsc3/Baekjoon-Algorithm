'''
[11721] 열개씩 끊어 출력하기 | https://www.acmicpc.net/problem/11721
알파벳 소문자와 대문자로만 이루어진 길이가 N인 단어가 주어진다. 한 줄에 10글자씩 끊어서 출력하는 프로그램을 작성하시오. 
'''
s = input()
for i in range(len(s)//10) :
    print(s[10*i : 10*(i+1)])
print(s[10*(len(s)//10):])

'''
a = str(input())
for i in range (0, len(a), 10) :
    print(a[i:i+10])
'''