def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights.reverse()
    time = 0
    gone_truck = []

    while len(truck_weights) != 0:
        time += 1
        if time % bridge_length == 0:
            del gone_truck[0]
        while len(truck_weights) > 0 and sum(gone_truck) + truck_weights[-1] <= weight and len(gone_truck) < bridge_length:
            b = truck_weights.pop()
            gone_truck.append(b)
            if time % bridge_length == 0:
                del gone_truck[0]
            
    answer = time
    return answer

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))

# 참조 코드 
def solution(bridge_length, weight, truck_weights):
    time = 0
    p = list(truck_weights) # 트럭 무게
    x = [0] * bridge_length # 다리
    s=0
    while (x):
        time += 1
        s-=x.pop(0) # s: 다리 위의 총 트럭 무게
        if p:
            if ( s + p[0] ) <= weight:
                s+=p[0] # 여유되면 트럭 추가
                x.append(p.pop(0)) # 다리에 트럭 추가  
            else:
                x.append(0) # 여유 없으면 무게 0 추가

    return time
    
print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))