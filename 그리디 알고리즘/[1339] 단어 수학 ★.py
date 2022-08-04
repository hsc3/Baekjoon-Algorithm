# [1339] 단어 수학 | Gold 4 | 그리디 알고리즘
'''
민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다. 단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다.
이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.
예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 두 수의 합은 99437이 되어서 최대가 될 것이다.
N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

words, alphabets = [], dict()
for _ in range(int(input())):
    word = input().rstrip()
    l = len(word)
    for i in range(l):
        # 일단 모든 알파벳을 1로 가정하고, 단어에서 차지하는 크기를 누적
        # EX) ABC -> A = 100 , B = 10 , C = 1
        alphabets[word[i]] = alphabets.get(word[i], 0) + (10**(l-1-i))
    words.append(word)

sortedAlphabet = sorted(alphabets, key = lambda x : -alphabets[x]) # words에 포함되어 있는 alphabet들을 내림차순 정렬

answer = 0
for word in words:
    num = ''
    for alphabet in word:
        num += str(9 - sortedAlphabet.index(alphabet)) # alphabet을 숫자로 변환
    answer += int(num)

print(answer)