def solution(genres, plays):
    answer = []
    matching = dict(zip(plays,genres))
    # print(matching)
    plays.sort(reverse=True)
    # print(plays)
    for i in plays:
        pass
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))