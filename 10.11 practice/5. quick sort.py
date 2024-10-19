# pivot을 기준으로 영역을 나눠 각각 정렬

def quick_sort(arr, l, r):
    if l+1 >= r:
        return
    
    p = partition(arr, l, r)
    print("현재 pivot 인덱스", p) # p - 1 하면 다음 피봇의 위치
    print()
    quick_sort(arr, l, p)
    quick_sort(arr, p+1, r)

    return arr

def partition(arr, l, r):
    p = arr[r-1] # pivot
    print("pivot", p)
    i = l
    for j in range(l, r):
        if arr[j] <= p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        print(arr) # 피봇과 비교해서 작거나 같으면 swap된 결과 잘 보세요
    return i - 1


print(quick_sort([4, 3, 1, 8, 7, 2, 5, 6], 0, 8))
