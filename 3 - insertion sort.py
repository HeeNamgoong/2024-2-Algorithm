unsorted = [3, 1, 4, 2, 5]

n = len(unsorted)
for i in range(1, n):
    for j in range(i, 0, -1):
        if unsorted[j-1] <= unsorted[j]:
            break
        unsorted[j-1], unsorted[j] = unsorted[j], unsorted[j-1]


print(unsorted)