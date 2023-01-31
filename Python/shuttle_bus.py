from collections import deque

def getMin(time):
    hour = time[:2]
    minute = time[3:]
    return int(hour)*60 + int(minute)

def getTime(min):
    hour = min/60
    minute = min%60
    hour = '0'+str(int(hour)) if hour < 10 else str(int(hour))
    minute = '0'+str(int(minute)) if minute < 10 else str(int(minute))
    return hour + ':' + minute
    
def solution(n, t, m, timetable):
    time = getMin("09:00")
    timetable = list(map(getMin, timetable))
    
    # timetable 오름차순 정렬
    timetable = deque(sorted(timetable))
    
    # 1 ~ n-1번까지 다른 크루 탐
    breaker = False
    for _ in range(n-1):
        for _ in range(m):
            if timetable and timetable[0] <= time:
                timetable.popleft()
        time += t

    answer = getTime(time)

    # n번째: m번째보다 1분 빨리 도착해야 됨
    for _ in range(m):
        if timetable and timetable[0] <= time:
            crew = timetable.popleft()
        else:
            break
    else:
         answer = getTime(crew-1) 
    
    return answer
