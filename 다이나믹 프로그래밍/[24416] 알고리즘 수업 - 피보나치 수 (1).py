# [24416] 알고리즘 수업 - 피보나치 수 (1) | Bronze 1 | 다이나믹 프로그래밍
'''
오늘은 n의 피보나치 수를 재귀호출과 동적 프로그래밍으로 구하는 알고리즘을 배웠다. 재귀호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해 보자.
아래 의사 코드를 이용하여 n의 피보나치 수를 구할 경우 코드1 코드2 실행 횟수를 출력하자.

- 재귀호출 의사 코드
fib(n) {
    if (n = 1 or n = 2)
    then return 1;  # 코드1
    else return (fib(n - 1) + fib(n - 2));
}

- 동적 프로그래밍 의사 코드
fibonacci(n) {
    f[1] <- f[2] <- 1;
    for i <- 3 to n
        f[i] <- f[i - 1] + f[i - 2];  # 코드2
    return f[n];
}
'''

def fibCnt(n):
    dp = [0] * n
    dp[:2] = [1, 1]

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n-1]

if __name__ == "__main__":
    n = int(input())
    print(fibCnt(n), n-2)