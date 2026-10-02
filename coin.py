import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    V = int(input_data[0])
    N = int(input_data[1])
    coins = [int(x) for x in input_data[2:2+N]]
    dp = [V + 1] * (V + 1)
    dp[0] = 0  
    for i in range(1, V + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[V] > V:
        print("-1")
    else:
        print(dp[V])
if __name__ == '__main__':
    solve()
