import sys

input = sys.stdin.readline
pwlen, wlen = map(int, input().split())
pwlist = [c for c in list(map(str, input().split()))]
ae = ['a', 'e', 'i', 'o', 'u']
pwlist.sort()

result = []
def recur(cur, visited, cnt, rs, aeiou):
  if cnt == 0:
    global result
    if 0 < aeiou and 2 <= (len(rs) - aeiou):
      result.append(rs)
    return
  
  for i in range(cur+1, wlen):
    if visited[i] == 0:
      visited[i] = 1
      if pwlist[i] in ae:
        recur(i, visited, cnt - 1, rs + pwlist[i], aeiou + 1)
      else:
        recur(i, visited, cnt - 1, rs + pwlist[i], aeiou)
      visited[i] = 0
  
def solution():
  visited = [0] * wlen
  recur(-1, visited, pwlen, "", 0)
  print(*result, sep="\n")

solution()