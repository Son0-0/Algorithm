#include <memory.h>

char* target;
int s1[26], s2[26];

bool check() {
    for (int i = 0; i < 26; i++) {
        if (s1[i] != s2[i]) return false;
    }
    return true;
}

int FindAnagram(int Len1, char* S1, int Len2, char* S2) {
    if (Len1 > Len2) return 0;

    memset(s1, 0, 26 * sizeof(int));
    memset(s2, 0, 26 * sizeof(int));

    for (int i = 0; i < Len1; i++) {
        s1[S1[i] - 'a']++;
        s2[S2[i] - 'a']++;
    }

    int answer = check() ? 1 : 0;
    for (int i = Len1; i < Len2; i++) {
        s2[S2[i - Len1] - 'a']--;
        s2[S2[i] - 'a']++;
        if (check()) {
            answer++;
        }
    }

    return answer;
}