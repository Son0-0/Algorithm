import sys

input = sys.stdin.readline

class Node:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right

size = int(input())
tree = {}

for idx in range(size):
  data, lt, rt = map(str, input().split())
  tree[data] = Node(data, lt, rt)
  
def preorder(node): # N - L - R
  print(node.data, end='')
  
  if node.left != '.':
    preorder(tree[node.left])
    
  if node.right != '.':
    preorder(tree[node.right])
  
def inorder(node): # L - N - R
  if node.left != '.':
    inorder(tree[node.left])
    
  print(node.data, end='')
  
  if node.right != '.':
    inorder(tree[node.right])
  
def postorder(node): # L - R - N
  if node.left != '.':
    postorder(tree[node.left])
  
  if node.right != '.':
    postorder(tree[node.right])
  
  print(node.data, end='')
  
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
print()