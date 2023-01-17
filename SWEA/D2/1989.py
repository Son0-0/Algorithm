T = int(input())

def solution():
    for tc in range(1, T + 1):
        target = input().rstrip()
        result = 1
        
        for i in range(len(target) // 2):
            if target[i] != target[-i-1]:
                result = 0
                break
                
        print(f'#{tc} ', result)
        
solution()