#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> flip(const vector<int>& arr, int i, int j) {
    vector<int> tmp = arr;
    reverse(tmp.begin() + i, tmp.begin() + j + 1);
    for (int k = i; k <= j; ++k) {
        tmp[k] = -tmp[k];
    }
    return tmp;
}

bool check_one(const vector<int>& arr) {
    vector<int> target(arr.size());
    for (int i = 0; i < arr.size(); ++i) {
        target[i] = i + 1;
    }
    int start = min_element(arr.begin(), arr.end()) - arr.begin();
    int end = 0;
    for (int i = 1; i <= arr.size(); ++i) {
        auto it = find(arr.begin(), arr.end(), -i);
        if (it != arr.end()) {
            end = it - arr.begin();
            break;
        }
    }
    vector<int> res = flip(arr, start, end);
    return res == target;
}

bool check_continuous_subarrays(const vector<int>& arr) {
    int n = arr.size();
    int i = 0;
    vector<pair<int, int>> sub_arrays;
    while (i < n) {
        int j = i + 1;
        while (j < n && arr[j] == arr[j - 1] + 1) {
            ++j;
        }
        if (j > i) {
            sub_arrays.emplace_back(i, j);
            if (check_one(flip(arr, i, j - 1))) {
                return true;
            }
        }
        i = j;
    }
    if (check_one(flip(arr, sub_arrays[0].first, sub_arrays[1].second - 1))) {
        return true;
    }
    if (check_one(flip(arr, sub_arrays[0].first, sub_arrays[2].second - 1))) {
        return true;
    }
    if (check_one(flip(arr, sub_arrays[1].first, sub_arrays[2].second - 1))) {
        return true;
    }
    if (check_one(flip(arr, sub_arrays[1].first, sub_arrays[3].second - 1))) {
        return true;
    }
    if (check_one(flip(arr, sub_arrays[2].first, sub_arrays[3].second - 1))) {
        return true;
    }
    return false;
}

bool check_two(const vector<int>& arr) {
    return check_continuous_subarrays(arr);
}

void check(const vector<int>& arr) {
    if (check_one(arr)) {
        cout << "one\n";
    } else if (check_two(arr)) {
        cout << "two\n";
    } else {
        cout << "over\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    vector<vector<int>> bread_tray(5, vector<int>(n));
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> bread_tray[i][j];
        }
    }
    for (const auto& arr : bread_tray) {
        check(arr);
    }
    return 0;
}
