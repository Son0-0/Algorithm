def solution(record):
    answer = []

    uname = {}

    for rec in record:
        command = rec.split()
        if command[0] == 'Enter':
            uname[command[1]] = command[2]
        elif command[0] == 'Change':
            uname[command[1]] = command[2]

    for rec in record:
        command = rec.split()
        if command[0] == 'Enter':
            answer.append(f'{uname[command[1]]}님이 들어왔습니다.')
        elif command[0] == 'Leave':
            answer.append(f'{uname[command[1]]}님이 나갔습니다.')

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
      "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
