def solution(answers):
    answer = []
    student_1 = [1, 2, 3, 4, 5]*len(answers)
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]*len(answers)
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*len(answers)
    my = []
    correct_1 = 0
    correct_2 = 0
    correct_3 = 0
    for i in range(len(answers)):
        if student_1[i] == answers[i]:
            correct_1 += 1
        else:
            continue
    my.append(correct_1)
    for i in range(len(answers)):
        if student_2[i] == answers[i]:
            correct_2 += 1
        else:
            continue
    my.append(correct_2)
    for i in range(len(answers)):
        if student_3[i] == answers[i]:
            correct_3 += 1
        else:
            continue
    my.append(correct_3)
    
    for j in range(len(my)):
        if my[j] >= max(my):
            answer.append(j+1)

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))