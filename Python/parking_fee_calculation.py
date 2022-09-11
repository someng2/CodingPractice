import collections
import math

def solution(fees, records):
    result = []
    
    def_time, def_fee, unit_time, unit_fee = fees
    record = collections.defaultdict(int)
    time_sum = collections.defaultdict(int)
    fee_result = collections.defaultdict(int)
    
    # records 배열 맨 뒤에서부터 조회
    # 1. 누적 주차시간 계산
    records.reverse()
    for x in records:
        time, car, state = x.split()
        hh, mm = time.split(":")
        minute = int(hh) * 60 + int(mm)
        if state == "OUT":
            record[car] = minute
        else:
            # 출차 기록 없을 경우 -> 23:59 출차
            if car not in record:
                time_sum[car] += 23*60+59 - minute
            else:
                time_sum[car] += record[car] - minute
                
    # 2. 주차 요금 계산
    for car, time in time_sum.items():
        fee_result[car] = calculate(def_time, def_fee, unit_time, unit_fee, time)
    
    # sort fee_result
    fee_result = sorted(fee_result.items())
    for car, fee in fee_result:
        result.append(fee)
    
    return result


def calculate(def_time, def_fee, unit_time, unit_fee, parking_time):
    if def_time >= parking_time:
        return def_fee
    else:
        time_left = parking_time - def_time
        return def_fee + math.ceil(time_left/unit_time) * unit_fee
