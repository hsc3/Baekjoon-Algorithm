'''
[1269] 대칭 차집합 | Silver 4 | 자료구조 (Set)
자연수를 원소로 갖는 공집합이 아닌 두 집합 A와 B가 있다. 이때, 두 집합의 대칭 차집합의 원소의 개수를 출력하는 프로그램을 작성하시오. 
두 집합 A와 B가 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.
'''
import sys; input = sys.stdin.readline
A, B = map(int, input().split())
aSet = set(map(int, input().split()))
bSet = set(map(int, input().split()))
And = aSet & bSet
print(len(aSet-And) + len(bSet-And)) # 대칭 차집합

'''
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
ll a[202020], b[202020];
void solve() {
	ll asize, bsize;
	cin >> asize >> bsize;
	for (ll i = 0; i < asize; i++)
		cin >> a[i];
	for (ll i = 0; i < bsize; i++) {
		cin >> b[i];
	}
	sort(a, a + asize);
	sort(b, b + bsize);
	ll ans = asize + bsize;
	ll i = 0, j = 0;
	while (i < asize && j < bsize) {
		if (a[i] == b[j]) {
			i++;
			j++;
			ans -= 2;
		}
		else {
			a[i] < b[j] ? i++ : j++;
		}
	}
	cout << ans << '\n';

}
int main() {
	cin.tie(NULL); cout.tie(NULL); ios_base::sync_with_stdio(false);
	solve();
	return 0;
}
'''