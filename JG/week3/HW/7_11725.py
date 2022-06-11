import sys

input = sys.stdin.readline

size = int(input())

tree = [[] for _ in range(size)]
for _ in range(size - 1):
    idx, target = map(int, input().split())
    tree[idx - 1].append(target - 1)
    tree[target - 1].append(idx - 1)

result = [0 for _ in range(size)]


def dfs(root):
    for node in tree[root]:
        if result[node] == 0:
            result[node] = root + 1
            dfs(node)


dfs(0)

for idx in range(1, size):
    print(result[idx])
