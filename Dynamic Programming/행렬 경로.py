matrix = [
    [6,7,12,5,],
    [5,3,11,18,],
    [7,17,3,3,],
    [8,10,14,9,]
] 


def matrix_path(matrix):
    n = len(matrix)
    dp = [[0] * n for _ in range(n)]

    def rec(i, j):
        print(dp)
        if i < 0 or j < 0: # 행렬 범위 벗어나면 리턴
            return 0
        if dp[i][j] != 0: # 값이 있으면
            return dp[i][j]
        dp[i][j] = max(rec(i-1, j), rec(i, j-1)) + matrix[i][j] # 왼쪽, 위쪽 + 자기자신

        return dp[i][j]

    return rec(n-1, n-1)

print(matrix_path(matrix))