import sys

input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a, b = find_parent(parent, a), find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

def solution():
  v, e = map(int, input().split())
  parent = [num for num in range(0, v + 1)]

  edges = []
  for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))
  edges.sort(key = lambda x:x[2])
  
  result = 0
  for edge in edges:
    a, b, cost = edge
    if find_parent(parent, a) != find_parent(parent, b):
      union_parent(parent, a, b) 
      result += cost
    
  print(result)

solution()