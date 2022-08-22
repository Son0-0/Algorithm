def solution(genres, plays):

    answer = {}
    for idx in range(len(genres)):
        if genres[idx] not in answer:
            answer[genres[idx]] = {'total': plays[idx],
                                   'songs': [[idx, plays[idx]]]}
        else:
            answer[genres[idx]]['total'] += plays[idx]
            answer[genres[idx]]['songs'].append([idx, plays[idx]])

    value = []
    
    for result in sorted(answer, key=lambda x: answer.get(x)['total'], reverse=True):
        for idx, song in enumerate(sorted(answer[result]['songs'], key=lambda x: (x[1], -x[0]), reverse=True)):
            if idx == 2:
                break
            value.append(song[0])

    return value


print(solution(["classic", "pop", "classic",
      "classic", "pop", "cpa"], [500, 600, 150, 800, 2500, 3200]))
