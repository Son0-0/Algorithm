import sys

x, y = map(int, sys.stdin.readline().split())

size = int(input())

ax = [x]
ay = [y]

max_value_x = -sys.maxsize - 1
max_value_y = -sys.maxsize - 1

for i in range(0, size):
  xy, l = map(int, sys.stdin.readline().split())
  if xy == 1:
    ax.append(l)
  else:
    ay.append(l)
    
ax.sort(reverse=True)
ay.sort(reverse=True)

if len(ax) > 1:
  for i in range(0, len(ax) - 1):
    max_value_x = max(max_value_x, (ax[i] - ax[i+1]))
  max_value_x = max(max_value_x, ax[len(ax) - 1])
else:
  max_value_x = x

if len(ay) > 1:
  ay_temp = []
  for i in range(0, len(ay) - 1):
    max_value_y = max(max_value_y, (ay[i] - ay[i+1]))
  max_value_y = max(max_value_y, ay[len(ay) - 1])
else:
  max_value_y = y
  
print(max_value_x * max_value_y)