#include <iostream>
#include <vector>
#include <algorithm>
#define INT_MAX 2147483647;

using namespace std;

vector<int> selectedIngredients;
vector<int> bestIngredients;
vector<vector<int>> ingredients;
vector<int> minRequirements;
int minCost = INT_MAX;
int maxNutrientSum = 0;


bool isValidSolution() {
    vector<int> sum(4, 0);
    for (int i = 0; i < selectedIngredients.size(); i++) {
        for (int j = 0; j < 4; j++) {
            sum[j] += ingredients[selectedIngredients[i]][j];
        }
    }
    for (int i = 0; i < 4; i++) {
        if (sum[i] < minRequirements[i]) {
            return false;
        }
    }
    return true;
}

bool canMeetRequirements(int index) {
    vector<int> remainingSum(4, 0);
	vector<int> selectedSum(4, 0);
    for (int i = index; i < ingredients.size(); i++) {
        for (int j = 0; j < 4; j++) {
            remainingSum[j] += ingredients[i][j];
        }
    }
	for (int i = 0; i < selectedIngredients.size(); i++) {
		for (int j = 0; j < 4; j++) {
			selectedSum[j] += ingredients[selectedIngredients[i]][j];
		}
	}

    for (int i = 0; i < 4; i++) {
        if (selectedSum[i] < minRequirements[i] && remainingSum[i] + selectedSum[i] < minRequirements[i]) {
            return false;
        }
    }
    return true;
}

void backtrack(int index, int totalCost) {
    if (index == ingredients.size()) {
        if (isValidSolution() && totalCost < minCost) {
            minCost = totalCost;
            bestIngredients = selectedIngredients;
            int nutrientSum = 0;
            for (int i = 0; i < selectedIngredients.size(); i++) {
                for (int j = 0; j < 4; j++) {
                    nutrientSum += ingredients[selectedIngredients[i]][j];
                }
            }
            maxNutrientSum = nutrientSum;
        } else if (isValidSolution() && totalCost == minCost) {
            int nutrientSum = 0;
            for (int i = 0; i < selectedIngredients.size(); i++) {
                for (int j = 0; j < 4; j++) {
                    nutrientSum += ingredients[selectedIngredients[i]][j];
                }
            }
            if (nutrientSum > maxNutrientSum) {
                bestIngredients = selectedIngredients;
                maxNutrientSum = nutrientSum;
            }
        }
        return;
	}

    if (index < ingredients.size()) {
		if (!canMeetRequirements(index)) return;
	}

    selectedIngredients.push_back(index);
    backtrack(index + 1, totalCost + ingredients[index][4]);
    selectedIngredients.pop_back();
    backtrack(index + 1, totalCost);
}

int main() {
    int numIngredients;
    cin >> numIngredients;

    minRequirements.resize(4);
    for (int i = 0; i < 4; i++) {
        cin >> minRequirements[i];
    }

    ingredients.resize(numIngredients);
    for (int i = 0; i < numIngredients; i++) {
        ingredients[i].resize(5);
        for (int j = 0; j < 5; j++) {
            cin >> ingredients[i][j];
        }
    }

    backtrack(0, 0);

    if (bestIngredients.empty()) {
        cout << "0" << endl;
    } else {
        sort(bestIngredients.begin(), bestIngredients.end());
        for (int i = 0; i < bestIngredients.size(); i++) {
            cout << bestIngredients[i] + 1 << " ";
        }
        cout << endl;
    }

    return 0;
}
