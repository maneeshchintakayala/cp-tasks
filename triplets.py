# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()
found = False
for i in range(n - 2):
    # Skip duplicate first elements
    if i > 0 and arr[i] == arr[i - 1]:
        continue
    left = i + 1
    right = n - 1
    while left < right:
        total = arr[i] + arr[left] + arr[right]
        if total == x:
            print(arr[i], arr[left], arr[right])
            found = True
            # Skip duplicate values
            left_val = arr[left]
            right_val = arr[right]
            while left < right and arr[left] == left_val:
                left += 1
            while left < right and arr[right] == right_val:
                right -= 1
        elif total < x:
            left += 1
        else:
            right -= 1
if not found:
    print("No Triplet Found")
