def solution(n, build_frame):
    answer = []
    
    _map = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    cx, cy = 0, 0
    for b in build_frame:
        cx, cy = b[0], b[1]
        if b[3] == 1:
            if b[2] == 0:
                if (cy == 0) or (_map[cx][cy - 1] == '-') or (_map[cx -1][cy] == '|') or (_map[cx + 1][cy] == '|'):
                    _map[cx][cy] = '-'
                    answer.append([cx, cy, 0])
            else:
                if (_map[cx + 1][cy - 1] == '-') or (_map[cx][cy - 1] == '-'):
                    _map[cx][cy] = '|'
                    answer.append([cx, cy, 1])
                    continue
                if (_map[cx -1][cy] == '|') and (_map[cx + 1][cy] == '|'):
                    _map[cx][cy] = '|'
                    answer.append([cx, cy, 1])
        elif b[3] == 0:
            if b[2] == 0:
                _map[cx][cy] = 0
                answer.remove([cx, cy, 0])
            else:
                if (_map[cx][cy - 1] == '|') or (_map[cx][cy + 1] == '|'):
                    _map[cx][cy] = 0
                    answer.remove([cx, cy, 1])
                
        print("=================")
        print(cx, cy, b[2], b[3])
        for m in _map:
            print(*m)
        print("=================")
    
                
    answer.sort(key = lambda x:(x[0], x[1], x[2]))   
    print(answer)
    
    return answer
  
solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])