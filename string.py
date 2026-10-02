A = input().strip()

n = len(A)
B = A[::-1]

prev = [0] * (n + 1)

for i in range(1, n + 1):
    curr = [0] * (n + 1)

    for j in range(1, n + 1):
        if A[i - 1] == B[j - 1]:
            curr[j] = 1 + prev[j - 1]
        else:
            curr[j] = max(prev[j], curr[j - 1])

    prev = curr

print(prev[n])
