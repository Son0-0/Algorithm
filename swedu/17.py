def isPossible(target):
    global N, K
    global nums
 
    temp = nums[:]
    cnt = 0
 
    for i in range(1, N):
        diff = abs(temp[i] - temp[i-1])
 
        if target < diff:
            cnt += (diff - target)
 
            if temp[i] > temp[i-1]:
                temp[i] -= (diff - target)
            else:
                temp[i-1] -= (diff - target)
 
        if K < cnt:
            return False
 
    for i in range(N-1, 0, -1):
        diff = abs(temp[i] - temp[i-1])
 
        if target < diff:
            cnt += (diff - target)
 
            if temp[i] > temp[i-1]:
                temp[i] -= (diff - target)
            else:
                temp[i-1] -= (diff - target)
 
        if K < cnt:
            return False
 
    return True
 
 
def solve():
    global N, K
    global nums
 
    T = int(input())
 
    for test_case in range(1, T + 1):
        N, K = map(int, input().split())
        answer = 0
 
        nums = list(map(int, input().split()))
 
        left, right = 0, max(nums) - min(nums)
 
        answer = 0
        while left <= right:
            mid = (left + right) // 2
 
            if(isPossible(mid)):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
 
        print(f'#{test_case} {answer}')
 
solve()