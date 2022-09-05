from itertools import combinations


def solution(orders, course):
    answer = []

    d = dict()
    for order in orders:
        for length in course:
            for comb in combinations(order, length):
                c = (''.join(sorted(comb)))
                d[c] = d.get(c, 0) + 1

    a = dict()
    for m, cnt in sorted(d.items()):
        l = len(m)
        if 1 < cnt:
            if l in course and l in a:
                target = a[l][0][1]
                if target == cnt:
                    a[l].append([m, cnt])
                elif target < cnt:
                    a[l] = [[m, cnt]]
            elif l not in a:
                a[l] = [[m, cnt]]

    answer = []
    for num in course:
        if num in a:
            for menu in a[num]:
                answer.append(menu[0])
    return sorted(answer)


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
