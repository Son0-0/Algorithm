import sys

input = sys.stdin.readline


def postorder(preorder, inorder):
    if len(preorder) == 0:
        return
    if len(inorder) == 0:
        return
      
    idx = inorder.index(preorder[0])
    postorder(preorder[1:idx + 1], inorder[0:idx])
    postorder(preorder[idx + 1:], inorder[idx + 1:])
    print(preorder[0], end=' ')


def solution():
    for _ in range(int(input())):
        nsize = int(input())
        prlist = list(map(int, input().split()))
        inlist = list(map(int, input().split()))
        postorder(prlist, inlist)
        print()


solution()