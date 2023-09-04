#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

unordered_map<string, int> um = {{"0001101", 0}, {"0011001", 1}, {"0010011", 2},
                                 {"0111101", 3}, {"0100011", 4}, {"0110001", 5},
                                 {"0101111", 6}, {"0111011", 7}, {"0110111", 8},
                                 {"0001011", 9}};

int isValid(vector<int>& nums) {
    int sum = (nums[0] + nums[2] + nums[4] + nums[6]) * 3 + nums[1] + nums[3] +
              nums[5] + nums[7];

    if (sum % 10 == 0) {
        int ret = 0;
        for (int i = 0; i < 8; i++) {
            cout << nums[i] << endl;
            ret += nums[i];
        }
        return ret;
    }

    return 0;
}

int main(int argc, char** argv) {
    int test_case;
    int T;

    cin >> T;

    for (test_case = 1; test_case <= T; ++test_case) {
        int n, m;
        scanf("%d %d\n", &n, &m);

        int ans = 0;

        for (int i = 0; i < n; i++) {
            string str;
            getline(cin, str);

            int size = (m / 7) - 8 + 1;
            bool flag = true;

            for (int j = m; j >= 0; j--) {
                vector<int> nums;

                if (str[j] == '1') {
                    if (j - 56 + 1 < 0) {
                        continue;
                    }

                    string temp = "";
                    int cnt = 0;
                    for (int p = j - 56 + 1; p <= j; p++) {
                        if (cnt == 7) {
                            cnt = 0;

                            if (um.find(temp) != um.end()) {
                                nums.push_back(um[temp]);
                            } else {
                                break;
                            }

                            temp = str[p];
                        } else {
                            temp += str[p];
                            cnt++;
                        }
                    }

                    if (nums.size() == 8) {
                        int answer = isValid(nums);
                        if (answer) {
                            ans = answer;
                            break;
                        }
                    }
                }
            }

            if (!ans) {
                break;
            }
        }

        cout << "#" << test_case << " " << ans << endl;
    }

    return 0;
}