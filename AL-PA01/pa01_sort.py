import sys

input = sys.stdin.readline

method, k = map(int, input().split())


def update_heap(arr, idx, num):
    left = 2 * idx
    right = 1 + 2 * idx
    small_idx = idx
    if left <= num and arr[small_idx] > arr[left]:
        small_idx = left
    if right <= num and arr[small_idx] > arr[right]:
        small_idx = right
    if small_idx != idx:
        arr[idx], arr[small_idx] = arr[small_idx], arr[idx]
        return update_heap(arr, small_idx, num)


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
    sorted_arr = []
    cnt = 0
    for _ in range(n):
        arr.append(int(input()))
    length = len(arr)
    arr = [0] + arr
    for i in range(length, 0, -1):
        update_heap(arr, i, length)

    for i in range(length, 0, -1):
        cnt += 1
        sorted_arr.append(arr[1])
        arr[i], arr[1] = arr[1], arr[i]
        update_heap(arr, 1, i - 1)
        if cnt == k:
            break

    arr = arr[1:][:-k]
    for i in arr:
        print(i)

else:  # 퀵 정렬
    n = int(input())
    arr = []
    cnt = 0
    for _ in range(n):
        arr.append(int(input()))
