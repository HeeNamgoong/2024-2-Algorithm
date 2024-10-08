def counting_sort(arr, r):
    cnts = [0] * r

    for x in arr:
        cnts[x] += 1

    for i in range(1, len(cnts)):
        cnts[i] += cnts[i-1]
    print(cnts)
    
    sorted = [0] * (len(arr))
    for x in reversed(arr):
        cnts[x] -= 1 # cnts[x] : 값이 들어갈 배열의 위치(인덱스)
        sorted[cnts[x]] = x
        print(cnts)
    arr[:] = sorted # 복사하는 거 까먹지 말자

    return arr # 배열 리턴하는 거 까먹지 말자





print(counting_sort([5, 1, 5, 1, 0, 4, 1, 2, 4, 5], 6))