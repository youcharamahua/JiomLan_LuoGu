n = int(input().strip())
# ��ʼ�����񣬴�СΪ(n+1) x (n+1)��������1��n
a = [[0] * (n + 1) for _ in range(n + 1)]
# ��ȡ����ֱ��(0,0,0)
data = list(map(int, input().split()))
x, y, z = data[0], data[1], data[2]
while x != 0 or y != 0 or z != 0:
    a[x][y] = z
    data = list(map(int, input().split()))
    x, y, z = data[0], data[1], data[2]
    
# ��ʼ����άdp���飬��СΪ(n+1) x (n+1) x (n+1) x (n+1)
f = [[[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
    
# ��̬�滮����
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            for l in range(1, n + 1):
                # �������ֿ��ܵ���һ����ϵ����ֵ
                MAX_val = max(
                    f[i - 1][j][k - 1][l],
                    f[i - 1][j][k][l - 1],
                    f[i][j - 1][k - 1][l],
                    f[i][j - 1][k][l - 1]
                )
                # ���ϵ�ǰ����λ�õ���ֵ
                f[i][j][k][l] = MAX_val + a[i][j] + a[k][l]
                # �������·���ߵ�ͬһλ�ã����ȥ�ظ�ֵ
                if i == k and j == l:
                    f[i][j][k][l] -= a[i][j]
    
print(f[n][n][n][n])

