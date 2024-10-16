import sys
input = sys.stdin.readline

N = int(input())
cnts = [0] * 10001 # 메모리 초과로 배열 길이 지정

for i in range(N):
    x = int(input())
    cnts[x] += 1

for num in range(1, 10001):
    if cnts[num] != 0:
        for cnt in range(cnts[num]): # 출력할 값의 개수
            print(num)
