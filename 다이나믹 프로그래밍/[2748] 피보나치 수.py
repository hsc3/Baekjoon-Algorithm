# Q : n번째 피보나치 수를 출력하라

# 1. Dynamic Programming with Memoization
def fibo_memoization(n) :
    memo[0] = 0
    memo[1] = 1

    for i in range(2, n + 1) :
        memo[i] = memo[i - 2] + memo[i - 1]
    return memo[n]

n = int(input())
memo = [0 for _ in range(n + 1)]
print(fibo_memoization(n))

#2. Top-Down --> using recursion
'''def fibo_top_down(n) :

    if n <= 1 :
        return n # memo[0] = 0 , memo[1] = 1
    
    if memo[n] != 0 :
        return memo[n]

    memo[n] = fibo_top_down(n - 2) + fibo_top_down(n - 1)
    return memo[n]
    
n = int(input())
memo = [0 for _ in range(n + 1)]
print(fibo_top_down(n))'''

#3. Bottom-Up --> for문
'''def fibo_bottom_up(n) :
    if n <= 1 :
        return n
    
    fir = 0
    sec = 1
    for i in range(0, n - 1) :
        next = fir + sec
        fir = sec
        sec = next
    return next

n = int(input())
print(fibo_bottom_up(n))'''