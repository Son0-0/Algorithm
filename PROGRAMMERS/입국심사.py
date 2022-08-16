def solution(n, times):
  answer = 0
  times.sort()

  def calculate(mid):
    return mid
  
  def binary_search(left, right):
    if right < left:
      return
    
    mid = (left + right) // 2
    value = calculate(mid)
    
    if value:
      binary_search(left, mid - 1)
    else:
      binary_search(mid + 1, right)
    

  binary_search(times[0] * n, times[-1] * n) 
    
  return answer
  
print(solution(6, [7, 10]))