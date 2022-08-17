# https://stackoverflow.com/questions/9490058/why-does-substring-slicing-with-index-out-of-range-work
# if you write s[999:9999],
# python is returning s[len(s):len(s)] since len(s) < 999 and your step is positive (1 -- the default).

def solution(s):

    size = len(s)
    answer = size

    for length in range(1, size // 2 + 1):
        new = ''
        same_size = 1
        prev = s[0:length]
        for i in range(1, size // length + 2):
            temp = s[length * i:length * (i + 1)]

            if prev == temp:
                same_size += 1
            else:
                if 1 < same_size:
                    new += str(same_size)
                new += prev
                prev = temp
                same_size = 1

        answer = min(answer, len(new))

    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
