import sys
input = sys.stdin.readline

method, k = map(int, input().split())

pivot_cnt = 0


def update_heap(array, idx, num):
    left = 2 * idx
    right = 1 + 2 * idx
    small_idx = idx
    if left <= num and array[small_idx] >= array[left]:
        small_idx = left
    if right <= num and array[small_idx] >= array[right]:
        small_idx = right
    if small_idx != idx:
        array[idx], array[small_idx] = array[small_idx], array[idx]
        update_heap(array, small_idx, num)


def is_sorted(array):
    if array == sorted(array):
        return True
    else:
        return False


def quick_sort(array, start, end):
    global pivot_cnt
    if start >= end:
        return
    pivot = start
    if pivot_cnt > k:
        return
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] > array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
            pivot_cnt += 1
            if pivot_cnt == k or is_sorted(array):
                for a in array:
                    print(a)
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


if method == 1:  # 삽입 정렬
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    cnt = 0
    for i in range(1, k + 1):
        for j in range(i, 0, -1):
            cnt += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    print(cnt)

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
    arr, tmp = [], []
    sorted_arr = []
    for _ in range(n):
        arr.append(int(input()))
    length = len(arr)
    arr = [0] + arr
    for i in range(length, 0, -1):
        update_heap(arr, i, length)
    for i in range(length, 0, -1):
        sorted_arr.append(arr[1])
        arr[i], arr[1] = arr[1], arr[i]
        arr.pop()
        tmp = arr
        update_heap(arr, 1, i - 1)
        if len(sorted_arr) == k:
            break
    tmp = tmp[1:]
    for i in tmp:
        print(i)

elif method == 4:  # 퀵 정렬
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    quick_sort(arr, 0, len(arr) - 1)
