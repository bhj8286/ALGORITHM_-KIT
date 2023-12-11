def solution(array, commands):
    answer = []
    for w in commands:
        i, j, k = w
        new = array[i-1:j]
        new.sort()
        answer.append(new[k-1])
    
        
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))