# 정렬된 값들과 비교하여 적절한 자리를 찾아가는
# best case때 최적의 알고리즘을 위해 반복문 break 있어야함!
# + 값이 같아도 swap하지 않아도 됨 -> break  : stable sort이다
arr = [4, 3, 1, 5, 2, 6]
n = len(arr)

for i in range(1, n):
    for j in range(i, 0, -1):
        if arr[j-1] <= arr[j]:
            break
        arr[j-1], arr[j] = arr[j], arr[j-1]
        print(arr)
print(arr)