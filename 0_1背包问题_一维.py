n, package_size = map(int, input().split())

material_sizes = list(map(int, input().split()))
material_value = list(map(int, input().split()))

dp = [0] * (package_size + 1)
    
for i in range(n):
    for j in range(package_size, -1, -1):
        if material_sizes[i] <= j:
            dp[j] = max(dp[j], dp[j - material_sizes[i]] + material_value[i])
        else:
            dp[j] = dp[j]
print(dp[package_size])

# 用每个物品依次遍历DP数组，所以当前「J」就是获得了上次的「记忆」