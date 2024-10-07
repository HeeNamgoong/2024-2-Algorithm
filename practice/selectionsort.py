arr = [4, 3, 1, 5, 2, 6]

n = len(arr)

for i in range(n):
    min_ = i
    for j in range(i+1, n):
        if arr[min_] > arr[j]:
            min_ = j
    arr[i], arr[min_] = arr[min_], arr[i]

print(arr)
