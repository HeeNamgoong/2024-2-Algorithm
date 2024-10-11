# 최대값을 찾아 맨 뒤로 보내는
arr = [4, 3, 1, 5, 2, 6]
n = len(arr)

for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)