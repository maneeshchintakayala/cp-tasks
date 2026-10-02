# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input().strip()
n = len(s)

# Build LPS (Longest Prefix Suffix) array
lps = [0] * n

j = 0
for i in range(1, n):
    while j > 0 and s[i] != s[j]:
        j = lps[j - 1]

    if s[i] == s[j]:
        j += 1
        lps[i] = j

# Length of the repeating pattern
p = n - lps[-1]

# It must divide the whole string
if n % p == 0:
    print(p)
else:
    print(n)
