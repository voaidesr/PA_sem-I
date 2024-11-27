# pbinfo 3672
# dp[i+1] = min(dp[i]+1, dp[i+1])
# dp[2i] = min(dp[i]+1, dp[2i])
# dp[3i] = min (dp[i]+1, dp[3i])

def minim_operatii(n):
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # Base case: 0 operations to get 1

    # Fill the DP table
    for x in range(2, n + 1):
        dp[x] = dp[x - 1] + 1  # Add 1
        if x % 2 == 0:
            dp[x] = min(dp[x], dp[x // 2] + 1)  # Multiply by 2
        if x % 3 == 0:
            dp[x] = min(dp[x], dp[x // 3] + 1)  # Multiply by 3

    return dp[n]
n = int(input())
print(minim_operatii(n))