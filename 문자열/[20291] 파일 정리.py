'''
[20291] 파일 정리 / Silver 3 / 문자열, 파싱, 자료구조
스브러스의 요청은 다음과 같다.
- 파일을 확장자 별로 정리해서 몇 개씩 있는지 알려줘.
- 보기 편하게 확장자들을 사전 순으로 정렬해 줘.
그럼 보물의 절반을 얻어내기 위해 얼른 스브러스의 노트북 파일 정리를 해줄 프로그램을 만들자!
'''
import sys
from collections import Counter
input = sys.stdin.readline

extensionList = [input().rstrip().split('.')[1] for _ in range(int(input()))] # 확장자를 입력받는다.
extensionCount = sorted(list(Counter(extensionList).items())) # 확장자명을 기준으로 count하고, 사전 순으로 정렬한다.

for extension, count in extensionCount :
    print(extension, count)