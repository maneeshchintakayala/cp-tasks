# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n=int(input())
a=list(map(int,input().split()))
s=sum(a)
k=n//2
ans=10**9

for c in combinations(a,k):
    ans=min(ans,abs(s-2*sum(c)))

if n%2:
    for c in combinations(a,k+1):
        ans=min(ans,abs(s-2*sum(c)))

print(ans)
