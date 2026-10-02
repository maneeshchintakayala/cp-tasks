# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

n,m=map(int,input().split())
g=[list(map(int,input().split())) for _ in range(n)]
q=deque()
fresh=0

for i in range(n):
    for j in range(m):
        if g[i][j]==2:
            q.append((i,j))
        elif g[i][j]==1:
            fresh+=1

time=0

while q and fresh:
    for _ in range(len(q)):
        i,j=q.popleft()
        for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            if 0<=x<n and 0<=y<m and g[x][y]==1:
                g[x][y]=2
                fresh-=1
                q.append((x,y))
    time+=1

print(time if fresh==0 else -1)
