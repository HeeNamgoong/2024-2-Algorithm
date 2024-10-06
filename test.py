def heapsort(arr):
    # 배열을 힙으로 변환 (최대 힙 구성)
    build_heap(arr)
    
    n = len(arr)
    
    # 힙에서 가장 큰 값을 차례로 배열 끝에 배치
    for i in range(n-1, 0, -1):
        # 배열의 첫 번째 원소(최대값)와 마지막 원소를 교환
        arr[0], arr[i] = arr[i], arr[0]
        
        # 최대값을 제외한 나머지 부분에 대해 다시 힙 성질을 유지
        siftdown(0, arr, i)
    
    # 정렬된 배열 출력
    print(arr)

def siftdown(i, arr, n):
    # i 번째 원소의 왼쪽 자식 노드 인덱스 계산
    c = 2*i + 1 # left child
    
    # 자식 노드가 배열 범위 내에 있는 동안 계속 반복
    while c < n:
        # 오른쪽 자식 노드가 존재하고, 오른쪽 자식이 더 크면 오른쪽 자식 선택
        if c+1 < n and arr[c] < arr[c+1]:
            c = c+1 # right child 선택
        
        # 부모 노드가 자식 노드보다 크면 루프 종료 (힙 성질 유지)
        if arr[i] > arr[c]:
            break
        
        # 부모 노드와 자식 노드를 교환하여 힙 성질 유지
        arr[i], arr[c] = arr[c], arr[i]
        
        # 자식 노드를 새로운 부모 노드로 설정하고 계속해서 아래로 내려감
        i = c
        c = 2*i + 1 # 새로운 자식 노드 계산

def build_heap(arr):
    n = len(arr)
    
    # 배열의 중간부터 역순으로 내려가며 힙을 구성
    # 힙 성질을 위해 배열의 절반까지만 순회
    for i in range(n//2 - 1, -1, -1):
        siftdown(i, arr, n)

# heapsort 실행
heapsort([3, 1, 4, 5, 2])
