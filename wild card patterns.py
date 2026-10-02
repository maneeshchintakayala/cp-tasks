# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input().strip()
p=input().strip()

i=j=0
star=-1
match=0

while i<len(s):
    if j<len(p) and (p[j]==s[i] or p[j]=='?'):
        i+=1
        j+=1
    elif j<len(p) and p[j]=='*':
        star=j
        match=i
        j+=1
    elif star!=-1:
        j=star+1
        match+=1
        i=match
    else:
        print(0)
        break
else:
    while j<len(p) and p[j]=='*':
        j+=1
    print(1 if j==len(p) else 0)
