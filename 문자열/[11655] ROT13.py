'''
[11655] ROT13 / Bronze 1 / 문자열
ROT13은 카이사르 암호의 일종으로 영어 알파벳을 13글자씩 밀어서 만든다.
ROT13은 알파벳 대문자와 소문자에만 적용할 수 있다. 알파벳이 아닌 글자는 원래 글자 그대로 남아 있어야 한다.
문자열이 주어졌을 때, "ROT13"으로 암호화한 다음 출력하는 프로그램을 작성하시오.
'''
import sys ; input = sys.stdin.readline

l = list(map(str, input().rstrip()))
answer = ""

for i in range(len(l)) :
    n = ord(l[i])
    if 65 <= n <= 90 or 97 <= n <= 122 :
        n += 13
        if (l[i].isupper() and n > 90) or (l[i].islower() and n > 122) :
            n -= 26
        l[i] = chr(n)

print(*l, sep='')

'''
s=input()
answer=[]

for x in s:
    if 'a'<=x and x<='z':
        x=ord(x)+13
        if x>122:
            x-=26
        answer+=chr(x)
    elif 'A'<=x and x<='Z':
        x=ord(x)+13
        if x>90:
            x-=26
        answer+=chr(x)
    else:
        answer+=x


for i in answer:
    print(i, end='')
'''