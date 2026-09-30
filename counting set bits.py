# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

count = 0
while n:
    n = n & (n - 1)
    count += 1

print(count)
