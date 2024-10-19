# 정렬되지 않은 값 중 최대값을 찾아 맨 뒤로 보내는
# 인접한 두 값 반복하여 비교 and swap

arr = [4, 3, 1, 5, 2]
n = len(arr)

for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    print("최댓값 마지막으로", arr[n-i-1])
print(arr)

# 이 코드도 가능
# for i in range(n):
#     for j in range(n-i-1):