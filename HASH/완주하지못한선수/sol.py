def solution(participant, completion):
    answer = ''
    for i in participant:
        if participant.count(i) - 1 == completion.count(i):
            answer = i

    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))



def solution(participant, completion):
    hashdict = {}
    sumhash1 = 0
    sumhash2 = 0
    answer = ''
    for i in participant:
        hashdict[hash(i)] = i
        # print(hashdict)
        sumhash1 += hash(i)
    
    for j in completion:
        sumhash2 += hash(j)
    
    answer = hashdict[sumhash1-sumhash2]
    
    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))


# 다른 사람 풀이

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]