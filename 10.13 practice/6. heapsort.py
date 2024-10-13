def heapsort(arr):
    n = len(arr)
    build_heap(arr, n)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sift_down(0, arr, i) ###
        
    return arr

def sift_down(i, arr, n):
    c = 2*i + 1
    
    while c < n:
        if c + 1 < n and arr[c] < arr[c+1]:
            c = c + 1
        if arr[c] < arr[i]: ###
            break
        arr[c], arr[i] = arr[i], arr[c]
        i = c
        c = 2*i + 1
            

def build_heap(arr, n):
    for i in range(n//2 - 1, -1, -1):
        sift_down(i, arr, n)


print(heapsort([73,6,57,88,60,42,83,72,48,85]))