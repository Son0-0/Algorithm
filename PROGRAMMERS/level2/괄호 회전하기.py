from collections import deque

def solution(s):
    answer = 0
    q = deque(s)
    
    def check_valid(target):
        stack = []
        
        for op in target:
            if op in ['(', '[', '{']:
                stack.append(op)
            else:
                if not stack:
                    return False
                temp = abs(ord(op) - ord(stack.pop()))
                if temp == 0 or 2 < temp:
                    return False

        if not stack:
            return True
    
    for _ in range(len(q)):
        q.append(q.popleft())
        if check_valid(q):
            answer += 1
        
    return answer