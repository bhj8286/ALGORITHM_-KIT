import heapq
def solution(operations):
    answer = []
    my =[]
    heapq.heapify(my)
    for i in operations:
        if i[0] == 'I':
            heapq.heappush(my, int(i.split()[1])) # I가 나온 경우 뒤의 숫자만 리스트에 넣기위해 띄어쓰기 기준으로 split후 리스트에 삽입
        elif i == "D -1" and len(my)!=0:
            heapq.heappop(my)
        elif i == "D 1" and len(my)!=0:
            my.pop(-1)
    my.sort()  ## my를 정렬해주었다. 근데 heappush를 사용하면 힙큐형태는 정렬이 되어나온다했는데 왜 필요한건가? 이 부분을 안넣으면 TC 6번이 통과가 안됨. 일반 리스트를 heapq.heapify()로 힙큐로 바꾸면 최소값은 [0]번째에 오는 것같음
    if len(my) != 0:
        answer.append(my[-1])
        answer.append(my[0])
    else:
        answer = [0,0]

    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

# sort부분: remove()나 pop(-1)을 한 경우 힙 구조가 깨진다함. 그래서 for문이 끝나고 sort를 시켜줘야하는 것같다. 
# 근데 그러면 elif i == "D 1" and len(my)!=0: my.pop(-1) 이 부분도 안돼야 하는거 아닌가?......

# 다른 사람 풀이
from heapq import heappush, heappop
def solution(arguments):
    max_heap = []
    min_heap = []
    for arg in arguments:
        if arg == "D 1":
            if max_heap != []:
                heappop(max_heap)
                if max_heap == [] or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
        elif arg == "D -1":
            if min_heap != []:
                heappop(min_heap)
                if min_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        else:
            num = int(arg[2:])
            heappush(max_heap, -num)
            heappush(min_heap, num)
    if min_heap == []:
        return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]
