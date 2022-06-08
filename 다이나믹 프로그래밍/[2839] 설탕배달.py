# brute force
'''
kg = int(input())
l = []
for i in range(kg // 5 + 1) :
    for j in range(kg // 3 + 1) :
        if 5 * i + 3 * j == kg :
            l.append(i + j)
if len(l) == 0 : print(-1)
else : print(min(l))
'''
# dynamic programming
def DP(kg) :
    
    max_five = kg // 5 # 최대 5kg 봉투의 수
    for five in range(max_five, -1, -1) :
        three = (kg - five * 5) // 3
        if five * 5 + three * 3 == kg :
            return five + three
    return -1

print(DP(int(input())))