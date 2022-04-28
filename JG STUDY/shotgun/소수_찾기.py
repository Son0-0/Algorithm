visited = []
result = []
numlist = []


def isPrime(num):
    if num < 2:
        return False

    if num == 2:
        return True
      
    for idx in range(2, num):
        if (num % idx) == 0:
            return False

    return True


def dfs(cur, odr_list, size):
    pnum = int(''.join(odr_list))

    if isPrime(pnum) == True:
        if not pnum in result:
            result.append(pnum)

    for i in range(size):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, odr_list + [numlist[i]], size)
            visited[i] = 0


def solution(numbers):
    global numlist
    numlist = list(map(str, numbers))

    size = len(numlist)

    for _ in range(size):
        visited.append(0)

    for idx in range(size):
        visited[idx] = 1
        dfs(idx, [numbers[idx]], size)
        visited[idx] = 0

    print(len(result), result)
    return len(result)
  
# # solution("17")
# # solution("011")
# solution("3")

# from itertools import permutations

# def isPrime(num):
#     if num < 2:
#         return False
    
#     if num == 2:
#         return True
    
#     for target in range(2, num):
#         if (num % target) == 0:
#             return False
        
#     return True

# def solution(numbers):
#     llist = []
#     for i in range(1, len(numbers) + 1):
#         llist += list(permutations(numbers, i))
#     llist = list(set(llist))

#     answer = []
#     for num in llist:
#         pnum = int(''.join(num))
#         if isPrime(pnum) == True:
#             answer.append(pnum)
            
#     answer = list(set(answer))
    
#     return len(answer)