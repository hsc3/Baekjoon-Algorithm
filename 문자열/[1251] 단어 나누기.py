'''
[1251] 단어 나누기 / Silver 5 / 문자열, 브루트포스
알파벳 소문자로 이루어진 단어를 가지고 아래와 같은 과정을 해 보려고 한다.
먼저 단어에서 임의의 두 부분을 골라서 단어를 쪼갠다. 즉, 주어진 단어를 세 개의 더 작은 단어로 나누는 것이다.
각각은 적어도 길이가 1 이상인 단어여야 한다. 이제 이렇게 나눈 세 개의 작은 단어들을 앞뒤를 뒤집고, 이를 다시 원래의 순서대로 합친다.
예를 들어,
단어 : arrested
세 단어로 나누기 : a / rre / sted
각각 뒤집기 : a / err / dets
합치기 : aerrdets
단어가 주어지면, 이렇게 만들 수 있는 단어 중에서 사전순으로 가장 앞서는 단어를 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

word = input().rstrip()

res = []
for i in range(1, len(word)-1) :
    for j in range(i+1, len(word)) :
        s1, s2, s3 = word[:i], word[i:j], word[j:] # 세 개의 단어로 나눈다.
        res.append(s1[::-1] + s2[::-1] + s3[::-1]) # 나눈 단어의 앞뒤를 뒤집는다.

print(sorted(res)[0]) # 사전순으로 가장 빠른 단어를 출력


