def solution(begin, target, words):
    answer = 51

    def calc(cur, word):
        cnt = 0
        for idx, c in enumerate(cur):
            if c != word[idx]:
                cnt += 1
                if 1 < cnt:
                    return False

        return True

    def dfs(cur, visited=[]):
        if cur == target:
            nonlocal answer
            answer = min(answer, len(visited))

        for word in words:
            if word not in visited and calc(cur, word) == True:
                dfs(word, visited + [word])

        return 0

    dfs(begin, [])

    if answer == 51:
        return 0
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
