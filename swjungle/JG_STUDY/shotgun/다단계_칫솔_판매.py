enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]


def calculate_pay(p):
    if p < 10:
        return 0

    return int(p * 0.1)


def solution():

    conn = {}

    for idx, name in enumerate(referral):
        if enroll[idx] not in conn:
            conn[enroll[idx]] = name
        else:
            conn[enroll[idx]].append(name)

    result = {}

    for idx, p in enumerate(amount):
        target = seller[idx]
        pay = (p * 100)
        fee = calculate_pay(pay)

        while True:
            if pay == 0:
              break
            if target not in result:
                result[target] = pay - fee
            else:
                result[target] += pay - fee
            target = conn[target]
            pay = int(pay * 0.1)
            fee = calculate_pay(pay)

            if target == "-":
                if target not in result:
                    result[target] = pay
                else:
                    result[target] += pay
                break

    answer = []
    for ename in enroll:
        if ename in result:
            answer.append(result[ename])
        else:
            answer.append(0)

    return answer


print(solution())