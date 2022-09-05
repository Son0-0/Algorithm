from cmath import phase


accept = 'a'


def solution(new_id):
    answer = ''

    # 1 phase
    new_id = new_id.lower()

    # 2 phase
    new_id = ''.join([c for c in new_id if c.isdigit()
                     or c.isalpha() or c in '-_.'])
    # 3 phase
    for _ in range(len(new_id)):
        new_id = new_id.replace('..', '.')

    # 4 phase
    new_id = phase4(new_id)

    # 5 phase
    if not new_id:
        new_id = 'a'

    # 6 phase
    if 16 <= len(new_id):
        new_id = new_id[:15]
        new_id = phase4(new_id)

    # 7 phase
    length = len(new_id)
    if length <= 2:
        new_id += new_id[-1] * (3 - length)

    return new_id


def phase4(new_id):
    # 4 phase
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]

    return new_id


# print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("................b"))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))
