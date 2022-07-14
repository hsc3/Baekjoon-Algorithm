'''
[1919] 애너그램 만들기 / Bronze 2 / 문자열
두 영어 단어가 철자의 순서를 뒤바꾸어 같아질 수 있을 때, 그러한 두 단어를 서로 애너그램 관계에 있다고 한다.
두 개의 영어 단어가 주어졌을 때, 두 단어가 서로 애너그램 관계에 있도록 만들기 위해서 제거해야 하는 최소 개수의 문자 수를 구하는 프로그램을 작성하시오.
문자를 제거할 때에는 아무 위치에 있는 문자든지 제거할 수 있다.
'''
import sys
input = sys.stdin.readline

wordA = list(input().rstrip())
wordB = list(input().rstrip())
intersection = []

for a in wordA:
    if a in wordB:
        intersection.append(a)
        wordB.remove(a)

print(len(wordA) + len(wordB) - len(intersection))


# import sys
# from collections import Counter
# input = sys.stdin.readline
# # 정답은 { ( A U B ) - ( A N B ) } 에 포함된 문자의 수와 같다.
# wordA = Counter(input().rstrip())
# wordB = Counter(input().rstrip())
#
# answer = 0
# for key in wordA.keys():
#     if wordA[key] - wordB[key] > 0:
#         answer += (wordA[key] - wordB[key])
#
# for key in wordB.keys():
#     if wordB[key] - wordA[key] > 0:
#        answer += (wordB[key] - wordA[key])
#
# print(answer)



# import sys
# from collections import Counter
#
# input = sys.stdin.readline
#
# wordA = Counter(input().rstrip())
# wordB = Counter(input().rstrip())
#
# answer = 0
# for key in wordA.keys():
#     if key in wordB.keys(): # 두 단어에 같은 문자가 포함되어 있는 경우
#         answer += abs(wordA[key] - wordB[key]) # 두 단어에 포함된 문자의 갯수의 차 만큼을 더한다.
#         wordB.pop(key) # wordB에서 해당 단어를 제거한다.
#     else:
#         answer += wordA[key] # wordA에만 포함된 단어인 경우, 단어의 갯수를 더한다.
#
# for value in wordB.values(): # wordB에 남은 단어의 갯수를 더한다.
#     answer += value
#
# print(answer)


