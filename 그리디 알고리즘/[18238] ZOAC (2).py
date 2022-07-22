# [18238] ZOAC (2) / Bronze 2 / 그리디 알고리즘
'''
작년 ZOAC의 방식은 너무 식상하다고 생각한 성우는 문자열을 보여주는 새로운 규칙을 고안해냈다!
규칙은 이러하다.

그림과 같은 원판에 문자들이 순서대로 적혀있다. 처음 순간에 화살표는 'A'를 가리키고 있다.
원판은 왼쪽 또는 오른쪽으로 돌릴 수 있다. 원판을 한 칸 돌리는 데에는 1의 시간이 소요된다.
화살표가 가리키고 있는 문자를 출력할 수 있다. 문자를 출력하는 데에 걸리는 시간은 없다.
시간이 너무 오래 걸리면 지루해할 ZOAC의 참가자들을 위해 성우는 해당 문자열을 앞에서부터 차례대로 최대한 빠르게 출력하려고 한다.

바쁜 성우를 위하여 해당 문자열을 출력하는 데 걸리는 시간의 최솟값을 구해보자.
'''
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
s = input()
ans = 0
idx = 0

for word in s :
    left = right = idx
    check = 0
    while True:
        if alphabet[left] == word :
            ans += check
            idx = left
            break
        if alphabet[right] == word :
            ans += check
            idx = right
            break
        
        check += 1
        left -= 1
        right += 1
        if left == -26 : left = 0
        if right == 26 : right = 0
print(ans)

'''
n=input()
text='A'
cnt=0
for i in range(len(n)):
    s=(min(abs(ord(n[i])-ord(text)),26-abs(ord(n[i])-ord(text))))
    cnt+=s
    text=n[i]
print(cnt)
'''