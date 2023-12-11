def solution(citations):
    answer = 0
    max_count = 0
    my_citations = list(set(sorted(citations)))
    for i in my_citations:
        count = 0
        for j in citations:
            if i <= j:
                count += 1
        if count >= i:
            max_count = i
    return answer
print(solution([0,0,0,0,2]))
print(solution([3, 0, 6, 1, 5]))