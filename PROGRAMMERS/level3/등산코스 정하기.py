from collections import defaultdict, deque


def solution(n, paths, gates, summits):
    # draw graph
    graph = defaultdict(list)
    for src, dest, cost in paths:
        graph[src].append([dest, cost])
        graph[dest].append([src, cost])

    # insert gates to queue
    costs = [10000001 for _ in range(n + 1)]
    q = deque()
    for gate in gates:
        q.append([0, gate])
        costs[gate] = 0

    summits = set(sorted(summits))

    while q:
        cost, cur = q.popleft()

        if cur in summits or costs[cur] < cost:
            continue

        for node, dis in graph[cur]:
            ncost = max(cost, dis)
            if ncost < costs[node]:
                costs[node] = ncost
                q.append([ncost, node])

    answer = [0, 10000001]
    for summit in sorted(summits):
        if costs[summit] < answer[1]:
            answer[0] = summit
            answer[1] = costs[summit]

    return answer


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [
      3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [
      2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [
      4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4],
      [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))
