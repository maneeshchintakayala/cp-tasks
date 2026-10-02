n = int(input())
words = input().split(',')
pattern = input().strip()

matches = []

for word in words:
    upper = ''.join(c for c in word if c.isupper())

    # Pattern must match as a subsequence
    j = 0
    for c in upper:
        if j < len(pattern) and c == pattern[j]:
            j += 1

    if j == len(pattern):
        matches.append(word)

# Sort lexicographically
matches.sort()

if matches:
    for word in matches:
        print(word)
else:
    print("No match found")
