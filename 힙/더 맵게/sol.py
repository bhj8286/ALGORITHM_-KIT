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

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K: ## scoville을 heapq리스트이므로 while min(scoville) < K:으로 시간낭비를 할 필요가 없다. 힙큐는 정렬이 되어 나오기 때문에
        if len(scoville) == 1: ## 모든 음식을 섞어서 스코빌 지수 k이상으로 만들지 못한 경우는 if문에 걸린다.
            return -1
        mix_scovile = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        answer += 1
        heapq.heappush(scoville,mix_scovile)
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))



