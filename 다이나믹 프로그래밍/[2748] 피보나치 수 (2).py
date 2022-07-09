'''
[2748] 피보나치 수 (2) / Bronze 1 / 다이나믹 프로그래밍
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
n=17일때 까지 피보나치 수를 써보면 다음과 같다.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
'''

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
