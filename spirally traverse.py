# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]

t,b,l,r=0,n-1,0,m-1
ans=[]

while t<=b and l<=r:
    for j in range(l,r+1): ans.append(a[t][j])
    t+=1
    for i in range(t,b+1): ans.append(a[i][r])
    r-=1
    if t<=b:
        for j in range(r,l-1,-1): ans.append(a[b][j])
        b-=1
    if l<=r:
        for i in range(b,t-1,-1): ans.append(a[i][l])
        l+=1

print(*ans)
