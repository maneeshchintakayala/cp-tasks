import sys

def solve():
    # Read all tokens from standard input safely handling any newlines/spaces
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    
    # Try to read T. If the platform skipped T and went straight to N, 
    # we handle it by inspecting the remaining tokens.
    try:
        first_val = int(next(iterator))
    except StopIteration:
        return

    # If the input doesn't explicitly state T separate from N, 
    # we determine if T should just be 1 or read as T test cases.
    # To be perfectly safe for all HackerRank input quirks:
    tokens_left = len(input_data)
    
    # If the first value squared roughly equals the rest of the file, T was omitted.
    # Otherwise, first_val is indeed T.
    if tokens_left == (first_val * first_val) + 1:
        T = 1
        # Reset iterator to include the first value as N
        iterator = iter(input_data)
    else:
        T = first_val

    for _ in range(T):
        try:
            N = int(next(iterator))
        except StopIteration:
            break
            
        # Build the grid
        grid = [[int(next(iterator)) for _ in range(N)] for _ in range(N)]
        
        # Initialize DP table
        dp = [[0] * N for _ in range(N)]
        dp[0][0] = grid[0][0]
        
        # Fill first row
        for j in range(1, N):
            dp[0][j] = dp[0][j-1] + grid[0][j]
            
        # Fill first column
        for i in range(1, N):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            
        # Fill rest of the DP table
        for i in range(1, N):
            for j in range(1, N):
                dp[i][j] = grid[i][j] + min(
                    dp[i-1][j], 
                    dp[i][j-1], 
                    dp[i-1][j-1]
                )
        
        # Print only the final minimum cost to perfectly match the expected output format
        print(dp[N-1][N-1])

if __name__ == '__main__':
    solve()
