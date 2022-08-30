import sys

input = sys.stdin.readline

n = int(input())
plist = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for idx in range(1, n + 1):
  graph[idx] = list(map(int, input().split()))[1:]

def solution():
  
  return 0

solution()