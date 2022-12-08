class Node :
    def __init__(self, prev = None, next = None):
        self.remove = False
        self.prev = prev
        self.next = next
        
def solution(n, k, cmd):
    answer = ""
    chart = [Node(i-1, i+1) for i in range(n)]
    chart[0].prev = None
    chart[n-1].next = None
    removed = []
    cur = k
    
    for c in cmd:
        x = c.split(" ")
        if x[0] == "U":
            for _ in range(int(x[1])):
                cur = chart[cur].prev
        elif x[0] == "D":
            for _ in range(int(x[1])):
                cur = chart[cur].next
        elif x[0] == "C":
            removed.append(cur)
            chart[cur].remove = True
            p , n = chart[cur].prev, chart[cur].next
            
            if p != None:   # if p 로만 조건문을 하면 p가 0일 경우(맨처음index)를 체크하지 못함!
                chart[p].next = n
            if n:
                chart[n].prev = p
                cur = n
            else:
                cur = p
            
        else:
            restore = removed.pop()
            chart[restore].remove = False
            p , n = chart[restore].prev, chart[restore].next
            if p:
                chart[p].next = restore
            if n:
                chart[n].prev = restore
            
    for x in chart:
        if x.remove == False:
            answer += 'O'
        else:
            answer += 'X'
    
    return answer
