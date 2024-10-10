n, package_size = map(int, input().split())

material_sizes = list(map(int, input().split()))
material_value = list(map(int, input().split()))

dp = [[0] * (package_size + 1) for _ in range(n)]

for j in range(material_sizes[0], package_size + 1):
    dp[0][j] = material_value[0]
    
for i in range(1, n):
    for j in range(package_size + 1):
        if material_sizes[i] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - material_sizes[i]] + material_value[i])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[n - 1][package_size])

# 「I」的含义：第「I」件物品
# 「J」的含义：背包第「J」大
# 背包要从「0」开始，扩展到「X」是在「模拟」背包装了物品若干后，剩下的大小