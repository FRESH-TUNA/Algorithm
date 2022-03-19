def solution(progresses, speeds):
    answer = []
    while len(progresses) != 0:
        progresses = list(map(lambda x : progresses[x] + speeds[x], range(len(progresses))))
        count = 0
        while len(progresses) > 0 and progresses[0] >= 100:
            count += 1
            progresses = progresses[1:]
            speeds = speeds[1:]
        if count > 0:
            answer += [count]
    return answer

#######
def solution(progresses, speeds):
    result = []
    works = [[progresses[i], speeds[i]] for i in range(len(progresses))]
    
    # progresses가 다떫어질때까지 iteraation
    while works:
        
        # 시간처리
        for work in works:
            work[0] += work[1]

        # 배포
        if works[0][0] >= 100:
            finished_work_counts = 1
            for work in works[1:]:
                if work[0] >= 100:
                    finished_work_counts += 1
                else: break
            result.append(finished_work_counts)
            works = works[finished_work_counts:]
            
    return result