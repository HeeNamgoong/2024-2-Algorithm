def heap_sort(arr):
    build_heap(arr)

    n = len(arr)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sift_down(0, arr, i) # sift_down(i, arr, n) 이라고 했음, 0 이어야하는 이유 : 루트 노드의 자식 노드의 인덱스를 알려주는 인자값인데 당연히 2*0 + 1 이지!!
    return arr

def sift_down(i, arr, n):
    c = 2*i + 1
    while c < n: # 자식 노드가 배열 안에 들어있을 동안
        if c + 1 < n and arr[c] < arr[c+1]:
            c = c + 1 # 오른쪽 자식 선택
        if arr[i] > arr[c]: # 부모, 자식 노드 비교
            break
        arr[i], arr[c] = arr[c], arr[i] # 부모 노드와 자식 노드 swap
        
        i = c
        c = 2*i + 1 



def build_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        sift_down(i, arr, n)

print(heap_sort([3, 1, 4, 5, 2]))