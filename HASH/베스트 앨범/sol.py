def solution(genres, plays):
    answer = []
    matching = dict(zip(plays,genres))
    matching_2 = dict(zip(genres,plays))
    hap = {}
    for v in set(genres):
        hap[v] = 0    
    # print(matching)
    plays.sort(reverse=True)
    # print(plays)
    for i in plays:
        hap[matching[i]] += i

    max_key = max(hap, key=lambda k: hap[k])

    
    
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

import collections

def solution(genres, plays):
    answer = []
    
    # 1
    sumOfGenres = collections.defaultdict(int)  # 장르별 총 재생 횟수
    playsListDict = collections.defaultdict(list)  # 장르별로 나눠서 재생횟수와 인덱스 리스트로 저장
    print(sumOfGenres)
    print(playsListDict)
    # 2
    for i, genre, play in zip(range(len(genres)), genres, plays):
        sumOfGenres[genre] += play
        playsListDict[genre].append([i, play])  # 장르(키)의 밸류에 리스트를 계속 추가함: [인덱스, 재생횟수] 형태

    # 3
    items = sorted(sumOfGenres.items(), key=lambda x: x[1], reverse=True)  # 밸류기준 내림차순 정렬
    print(items)

    # 4
    for key, val in items:
        # 4-1
        # 해당 장르의 (인덱스, 재생횟수)를 재생횟수 기준 정렬
        playTimes = sorted(playsListDict[key], key=lambda x: x[1], reverse=True)
        # 4-2
        for idx, play in playTimes[:2]:
            answer.append(idx)
            
    return answer
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
