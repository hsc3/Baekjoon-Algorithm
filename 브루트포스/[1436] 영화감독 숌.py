# [1436] 영화감독 숌 | Silver 5 | 브루트포스
'''
숌은 자신이 조지 루카스와 피터 잭슨을 뛰어넘는다는 것을 보여주기 위해서 영화 제목을 좀 다르게 만들기로 했다.
종말의 숫자란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수를 말한다. 제일 작은 종말의 숫자는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 과 같다.
따라서, 숌은 첫 번째 영화의 제목은 세상의 종말 666, 두 번째 영화의 제목은 세상의 종말 1666 이렇게 이름을 지을 것이다. 일반화해서 생각하면, N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 숫자) 와 같다.
숌이 만든 N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline
N = int(input()) # N은 10,000보다 작거나 같은 자연수이다.
# 59666 -> 60666 (o)  59666 -> 66600 (x)
num = 6
while True:
    if '666' in str(num):
        N -= 1
        if N == 0:
            break
    num += 1

print(num)

'''
n=int(input())
if n==1: print(666)          #규칙 예외: n=1인 경우, 1666이 아니라 그냥 666임
else:
    a = 0                    #앞에 더해질 숫자
    b = -1                   #뒤에 더해질 숫자
    count = 0                #a에서 일의 자리부터 n의 자리까지 6이 연속으로 발견된 숫자 
                             #ex: 166이면 2, 616이면 1, 660 이면 0임
        
    flaga = True             #a를 count시키라는 flag
    flagb = False            #b를 count시키라는 flag
    
    for i in range(1,n):
        if flaga:
            a+=1                
            stra = str(a)
            count = 0   
            #a의 값에 6이 존재하는지 확인
            for j in range(len(stra)-1,-1,-1):   
                if stra[j]=="6": count+=1 #일의 자리부터 6이 연속으로 발견될때마다 1씩 증가 
                else: break               #한번이라도 6이 아닌경우가 발생 할 시 증가 정지
                    
            if count>0:                   #연속된 6을 한번이라도 발견한 경우, b를 count하도록 바꾼다
                flaga = False
                flagb = True
         
        if flagb:
           b+=1
           if b == pow(10,count):         #b가 9,99,999...까지 센 경우 (어디까지 세어야하는 진 count가 힌트가 됨)
               b = -1                     #b값 초기화
               a+=1                       
               flaga = True
               flagb = False
      
    stra = str(a)
    strb = str(b)
 
    #a에 6이 발견되지 않은 경우와 동일. 조건식을 count==0으로 대체해도 된다.
    if strb == "-1":
         print(stra+"666")
         #그냥 a값에 666만 붙히면 된다
        
    #a에 6이 하나라도 발견되서 count된 경우, 케이스가 세개로 갈림
    elif strb != "-1":
         #뒤에 붙히는 b값의 자릿수 맞추기 (0 채워넣기)
         if b<pow(10,count-1):
            for i in range(0,count-1):
                strb="0"+strb   
                
         if count == 1: print(stra+"66"+strb)
         #a가 연속된 6이 한개밖에 없어서 추가적인 6을 두개 붙혀야 하는 경우      
         elif count == 2: print(stra+"6"+strb)
         #a가 연속된 6이 두개가 이미 존재해서 추가적인 6을 하나만 붙혀도 되는 경우                      
         else: print(stra+strb)  
         #a가 연속된 6이 세개가 이미 존재해서 추가적인 6을 덧붙힐 필요가 없는 경우
'''