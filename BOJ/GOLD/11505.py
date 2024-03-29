import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

nums = [int(input()) for _ in range(N)]
n = len(nums)
tree = [0 for _ in range(2*n+1)]


def buildTree():
    global tree
    
    # leaf node
    for i in range(n):
        tree[i+n] = nums[i]
        
    # p = lc + rc
    for i in range(n-1, 0, -1):
        tree[i] = (tree[2*i] * tree[2*i+1]) % 1000000007
    
    
def updateTree(index, newValue):
    tree[index+n] = newValue
    index += n
    
    i = index
    
    while i > 1:
        tree[i>>1] = tree[i] * tree[i^1]
        i >>= 1
    

def calculate(l, r):
    sum = 1
    
    l += n
    r += n
    
    while l < r:
        if sum == 0:
            return sum
        if ((l&1) > 0):
            sum *= tree[l] % 1000000007
            l += 1
        
        if ((r&1) > 0):
            r -= 1
            sum *= tree[r] % 1000000007
            
        l >>= 1
        r >>= 1
        
    return sum % 1000000007


def solution():
    
    buildTree()
    
    for _ in range(M+K):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            updateTree(cmd[1]-1, cmd[2])
        else:
            print(calculate(cmd[1]-1, cmd[2]))
            
solution()