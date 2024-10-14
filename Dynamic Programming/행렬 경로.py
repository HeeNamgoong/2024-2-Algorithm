matrix = [
    [6,7,12,5,],
    [5,3,11,18,],
    [7,17,3,3,],
    [8,10,14,9,]
] 

### memoization 재귀 호출 ###
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
##############################


### tabulation 동적 프로그래밍 ###

def matrix_path(matrix):
    n = len(matrix)
    dp = [[0] * (n+1) for _ in range(n+1)] # 행렬 범위 벗어나는 index error 방지하기 위해 padding 줌

    for i in range(n):
        for j in range(n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]

    return dp[i][j]

print(matrix_path(matrix))