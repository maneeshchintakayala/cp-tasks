dividend, divisor = map(int, input().split())

q = int(dividend / divisor)

INT_MAX = 2147483647
INT_MIN = -2147483648

if q > INT_MAX:
    print(INT_MAX)
elif q < INT_MIN:
    print(INT_MIN)
else:
    print(q)
