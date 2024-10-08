def counting_sort(arr, r):
    n = len(arr)
    cnts = [0] * r

    for x in arr: # 각 값의 개수를 count
        cnts[x] += 1

    for i in range(1, r): # cumulate, 값이 마지막으로 들어간 위치의 다음자리 index
        cnts[i] += cnts[i-1]

    sorted = [0] * n
    for x in reversed(arr):
        cnts[x] -= 1 # 배열에 삽입을 위해 값을 1씩 감소
        sorted[cnts[x]] = x
    
    arr[:] = sorted

    return arr


print(counting_sort([5, 1, 5, 1, 0, 4, 1, 2, 4, 5], 6))