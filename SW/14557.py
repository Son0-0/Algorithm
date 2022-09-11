T = int(input())

dx = [-1, 1]

for test_case in range(1, T + 1):
    q = []

    cards = list(map(int, input()))
    length = len(cards)

    while 1 in cards:
        for idx, card in enumerate(cards):
            if card == 1:
                cards[idx] = -1
                for i in range(2):
                    nx = idx + dx[i]
                    if 0 <= nx < length:
                        if cards[nx] == 1:
                            cards[nx] = 0
                        elif cards[nx] == 0:
                            cards[nx] = 1

    if sum(cards) == -length:
        print(f'#{test_case} yes')
    else:
        print(f'#{test_case} no')
