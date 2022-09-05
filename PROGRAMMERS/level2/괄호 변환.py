def divide(p):
    l, r = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            l += 1
        else:
            r += 1

        if l == r:
            return p[:i + 1], p[i + 1:]


def is_valid(p):
    stack = []
    for c in p:
        if c == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            stack.pop()
    return True


def solution(p):
    answer = ''

    if not p:
        return ''

    u, v = divide(p)

    if is_valid(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'

        for c in u[1:-1]:
            if c == '(':
                answer += ')'
            else:
                answer += '('

        return answer


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
