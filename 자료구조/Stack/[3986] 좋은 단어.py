# [3986] 좋은 단어 | Silver 4 | 자료구조(stack)
'''
평석이는 단어 위로 아치형 곡선을 그어 같은 글자끼리(A는 A끼리, B는 B끼리) 쌍을 짓기로 하였다.
만약 선끼리 교차하지 않으면서 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝 지을수 있다면 '좋은 단어'이다. 
평석이가 '좋은 단어' 개수를 세는 것을 도와주자.
'''
import sys
input = sys.stdin.readline

ans = 0
for _ in range(int(input())) :
    word = input().rstrip()
    stk = []
    for c in word :
        if stk and stk[-1] == c :
            stk.pop()
        else :
            stk.append(c)

    if not stk :
        ans += 1

print(ans)

# import sys
# input = sys.stdin.readline
#
# ans = 0
# for _ in range(int(input())) :
#     word = input().rstrip()
#     while True :
#         if 'AA' in word :
#             word = word.replace('AA', '')
#         if 'BB' in word :
#             word = word.replace('BB', '')
#         if 'AA' not in word and 'BB' not in word :
#             break
#
#     if len(word) == 0 :
#         ans += 1
#
# print(ans)