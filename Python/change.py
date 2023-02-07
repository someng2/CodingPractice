def solution(n, money):
    money = list(filter(lambda x: x<=n, money))
    dp = [0] * (n+1)
    
    for coin in money:
        dp[coin] += 1
        for price in range(coin+1, n+1):
            dp[price] += dp[price-coin]
                
    return dp[n] % 1000000007
