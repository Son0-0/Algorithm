import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

v_size, e_size = map(int, input().split()) # 정점의 개수 / 간선의 개수
k = int(input()) # start number

graph = [[] for _ in range(v_size + 1)]
visited = [False for _ in range(v_size + 1)]
distance = [INF for _ in range(v_size + 1)]

for _ in range(e_size):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))

def daijkstra(v):
  distance[v] = 0
  cost = []
  heapq.heappush(cost, (0, v))
  
  while cost:
    cur_cost, vtx = heapq.heappop(cost)
    
    if distance[vtx] < cur_cost:
      continue
    
    for i in graph[vtx]:
      ccost = cur_cost + i[1]
      
      if ccost < distance[i[0]]:
        distance[i[0]] = ccost
        heapq.heappush(cost, (ccost, i[0]))
  
def solution():
  daijkstra(k)
  
  for num in distance[1:]:
    if num == INF:
      print("INF")
    else:
      print(num)

solution()