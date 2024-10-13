# k 자릿수 이하, 낮은 자릿수부터 높은 자릿수 순서대로 자릿수를 기준으로 안정 정렬
def radix_sort(arr, k, r):
    for i in range(k):
        stable_sort_by_digit(arr, i, r)
    return arr

    


def stable_sort_by_digit(arr, k, r):
    n = len(arr)
    cnts = [0] * r
    rtok = r ** k

    for x in arr:
        cnts[(x//rtok) % r] += 1

    for i in range(1, r):
        cnts[i] += cnts[i-1]
    
    sorted = [0] * n
    for x in reversed(arr):
        cnts[(x//rtok) % r] -= 1
        sorted[cnts[(x//rtok) % r]] = x

    arr[:] = sorted



print(radix_sort([123, 2154, 222, 4, 283, 1560, 1061, 2150], 4, 10))