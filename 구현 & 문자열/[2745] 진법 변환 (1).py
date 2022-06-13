# [2745] 진법 변환 (1)
# Bronze 2 >> 수학, 구현, 문자열

N, B = input().split()

res = 0

for i in range(len(N)) :
    if N[i].isalpha() :
        num = ord(N[i]) - 55
    else : 
        num = int(N[i])

    res += num * (int(B) ** (len(N)-i-1))

print(res)

'''
N, B= map(str, input().split())
B = int(nota)
print(int(N, B))
'''