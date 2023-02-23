from collections import defaultdict
def solution(today, terms, privacies):
    answer = []
    term_dic = defaultdict(int)
    
    def calculateDate(accumulate_date, exp_month):
        year, month, day = accumulate_date.split('.')
        year, month = int(year), int(month)
        month += exp_month
        if month > 12:
            year += month // 12
            month = month % 12
            if month == 0:
                month = 12
                year -= 1
        return str(year) + '.' + str(month).zfill(2) + '.' + day
        
    # 오늘 날짜 >= (수집 일자+ 유효기간) : 파기
    for term in terms:
        term_dic[term.split(' ')[0]] = int(term.split(' ')[1])
    
    for i, privacy, in enumerate(privacies):
        accumulate_date, kind = privacy.split(' ')
        date = calculateDate(accumulate_date, term_dic[kind])
        if today >= date:
            answer.append(i+1)
    
    return answer
