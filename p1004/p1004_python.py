n = int(input().strip())
# 初始化网格，大小为(n+1) x (n+1)，索引从1到n
a = [[0] * (n + 1) for _ in range(n + 1)]
# 读取输入直到(0,0,0)
data = list(map(int, input().split()))
x, y, z = data[0], data[1], data[2]
while x != 0 or y != 0 or z != 0:
    a[x][y] = z
    data = list(map(int, input().split()))
    x, y, z = data[0], data[1], data[2]
    
# 初始化四维dp数组，大小为(n+1) x (n+1) x (n+1) x (n+1)
f = [[[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
    
# 动态规划处理
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            for l in range(1, n + 1):
                # 计算四种可能的上一步组合的最大值
                MAX_val = max(
                    f[i - 1][j][k - 1][l],
                    f[i - 1][j][k][l - 1],
                    f[i][j - 1][k - 1][l],
                    f[i][j - 1][k][l - 1]
                )
                # 加上当前两个位置的数值
                f[i][j][k][l] = MAX_val + a[i][j] + a[k][l]
                # 如果两个路径走到同一位置，需减去重复值
                if i == k and j == l:
                    f[i][j][k][l] -= a[i][j]
    
print(f[n][n][n][n])

