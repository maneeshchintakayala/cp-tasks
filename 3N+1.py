# Enter your code here. Read input from STDIN. Print output to STDOUT
i, j = map(int, input().split())

original_i, original_j = i, j

if i > j:
    i, j = j, i

def cycle_length(n):
    length = 1

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1

    return length

max_length = 0

for n in range(i, j + 1):
    max_length = max(max_length, cycle_length(n))

print(original_i, original_j, max_length)
