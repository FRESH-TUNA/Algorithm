def solution(lines):
    datas = []
    answer = 0
    
    for line in lines:
        _, endTime, times = line.split()
        endTime = timeToMs(endTime)
        startTime = endTime - int(float(times[:-1])*1000)+1
        datas.append((startTime, endTime))
        
    for i in range(len(datas)):
        end = datas[i][1]
        count = 1
        
        for j in range(i+1, len(datas)):
            start = datas[j][0]
            if start < end+1000:
                count += 1
        answer = max(answer, count)
    return answer

# 20:59:57.421
def timeToMs(times):
    h, m, s = times.split(":")
    h, m, s = int(h), int(m), float(s)
    return h*3600*1000 + m*60*1000 + int(s*1000)

