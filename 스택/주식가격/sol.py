# 내 풀이: 반례가 없어 보인다. 질문하기에 있는 반례들 다 통과하는데 TC1빼고 다 실패함 ㅜ
# def solution(prices):
#     answer = []
#     for i in range(len(prices)-1):
#         sub_prices = prices[i:]  # 슬라이싱하여 원본 리스트를 변경하지 않도록 함
#         if prices[i] == min(sub_prices):
#             answer.append(len(prices)-(i+1))
#         elif prices[i] > prices[i+1]:
#             answer.append(1)
#         else:
#             answer.append(sub_prices.index(min(sub_prices))) # min(sub_prices)으로 하면 안되고 그 수보다 작기만 한 수를 찾으면 된다
    
#     answer.append(0)
#     return answer

# print(solution([1, 2, 3, 4, 5, 6, 1, 1, 2, 3, 1, 2, 3]))
# print(solution([1, 2, 3, 4, 1]))
# print(solution([5, 4, 3, 2, 5]))

# any 찾아보기

# 수정 코드 
def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        sub_prices = prices[i:]  # 슬라이싱하여 원본 리스트를 변경하지 않도록 함
        for k in sub_prices:
            if prices[i] > k:
                ga = k
                break
        if prices[i] == min(sub_prices):
            answer.append(len(prices)-(i+1))
        else:
            answer.append(sub_prices.index(ga))
    
    answer.append(0)
    return answer

print(solution([2, 5, 8, 4, 2]))
print(solution([1, 2, 3, 4, 5, 6, 1, 1, 2, 3, 1, 2, 3]))
print(solution([1, 2, 3, 4, 1]))
print(solution([5, 4, 3, 2, 5]))

# 시간 복잡도 개선
def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer