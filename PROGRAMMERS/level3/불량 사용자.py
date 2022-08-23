def solution(user_id, banned_id):
    answer = set()
    size = len(banned_id)
    id_list = [set() for _ in range(size)]

    def calc(target, length):
        for index, id in enumerate(banned_id):
            if len(id) != length:
                continue
            flag = True
            for idx, c in enumerate(id):
                if c != '*' and c != target[idx]:
                    flag = False
                    break
            if flag:
                id_list[index].add(target)

    for id in user_id:
        calc(id, len(id))

    def dfs(cur, visited=[]):
        if cur == size:
            nonlocal answer
            answer.add(''.join(sorted(visited)))
            return

        for id in id_list[cur]:
            if id not in visited:
                dfs(cur + 1, visited + [id])

    dfs(0, [])
    return len(answer)


print(solution(["frodo", "fradi", "crodo",
      "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123",
      "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
      ["fr*d*", "*rodo", "******", "******"]))
