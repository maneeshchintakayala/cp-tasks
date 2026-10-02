def binary_gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1
    while (a & 1) == 0:
        a >>= 1
    while b != 0:
        while (b & 1) == 0:
            b >>= 1
        if a > b:
            a, b = b, a
        b = b - a
    return a << shift
A, B, T = map(int, input().split())
g = binary_gcd(A, B)
if T == 0 or (T <= max(A, B) and T % g == 0):
    print("YES")
else:
    print("NO")
