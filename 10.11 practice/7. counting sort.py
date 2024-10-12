# 특정 값 r 이하의 수들이 몇 개 있는지 count해서 적절한 인덱스로 배열의 요소들을 보내주는 것
def counting_sort(arr, r):
    n = len(arr)
    cnts = [0] * r

    for x in arr:
        cnts[x] += 1

    for i in range(1, r):
        cnts[i] += cnts[i-1]
    
    sorted = [0] * n

    for x in reversed(arr):
        cnts[x] -= 1
        sorted[cnts[x]] = x # sorted[cnts[x]] += 1 이랬음... 어떤 값이 배열에 배치되는지 잘 파악하고 있어야지, 정렬하고 싶은 배열의 요소가 들어가겠죠
    
    arr = sorted[:]
    return arr



print(counting_sort([5, 1, 5, 1, 0, 4, 1, 2, 4, 5], 6))