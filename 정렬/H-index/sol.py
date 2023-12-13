# 위키피디아 설명
# h-index를 구하기 위해서는 배열을 내림차순으로 바꿔야합니다.
# 그리고 각각의 인덱스와 인덱스에 해당하는 값을 비교해 인덱스가 인덱스에 해당하는 값보다 크거나 같으면 그 값이 h-index입니다.
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i,v in enumerate(citations):
        if i >= v:
            answer = i
            break # break를 하는 이유: 최댓값을 찾아야하기때문에
        else:
            answer = len(citations)  # print(solution([4, 4, 4]))의 경우 대비
            
    return answer

print(solution([6, 5, 5, 5, 3, 2, 1, 0]))
print(solution([3, 0, 6, 1, 5]))
print(solution([4, 4, 4]))

# 다른 사람 풀이: 이게 뭐지?
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
