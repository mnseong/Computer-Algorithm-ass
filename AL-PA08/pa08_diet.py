def branch_and_bound(n, target, ingredients):
    def calculate_nutrients(selection):
        nutrients = [0, 0, 0, 0]
        for idx in selection:
            ingredient = ingredients[idx - 1]
            nutrients = [a + b for a, b in zip(nutrients, ingredient[:4])]
        return nutrients

    def backtrack(curr_selection, curr_cost, curr_nutrients):
        min_cost=0
        result=0

        if curr_nutrients >= target and curr_cost < min_cost:
            min_cost = curr_cost
            result = curr_selection.copy()

        if curr_selection and curr_cost >= min_cost:
            return

        for i in range(curr_selection[-1] + 1, n + 1):
            selection = curr_selection + [i]
            nutrients = calculate_nutrients(selection)
            cost = curr_cost + ingredients[i - 1][4]

            if nutrients >= target and cost < min_cost:
                backtrack(selection, cost, nutrients)

    min_cost = float('inf')
    result = []
    for i in range(1, n + 1):
        backtrack([i], ingredients[i - 1][4], ingredients[i - 1][:4])

    return result

# 입력 받기
n = int(input())
target = list(map(int, input().split()))
ingredients = []
for _ in range(n):
    ingredients.append(list(map(int, input().split())))

print(target)
print(ingredients)

# # 결과 계산
# result = branch_and_bound(n, target, ingredients)
#
# # 결과 출력
# if result:
#     print(' '.join(map(str, result)))
# else:
#     print(0)
