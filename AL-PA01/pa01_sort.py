import sys

input = sys.stdin.readline


method, k = map(int, input().split())

if method == 1:  # 삽입 정렬
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    target = arr[k]
    sorted_arr = arr[:1]
    ready = arr[1:]
    ans = 0
    check = False
    cnt = 0
    while len(ready) > 0:
        if not check:
            # print(sorted_arr)
            # print(ready)
            # print("현재 비교 횟수:" + str(cnt))
            cur = ready.pop(0)
            for i in range(len(sorted_arr)):
                cnt += 1
                if cur <= sorted_arr[i]:
                    sorted_arr.insert(i, cur)
                    if cur == target:
                        check = True
                        print(cnt)
                    break
            else:
                cnt += 1
                sorted_arr.append(cur)
                if cur == target:
                    check = True
                    print(cnt)
        else:
            break

elif method == 2:  # 선택 정렬
    n = int(input())
    arr = []
    cnt = 0
    for _ in range(n):
        arr.append(int(input()))
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        cnt += 1
        if cnt == k:
            break
    for i in arr:
        print(i)

elif method == 3:  # 힙 정렬
    n = int(input())
    arr = []
    cnt = 0
    for _ in range(n):
        arr.append(int(input()))

else:  # 퀵 정렬
    n = int(input())
    arr = []
    cnt = 0
    for _ in range(n):
        arr.append(int(input()))

