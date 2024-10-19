# 정렬되지 않은 값들 중, 최솟값을 찾아 맨 앞으로 보내는
arr = [4, 3, 1, 5, 2, 6]
n = len(arr)

min_ = 0
for i in range(n):
    min_ = i
    for j in range(i+1, n):
        if arr[min_] > arr[j]:
            min_ = j
    arr[min_], arr[i] = arr[i], arr[min_]
    print(arr)
print(arr)