def solution(progresses, speeds):
    answer = []
    janup = list(map(lambda x:100-x, progresses))
    # print(janup)
    ws = [x / y for x, y in zip(janup, speeds)]
    work_speed = []
    # 밑의 for문을 돌리는 이유: ([90, 90], [10, 9]) 이 경우는 [1, 1]이 출력, ([5, 5, 5],[21, 25, 20])는 [3]dl 출력되어야하는데 23번째에서
    # 일괄적으로 round나 int를 쓰면 오류가 생긴다 그래서 ws에서 정수로 딱 떨어지는 값이면 그대로 값을 넣고 소수점이 있다면 한번의 작업이 더 필요하므로 +1을 해주었다.
    for i in ws:
        if int(i) == i:
            work_speed.append(i)
        else:
            i = int(i)+1
            work_speed.append(i)    

    while len(work_speed) != 0:
        # 큰 값부터 다시 반복
        current_index = 0 # 어차피 앞에 있던 작업했던 것들은 25번째 줄 코드에서 잘라내기때문에 첫번째부터 시작
        current_value = work_speed[current_index]
        
        # 카운트 및 삭제
        count = 1
        while current_index + count < len(work_speed) and work_speed[current_index + count] <= current_value:
            count += 1
        del work_speed[current_index:current_index + count]
        answer.append(count)
        
    return answer

print(solution( [90, 90], [10, 9]))
print(solution([5, 5, 5],[21, 25, 20]))
print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))




# def solution(progresses, speeds):
#     answer = []
#     janup = list(map(lambda x:100-x, progresses))
#     # print(janup)
#     ws = [x / y for x, y in zip(janup, speeds)]
#     work_speed = []
#     for i in ws:
#         if int(i) == i:
#             work_speed.append(i)
#         else:
#             i = int(i)+1
#             work_speed.append(i)

#     start_index = 0   --------> strat_index를 이곳에 두면 런타임 에러가 뜬다
    
#     while len(work_speed) != 0:
#         current_index = start_index
#         current_value = work_speed[current_index]
        
#         # 카운트 및 삭제
#         count = 1
#         while current_index + count < len(work_speed) and work_speed[current_index + count] <= current_value:
#             count += 1
#         del work_speed[current_index:current_index + count]
#         answer.append(count)
        
#         # 큰 값부터 다시 반복
#         current_index = len(work_speed) - 1

#     while True:
#         if not work_speed:
#             break
                    
            
#     return answer

# print(solution( [90, 90], [10, 9]))
# print(solution([5, 5, 5],[21, 25, 20]))
# print(solution([93, 30, 55],[1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))