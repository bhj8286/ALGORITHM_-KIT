# 정확도:71,     * 시간 초과로 오답 뜸
def solution(scoville, K):
    answer = 0
    while min(scoville) < K:
        scoville.sort()
        i = scoville.pop(0)
        j = scoville.pop(0)
        mix_scovile = i + (j*2)
        answer += 1
        scoville.append(mix_scovile)
        
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))