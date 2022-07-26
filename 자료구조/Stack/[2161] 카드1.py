# [2161] 카드1 | Bronze 1 | 자료구조(stack)
'''
N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며,
1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
N이 주어졌을 때, 버린 카드들을 순서대로 출력하고, 마지막에 남게 되는 카드를 출력하는 프로그램을 작성하시오.
'''

def Solution(N) :
    stk = [n for n in range(1, N+1)]
    ans = []

    while True :
        ans.append(stk.pop(0))
        if not stk :
            break
        stk.append(stk.pop(0))

    print(*ans, sep = ' ')

if __name__ == "__main__" :
    Solution(int(input()))