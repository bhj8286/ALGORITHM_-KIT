def solution(sizes):
    answer = 0
    re_sizes = []
    garo = []
    sero = []
    for i in sizes:
        re_sizes.append(sorted(i))
    for j in range(len(re_sizes)):
        garo.append(re_sizes[j][0])
    for j in range(len(re_sizes)):
        sero.append(re_sizes[j][1])
    answer = max(garo)*max(sero)
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))

# 다른 사람 풀이: 오...
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
