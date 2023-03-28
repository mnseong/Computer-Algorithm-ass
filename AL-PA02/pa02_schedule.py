import sys

input = sys.stdin.readline

p, n = map(int, input().split())
m = int(input())
schedule_dict = {}
research_list = [p for _ in range(n)]
noise_list = [0 for _ in range(n)]


def cal_partial_sum(array):
    length = len(array)
    dp = [0] * length
    dp[0] = array[0]
    for i in range(1, length):
        dp[i] = max(dp[i - 1] + array[i], array[i])
    return max(dp)


for i in range(m):
    t = int(input())
    arr = []
    for _ in range(t):
        tmp_arr = list(map(int, input().split()))
        arr.append(tmp_arr)
    schedule_dict[i + 1] = arr

for team in schedule_dict.values():
    for work in team:
        for i in range(work[0], work[1]):
            noise_list[i] += work[2]

for i in range(n):
    research_list[i] = research_list[i] + noise_list[i]

print(cal_partial_sum(research_list))
