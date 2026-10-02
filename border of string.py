# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input().strip()
n = len(s)
lps = [0] * n
length = 0
i = 1
while i < n:
    if s[i] == s[length]:
        length += 1
        lps[i] = length
        i += 1
    elif length > 0:
        length = lps[length - 1]
    else:
        lps[i] = 0
        i += 1
border_length = lps[-1]
if border_length == 0:
    print(-1)
else:
    print(s[:border_length])
