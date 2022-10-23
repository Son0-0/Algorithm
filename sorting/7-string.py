target = 'abab'
text = 'abababab'


def brute_force():

    answer = []

    for i in range(len(text) - len(target) + 1):
        flag = 1
        for j in range(len(target)):
            if target[j] != text[i + j]:
                flag = 0
                break

        if flag == 1:
            answer.append(i)

    return answer


def compute_lps():
    lps = [0 for _ in range(len(target))]

    length = 0
    for i in range(1, len(target)):
        if target[length] == target[i]:
            length += 1
            lps[i] = length

        else:
            if length != 0:
                length = lps[length - 1]

            else:
                lps[i] = 0

    return lps


def kmp():
    answer = []

    lps = compute_lps()

    i, j = 0, 0
    while i < len(text):
        if target[j] == text[i]:
            i += 1
            j += 1
            if j == len(target):
                answer.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return answer


print(brute_force())
print(kmp())
