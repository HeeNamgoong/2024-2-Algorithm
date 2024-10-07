arr = [4, 3, 1, 5, 2, 6]

n = len(arr)
for i in range(n-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)