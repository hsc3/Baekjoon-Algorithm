# [10809] 알파벳 찾기 | Bronze 5 | https://www.acmicpc.net/problem/10809
import sys
input = sys.stdin.readline
# chr : ascii -> alphabet
# ord : alphabet -> ascii
# a = 97 ~ z = 122

dict = [-1 for _ in range(26)]
word = list(input().rstrip())
for i in range(len(word)):
    if dict[ord(word[i])-97] == -1:
        dict[ord(word[i])-97] = i

print(*dict)

