# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    g, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return g, x, y


A, B = map(int, input().split())

D, x0, y0 = extended_gcd(A, B)

p = B // D
q = A // D

candidates = set()


for value, step in [(-x0, p), (y0, q)]:
    k = value // step
    candidates.add(k - 1)
    candidates.add(k)
    candidates.add(k + 1)

best = None

for k in candidates:
    x = x0 + k * p
    y = y0 - k * q

    current = (abs(x) + abs(y), x > y, x, y)

    if best is None or current < best[0]:
        best = (current, x, y)

x = best[1]
y = best[2]

print(x, y, D)
