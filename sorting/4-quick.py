target = [3, 5, 1, 2, 7, 8, 4, 6, 9, 10]


def quick_sort(left, right):
    if right - left < 1:
        return

    pivot = target[left]

    lptr, rptr = left + 1, right

    while lptr <= rptr:
        if pivot < target[lptr] and target[rptr] < pivot:
            target[lptr], target[rptr] = target[rptr], target[lptr]
            lptr, rptr = left + 1, right

        if target[lptr] <= pivot:
            lptr += 1

        if pivot <= target[rptr]:
            rptr -= 1

    target[left], target[rptr] = target[rptr], target[left]

    quick_sort(left, rptr - 1)
    quick_sort(lptr, right)


print('before:\t', target)
quick_sort(0, len(target) - 1)
print('after:\t', target)
