# [6996] 애너그램 | Bronze 1 | 문자열, 정렬
'''
두 단어 A와 B가 주어졌을 때, A에 속하는 알파벳의 순서를 바꾸어서 B를 만들 수 있다면, A와 B를 애너그램이라고 한다.
두 단어가 애너그램인지 아닌지 구하는 프로그램을 작성하시오.
'''
T = int(input())
for _ in range(T) :
    A, B = input().split() # string
    A_list = sorted(list(A)) # string -> list 변환 후 정렬 ★
    B_list = sorted(list(B))

    if A_list == B_list : # list를 직접적으로 비교할 수 있음
        print("{} & {} are anagrams.".format(A, B))
    else :
        print("{} & {} are NOT anagrams.".format(A, B))