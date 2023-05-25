def rabin_karp(pattern, text):
    m = len(pattern)
    n = len(text)
    d = 2
    q = 30011
    h = pow(d, m - 1) % q

    p = 0
    t = 0

    comparisons = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        comparisons += 1
        if p == t:
            for j in range(m):
                comparisons += 1
                if text[i + j] != pattern[j]:
                    break
            else:
                break

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q

            if t < 0:
                t = (t + q)

    return comparisons


def kmp(pattern, text):
    p = len(pattern)
    t = len(text)

    # 패턴의 실패 함수를 계산하는 함수
    def compute_failure_function(pattern):
        failure = [0] * p
        i = 1
        j = 0
        while i < p:
            if pattern[i] == pattern[j]:
                j += 1
                failure[i] = j
                i += 1
            elif j > 0:
                j = failure[j - 1]
            else:
                failure[i] = 0
                i += 1
        return failure

    failure = compute_failure_function(pattern)
    i = 0
    j = 0
    comparisons = 0  # 비교 횟수 초기화

    while i < t:
        comparisons += 1  # 문자 비교 횟수 증가
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == p:
                # 패턴이 일치하는 경우
                return comparisons
        else:
            if j > 0:
                j = failure[j - 1]
            else:
                i += 1

    return comparisons


def compute_jump(pattern):
    jump = {}
    pattern_length = len(pattern)

    for i in range(pattern_length - 1):
        jump[pattern[i]] = pattern_length - i - 1

    return jump


def boyer_moore(pattern, text):
    jump = compute_jump(pattern)
    # print(jump)
    n = len(text)
    m = len(pattern)
    i = 0
    comparisons = 0

    while i <= n - m:
        j = m - 1
        while j >= 0:
            comparisons += 1
            if pattern[j] == text[i + j]:
                j -= 1
            else:
                if text[i + m - 1] in jump:
                    jump_step = jump[text[i + m - 1]]
                else:
                    jump_step = m
                i += max(jump_step, j - (m - 1 - jump_step))
                break
        else:
            return comparisons


# 입력 처리
pattern_count = int(input())  # 패턴 개수
patterns = ''
for _ in range(pattern_count):
    patterns += input()
text_count = int(input())  # 텍스트 줄 수
text = ''
for _ in range(text_count):
    text += input()

rk_val = rabin_karp(patterns, text)
kmp_val = kmp(patterns, text)
bm_val = boyer_moore(patterns, text)

method_dict = {
    "RK": 1,
    "KMP": 2,
    "BM": 3
}

result = [
    (rk_val, 1),
    (kmp_val, 2),
    (bm_val, 3)
]

result.sort()

if result[0][0] != result[1][0]:
    print(result[0][1], end=" ")
else:
    print(0, end=" ")

if result[0][0] == result[1][0]:
    print(0, end=" ")

if result[0][0] != result[1][0] and result[1][0] != result[2][0]:
    print(result[1][1], end=" ")
    print(result[2][1])
elif result[1][0] != result[2][0]:
    print(result[2][1])
else:
    print(0, end=" ")

if result[1][0] == result[2][0]:
    print(0)

print()
