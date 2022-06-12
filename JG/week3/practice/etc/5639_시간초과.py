import sys

input = sys.stdin.readline


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def preorder(node):  # N - L - R
    print(node.data, end='')

    if node.left != None:
        preorder(node.left)

    if node.right != None:
        preorder(node.right)


def postorder(node):  # L - R - N
    if node.left:
        postorder(node.left)

    if node.right:
        postorder(node.right)

    print(node.data)


def solution():
    tree = {}
    num = []
    while True:
        try:
            num.append(int(input()))
        except:
            break

    size = len(num)
    min_num = min(num)

    stack = []
    # init tree and stack before tracking binary tree
    for idx in range(size):
        tree[num[idx]] = Node(num[idx], None, None)
        while stack:
            cur_tree = tree[stack[-1]]
            # if cur_tree < num[idx] then pop and update tree
            if cur_tree.data < num[idx]:
                stack.pop()
                while stack and tree[stack[-1]].data < num[idx]:
                    cur_tree = tree[stack.pop()]
            if cur_tree.data == min_num:
                stack.pop()
                continue
            if not cur_tree.left and num[idx] < cur_tree.data:
                cur_tree.left = tree[num[idx]]
                break
            elif not cur_tree.right and cur_tree.data < num[idx]:
                cur_tree.right = tree[num[idx]]
                break
            elif not cur_tree.left and not cur_tree.right:
              stack.pop()
        stack.append(num[idx])

    postorder(tree[num[0]])


solution()