import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

N, E = map(int, input().split())
graph = [[] for _ in range(N)]
cost = [INF for _ in range(N)]

for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a-1].append((b-1, c))
  graph[b-1].append((a-1, c))
  
strt, des = map(int, input().split())

# 1 - 2 - 3 - 4
# 1 - 3 - 2 - 4 

def daijkstra():
  queue = []
  cost[strt - 1] = 0
  heapq.heappush(queue, (0, 0))
  
  while queue:
    c, vtx = heapq.heappop(queue)
    
    if cost[vtx] < c:
      continue
    
    for i in graph[vtx]:
      cur_cost = c + i[1]
      
      if cur_cost < cost[i[0]]:
        cost[i[0]] = cur_cost
        heapq.heappush(queue, (cur_cost, i[0]))
      
def solution():
  daijkstra()
  print(cost)
  
solution()