import sys, math

n = int(input())
num_list = list(map(int, input().split()))

def init(tree, i, left, right):
  if left == right:
    tree[i] = num_list[left]
    return tree[i]
  
  mid = left + (right - left) // 2
  tree[i] = init(tree, i * 2, left, mid) + init(tree, i * 2 + 1, mid + 1, right)
  return tree[i]

def solution():
  
  tree = [0] * (2 ** math.ceil(math.log2(n) + 1))
  init(tree, 1, 0, n - 1)
  
  def query(left, right, index, ql, qr):
    if right < ql and qr < left:
      return 0
  
    if ql <= left and right <= qr:
      return tree[index]
    
    mid = (left + right) // 2
    return query(left, mid, index * 2, ql, qr) +query(mid + 1, right, index * 2 + 1, ql, qr)
  
  print(tree)
  
  print(query(0, n - 1, 1, 1, 2))
  
  return 0
  
solution()