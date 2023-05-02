def flip(arr, i, j):
    tmp = arr[:]
    tmp[i:j + 1] = [-x for x in reversed(tmp[i:j + 1])]
    return tmp


def check_one(arr):
    target = [x + 1 for x in range(len(arr))]
    start = arr.index(min(arr))
    end = 0
    for i in range(1, len(arr) + 1):
        if -i in arr:
            end = arr.index(-i)
            break
    res = flip(arr, start, end)
    if res == target:
        return True
    return False


def check_continuous_subarrays(arr):
    n = len(arr)
    i = 0
    sub_arrays = []
    while i < n:
        j = i + 1
        while j < n and arr[j] == arr[j - 1] + 1:
            j += 1
        if j > i:
            sub_arrays.append((i, j))
            if check_one(flip(arr, i, j - 1)):
                return True
        i = j
    if check_one(flip(arr, sub_arrays[0][0], sub_arrays[1][1] - 1)):
        return True
    if check_one(flip(arr, sub_arrays[0][0], sub_arrays[2][1] - 1)):
        return True
    if check_one(flip(arr, sub_arrays[1][0], sub_arrays[2][1] - 1)):
        return True
    if check_one(flip(arr, sub_arrays[1][0], sub_arrays[3][1] - 1)):
        return True
    if check_one(flip(arr, sub_arrays[2][0], sub_arrays[3][1] - 1)):
        return True
    return False


def check_two(arr):
    if check_continuous_subarrays(arr):
        return True
    return False


def check(arr):
    if check_one(arr):
        print('one')
    elif check_two(arr):
        print('two')
    else:
        print('over')


n = int(input())
target = [x + 1 for x in range(n)]
bread_tray = []

for i in range(5):
    tmp_arr = list(map(int, input().split()))
    bread_tray.append(tmp_arr)

for arr in bread_tray:
    check(arr)
