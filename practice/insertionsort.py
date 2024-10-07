arr = [3, 4, 6, 2, 7, 1, 5, 8]

n = len(arr)
for i in range(1, n):
    for j in range(i, 0, -1):
        if arr[j-1] <= arr[j]:
            break
        arr[j-1], arr[j] = arr[j], arr[j-1]

print(arr)