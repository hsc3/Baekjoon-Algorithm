# [2607] 비슷한 단어 | Silver 3 | 문자열
'''
영문 알파벳 대문자로 이루어진 두 단어가 다음의 두 가지 조건을 만족하면 같은 구성을 갖는다고 말한다.
1. 두 개의 단어가 같은 종류의 문자로 이루어져 있다.
2. 같은 문자는 같은 개수 만큼 있다.

두 단어가 같은 구성을 갖는 경우, 또는 한 단어에서 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우에 이들 두 단어를 서로 비슷한 단어라고 한다.
입력으로 여러 개의 서로 다른 단어가 주어질 때, 첫 번째 단어와 비슷한 단어가 모두 몇 개인지 찾아 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline
# 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어 같은 구성을 갖는다.
# -> 단어에서 하나의 문자만 달라야 한다.
def Compare(w1, w2):

    if len(w1) < len(w2):
        short_word, long_word = w1, w2
    else:
        short_word, long_word = w2, w1

    while short_word and long_word:
        word = short_word.pop(0) # 비교할 문자
        if word in long_word: # 두 단어에 모두 포함된 경우
            long_word.remove(word) # 긴 단어에서 해당 문자 제거

    return 1 if len(long_word) < 2 else 0 # 긴 단어의 길이가 2보다 짧으면 비슷한 문자 O


if __name__ == "__main__" :
    word = [list(input().rstrip()) for _ in range(int(input()))]

    answer = 0
    for i in range(1, len(word)):
        answer += Compare(word[0].copy(), word[i])

    print(answer)