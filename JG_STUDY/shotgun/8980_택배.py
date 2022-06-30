import sys, heapq

input = sys.stdin.readline

n, c = map(int, input().split())
town = []


input_size = int(input())
for _ in range(input_size):
  a, b, d = map(int, input().split())
  heapq.heappush(town, [b - a, a, b, d])

def solution():  
  truck = []
  cur_c = 0
  answer = 0
  for idx in range(1, n + 1):
    while truck:
      pos, size = heapq.heappop(truck)
      if pos == idx:
        cur_c -= size
        answer += size
      else:
        heapq.heappush(truck, [pos, size])
        break
    
    temp = []
    while town and cur_c < c:
      pri, src, dst, size = heapq.heappop(town)
      if src != idx:
        temp.append([pri, src, dst, size])
        break
      if cur_c + size <= c:
        cur_c += size
        heapq.heappush(truck, [dst, size])
      elif cur_c < c and c <= cur_c + size:
        heapq.heappush(truck, [dst, c - cur_c])
        cur_c = c
        break
      
    while temp:
      heapq.heappush(town, temp.pop())
        
  print(answer)
  
solution()