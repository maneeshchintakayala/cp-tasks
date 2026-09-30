def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed"

    # Handle sign
    negative = (x < 0) ^ (y < 0)

    dividend = abs(x)
    divisor = abs(y)

    low = 0
    high = dividend
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        if mid * divisor == dividend:
            ans = mid
            break
        elif mid * divisor < dividend:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return -ans if negative else ans


# Input
x, y = map(int, input().split())

# Output
print(divide(x, y))
