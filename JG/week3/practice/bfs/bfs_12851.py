import sys
from collections import deque

input = sys.stdin.readline
END = 100001
move = [1, -1]
road = [-1 for _ in range(END)]
N, K = map(int, input().split())
cnt = 0

def bfs(n):
  global cnt
  road[n] = 0
  queue = deque()
  queue.append(n)
  
  while queue:
    cur = queue.popleft()
    if cur == K:
      cnt += 1
    for i in range(3):
      if i == 2:
        pos = cur * 2
      else:
        pos = cur + move[i]
      if 0 <= pos < END:
        if road[pos] == -1 or road[cur] + 1 == road[pos]:
          road[pos] = road[cur] + 1
          queue.append(pos)
  
def solution():
  bfs(N)
  print(road[K])
  print(cnt)
  
solution()