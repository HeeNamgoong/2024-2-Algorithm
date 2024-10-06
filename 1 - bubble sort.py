unsorted = [3, 1, 4, 2, 5]

n = len(unsorted)
for i in range(n-1, 0, -1):
    for j in range(i):
        if unsorted[j] > unsorted[j+1]:
            unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]

print(unsorted)