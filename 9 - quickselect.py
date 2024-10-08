def quickselect(arr, l, r, i):
    if l+1 >= r:
        return arr[l] # 배열의 남은 부분이 하나 일때, ex) l=3, r=4 -> arr[3] 리턴
    
    p = partition(arr, l, r)

    if p == i: # pivot이랑 같으면 바로 pivot 리턴
        return arr[p]
    elif i < p: # pivot보다 작은 곳에 있으면 pivot보다 작은 부분 재귀
        return quickselect(arr, l, p, i)
    elif i > p:
        return quickselect(arr, p+1, r, i)

def partition(arr, l, r):
    p = arr[r-1]

    i = l
    for j in range(l, r): 
        if arr[j] <= p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return i - 1
    

print(quickselect([11, 1, 9, 2, 7, 13, 12, 8, 6, 3, 10], 0, 11, 3))
