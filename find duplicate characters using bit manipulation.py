# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input().strip()
seen = 0
duplicates = 0
result = []
for c in s:
    bit = 1 << (ord(c) - ord('a'))
    if seen & bit:
        if not (duplicates & bit):
            result.append(c)
            duplicates |= bit
    else:
        seen |= bit
if result:
    print(*result)
else:
    print("No duplicates")
