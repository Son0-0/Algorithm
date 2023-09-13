#include <iostream>
#include <memory.h>
 
constexpr int MAX = 200001;
 
using namespace std;
 
int arr[MAX];
int dp[MAX];
 
int main(int argc, char** argv)
{
    int T;
    scanf("%d", &T);
 
    for (int test_case = 1; test_case <= T; ++test_case)
    {
        int N;
        scanf("%d", &N);
 
        memset(arr, 0, sizeof(arr));
        memset(dp, 0, sizeof(dp));
 
        for (int i = 0; i < N; i++) {
            scanf("%d", &arr[i]);
        }
 
        int answer = arr[0] > 0 ? arr[0] : 0;
        dp[0] = answer;
 
        for (int i = 1; i < N; i++) {
            if (0 < dp[i - 1] + arr[i])
                dp[i] = dp[i - 1] + arr[i];
 
            if (answer < dp[i])
                answer = dp[i];
        }
 
        printf("#%d %d\n", test_case, answer);
    }
    return 0;
}
