unsorted = [3,4,6,2,7,1,5,8]

n = len(unsorted)
for i in range(n):
    min_ = i
    for j in range(i+1, n):
        if unsorted[min_] > unsorted[j]:
            min_ = j
    unsorted[min_], unsorted[i] = unsorted[i], unsorted[min_]    

print(unsorted)