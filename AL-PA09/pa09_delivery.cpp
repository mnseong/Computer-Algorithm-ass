#include <iostream>
#include <vector>
#include <cmath>
#include <climits>

using namespace std;

struct Point {
    int x;
    int y;
};

int n;
vector<int> deliveryOrder;
vector<int> carried;
vector<Point> restaurants;
vector<Point> homes;
vector<bool> visited;
int minDistance = INT_MAX;
vector<int> currOrder;
int currDistance = 0;

int calculateDistance(const Point& p1, const Point& p2) {
    return abs(p1.x - p2.x) + abs(p1.y - p2.y);
}

vector<int> getLexicographicallySmaller(const vector<int>& vec1, const vector<int>& vec2) {
    size_t minLength = min(vec1.size(), vec2.size());

    for (size_t i = 0; i < minLength; ++i) {
        if (vec1[i] < vec2[i]) {
            return vec1;
        } else if (vec1[i] > vec2[i]) {
            return vec2;
        }
    }
    return vec1.size() < vec2.size() ? vec1 : vec2;
}

void backtrack(int count, vector<int>& currOrder, int currDistance, int curX, int curY) {
    if (count == n) {
        if (currDistance < minDistance) {
            deliveryOrder = currOrder;
            minDistance = currDistance;
        }
		else if (currDistance == minDistance) {
			if (getLexicographicallySmaller(deliveryOrder, currOrder) == currOrder) {
				deliveryOrder = currOrder;
			}
        }
        return;
    }

    if (carried.size() < 2) {
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;

                int distanceToRestaurant = calculateDistance({curX, curY}, restaurants[i]);

                currDistance += distanceToRestaurant;
                currOrder.push_back(i + 1);
                carried.push_back(i + 1);

                backtrack(count, currOrder, currDistance, restaurants[i].x, restaurants[i].y);

                currDistance -= distanceToRestaurant;
                currOrder.pop_back();
                carried.pop_back();
                visited[i] = false;
            }
        }
    }

	for (int i = 0; i < carried.size(); i++) {
		int tmp = carried[i];
		int distanceToHome = calculateDistance({curX, curY}, homes[tmp - 1]);
		currDistance += distanceToHome;
		currOrder.push_back(-tmp);
		carried.erase(carried.begin() + i);
		backtrack(count + 1, currOrder, currDistance, homes[tmp - 1].x, homes[tmp - 1].y);
		currDistance -= distanceToHome;
		currOrder.pop_back();
		carried.insert(carried.begin() + i, tmp);
	}
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    restaurants.resize(n);
    homes.resize(n);
    visited.resize(n, false);

    for (int i = 0; i < n; i++) {
        cin >> restaurants[i].x >> restaurants[i].y >> homes[i].x >> homes[i].y;
    }

    backtrack(0, currOrder, currDistance, 500, 500);

    for (int i = 0; i < deliveryOrder.size(); i++) {
        cout << deliveryOrder[i] << " ";
    }

    cout << endl << minDistance << endl;

    return 0;
}
