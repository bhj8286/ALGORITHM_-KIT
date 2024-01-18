import heapq
def solution(jobs):
    answer = 0
    hap = 0
    jongryo_list = []
    flipped_list = []
    heapq.heapify(flipped_list)
    for i in jobs:
        i = i[::-1] # 작업시간 적은 순서대로 꺼내기위해 리스트를 [[3, 0], [9, 1], [6, 2]]로 바꾸어줌
        heapq.heappush(flipped_list,i)
    while len(flipped_list) != 0:
        a= heapq.heappop(flipped_list)
        hap += a[0]
        jongryo = hap - a[1]
        jongryo_list.append(jongryo)
    answer = sum(jongryo_list)/len(jobs)
    return answer

print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 5], [1, 2], [5, 5]]))

import heapq
def solution(jobs):
    answer = 0
    hap = 0
    j = len(jobs)
    jongryo_list = []
    zero_jobs = []
    not_zero_jobs = []
    flipped_list = []
    for i in jobs:
        if i[0] == 0:
            zero_jobs.append(i)
        else:
            not_zero_jobs.append(i)
    print(zero_jobs)
    print(not_zero_jobs)
    heapq.heapify(zero_jobs)
    heapq.heapify(not_zero_jobs)
    heapq.heapify(flipped_list)
    while len(zero_jobs) != 0:
        a= heapq.heappop(zero_jobs)
        hap += a[1]
        jongryo = hap - a[0]
        jongryo_list.append(jongryo)
    for i in not_zero_jobs:
        i = i[::-1] # 작업시간 적은 순서대로 꺼내기위해 리스트를 [[3, 0], [9, 1], [6, 2]]로 바꾸어줌
        heapq.heappush(flipped_list,i)
    while len(flipped_list) != 0:
        a= heapq.heappop(flipped_list)
        hap += a[1]
        jongryo = hap - a[0]
        jongryo_list.append(jongryo)
    answer = sum(jongryo_list)/j
    return answer
print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 5], [1, 2], [5, 5]]))


