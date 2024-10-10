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
