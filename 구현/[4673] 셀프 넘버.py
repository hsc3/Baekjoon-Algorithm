'''
[4673] 셀프 넘버 / Silver 5 / 구현, 수학, 브루트포스
양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자. 예를 들어, d(75) = 75+7+5 = 87이다.
양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다. 
n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고, 39는 51의 생성자, 51은 57의 생성자이다. 생성자가 한 개보다 많은 경우도 있다.
생성자가 없는 숫자를 셀프 넘버라고 한다.
10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''
def d(n) :
    generator = n
    for num in str(n) :
        generator += int(num)

    return generator

if __name__ == "__main__" :

    check = [False] * 10001
    allNumber = set(range(1, 10001))
    notSelfNumber = set()

    for i in range(1, 10001) :
        notSelfNumber.add(d(i))

    print(*sorted(allNumber - notSelfNumber), sep = '\n')

'''
def d(n) :
    global selfNum, check

    generator = n 

    for num in str(n) :
        generator += int(num)

    if generator > 10000 : 
        return

    selfNum[generator] = False 
    check[generator] = True    

    return d(generator)


if __name__ == "__main__" :
    
    selfNum = [True] * 10001 
    check = [False] * 10001

    for i in range(1, 10001) :
        if not check[i] :
            d(i) 

    for i in range(1, 10001) :
        if selfNum[i] :
            print(i)
'''