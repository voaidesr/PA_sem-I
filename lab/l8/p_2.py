# pbinfo 3672
# dp[i+1] = min(dp[i]+1, dp[i+1])
# dp[2i] = min(dp[i]+1, dp[2i])
# dp[3i] = min (dp[i]+1, dp[3i])

def minim_operatii(n):
    if(n == 1):
        return 0
    dp = [n+1] * (3*n+1)
    dp[1] = 0
    for i in range(n+1):
        dp[i+1] = min(dp[i]+1, dp[i+1])
        dp[2*i] = min(dp[i]+1, dp[2*i])
        dp[3*i] = min (dp[i]+1, dp[3*i])
    return(dp[n])
n = int(input())
print(minim_operatii(n))