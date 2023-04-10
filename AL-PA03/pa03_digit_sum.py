import itertools

n = int(input())


# string 형의 수가 주어졌을 때, 각 자릿수의 합을 더해서 반환하는 함수
def sum_digits(num):
    return sum(map(int, num))


# 원소 2개를 가진 tuple들을 원소로 가진 list가 주어졌을 때, 각 tuple의 두 원소의 합이 최대인 값을 구해서 반환하는 함수
def cal_max_sum(lst):
    max_sum = -1
    for tpl in lst:
        curr_sum = sum_digits(tpl[0]) + sum_digits(tpl[1])
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum


# tuple에서 중복된 원소를 제거하고, 첫 번째 원소 기준으로 오름차순 정렬하여 반환하는 함수
def sort_tuples(lst):
    sorted_tuples = [tuple(sorted(t)) for t in lst]
    return sorted(list(set(sorted(sorted_tuples))), key=lambda tpl: int(tpl[0]))


numbers = []  # 합이 n인 경우를 저장할 list
combinations = itertools.combinations(range(10), 6)  # combinations를 이용해 0~9까지의 자연수 중에서 6개를 뽑는 모든 경우의 수

# 뽑은 6개의 수를 세개씩 나누어 num1, num2로 분리시키고 더해서, n값이면 numbers에 저장한다.
for comb in combinations:
    for numbers1 in itertools.permutations(comb, 3):
        for numbers2 in itertools.permutations(set(comb) - set(numbers1), 3):
            num1 = str(numbers1[0]) + str(numbers1[1]) + str(numbers1[2])
            num2 = str(numbers2[0]) + str(numbers2[1]) + str(numbers2[2])
            if int(num1) + int(num2) == n:
                numbers.append((num1, num2))

numbers = sort_tuples(numbers)  # 위에서 정의한 sort_tuples 함수로 numbers 를 중복 제거 및 오름차순 정렬 시킨다.
m_sum = cal_max_sum(numbers)  # 위에서 정의한 cal_max_sum 함수로 numbers에서 각 원소의 합의 최대값을 구한다.
result = ()  # 결과를 반환할 tuple

# numbers의 원소 전체를 순회하며 각 원소(tuple)을 구성하는 원소들의 합이 m_sum값과 같은지 확인 후, 같으면 그 값을 result에 저장하고 즉시 break
# numbers를 첫 번째 수 기준으로 정렬시켰기 때문에, break 하면 각 자리의 합이 최대가 되는 수가 여러 개라도 가장 작은 수가 포함된 경우가 출력된다.
for number in numbers:
    n1, n2 = number
    if sum_digits(n1) + sum_digits(n2) == m_sum:
        result = (n1, n2)
        break

# 문제의 조건을 만족하는 분리된 두 수와, 각 자리의 합이 최대가 되는 두 수를 출력한다.
# 만약 분리되는 수가 존재하지 않으면 numbers가 비어있는 list일 것이므로, m_sum 값이 -1
print(f"{result[0]} {result[1]} {m_sum}" if m_sum != -1 else m_sum)
