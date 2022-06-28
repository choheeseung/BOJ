t = int(input())  # 테스트케이스

for _ in range(t):
    n = int(input())  # 동전의 가지 수
    coins = list(map(int, input().split()))  # 동전의 각 금액
    money = int(input())  # 만들어야 할 금액

    dp = [0 for i in range(money + 1)]
    dp[0] = 1

    for i in range(n):
        for j in range(coins[i], money + 1):
            dp[j] += dp[j-coins[i]]

    print(dp[money])
