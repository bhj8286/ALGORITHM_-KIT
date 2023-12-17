def solution(nums):
    answer = 0
    max_pick = len(nums)/2 # 최대로 데려갈 수 있는 포켓몬의 수
    nums = set(nums)
    if len(nums) >= max_pick:  # 포켓몬의 종류가 최대로 데려갈 수 있는 포켓몬의 수보다 크거나 같은 경우는 
        answer = max_pick      # 최대로 데려갈 수 있는 포켓몬의 수 = max_pick
    else:                      #  포켓몬의 종류가 최대로 데려갈 수 있는 포켓몬의 수보다 적은 경우
        answer = int(len(nums))  # 종류수만큼만 가져갈 수 있다
    return answer

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))

# 근데 이게 왜 hash문제인지?