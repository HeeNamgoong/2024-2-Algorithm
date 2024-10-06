def heapsort(arr):
    build_heap(arr)
    n = len(arr)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] # arr[0]: 최상단 max node
        siftdown(0, arr, i)
    print(arr)

def siftdown(i, arr, n):
    c = 2*i + 1 # left child
    while c < n: # 자식 노드가 배열 범위 내에 있는 동안 계속 반복
        if c+1 < n and arr[c] < arr[c+1]: # 오른쪽 자식 노드가 존재하고, 오른쪽 자식이 더 크면 오른쪽 자식 선택
            c = c+1 # right child
        if arr[i] > arr[c]: # 부모, 자식 노드 비교
            break
        arr[i], arr[c] = arr[c], arr[i]
        i = c
        c = 2*i + 1 

def build_heap(arr):
    n = len(arr)
    # 배열의 중간부터 역순으로 내려가며 힙을 구성
    # 힙 성질을 위해 배열의 절반까지만 순회
    # (n//2) - 1 ~ 0  : 부모 노드 /  그 이후는 leaf node인데 leaf node는 힙 성질을 유지할 필요가 없어서
    for i in range((n//2) - 1 , -1, -1):
        siftdown(i, arr, n)

heapsort([3, 1, 4, 5, 2])