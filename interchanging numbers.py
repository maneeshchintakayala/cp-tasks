n = int(input())
arr = list(map(int, input().split()))

min_index = arr.index(min(arr))
max_index = arr.index(max(arr))

arr[min_index], arr[max_index] = arr[max_index], arr[min_index]

print(*arr)
