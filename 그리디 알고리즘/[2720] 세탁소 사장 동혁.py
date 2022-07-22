# [2720] 세탁소 사장 동혁 / Bronze 3 / 그리디 알고리즘
'''
거스름돈의 액수가 주어지면 리암이 줘야할 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)의 개수를 구하는 프로그램을 작성하시오.
거스름돈은 항상 $5.00 이하이고, 손님이 받는 동전의 개수를 최소로 하려고 한다. 예를 들어, $1.24를 거슬러 주어야 한다면, 손님은 4쿼터, 2다임, 0니켈, 4페니를 받게 된다.
'''
def calProgram(money, q, d, n, p) :

    if money == 0 : return [q, d, n, p]

    if money >= 25 :
        return calProgram(money-25, q+1, d, n, p)
    elif money >= 10 :
        return calProgram(money-10, q, d+1, n, p)
    elif money >= 5 :
        return calProgram(money-5, q, d, n+1, p)
    elif money >= 1 :
        return calProgram(money-1, q, d, n, p+1)

T = int(input()) # test case
for _ in range(T) :
    result = calProgram(int(input()), 0, 0, 0, 0)
    for n in result :
        print(n, end = ' ')
    print()