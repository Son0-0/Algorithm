def solution(lines):

    tlist = []
    for line in lines:
        _, target, due = line.split()
        target = target.split(':')
        time = (int(target[0]) * 3600 + int(target[1])
                * 60 + float(target[2])) * 1000
        tlist.append([time - float(due[:-1])*1000 + 1, time])

    max_value = 0
    for i in range(len(lines)):
        cnt = 0
        for j in range(i, len(lines)):
            if tlist[j][0] - 1000 < tlist[i][1]:
                cnt += 1
        max_value = max(max_value, cnt)

    return max_value


print(solution(["2016-09-15 00:00:00.000 3s"]))
print(solution(["2016-09-15 23:59:59.999 0.001s"]))
print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s",
                "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))
print(solution(["2016-09-15 00:00:00.000 2.3s",
                "2016-09-15 23:59:59.999 0.1s"]))
