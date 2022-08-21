def solution(record):
    result = []
    user = {}
    
    for x in record:
        temp = x.split()
        message = temp[0]
        uid = temp[1]
        nick = ''
        if len(temp) == 3:
            nick = temp[2]
        # print(message, ',', uid, ',', nick)
        
        if message == "Enter" or message == "Change":
            user[uid] = nick

        # print('user = ', user)
        
    for x in record:
        temp = x.split()
        message = temp[0]
        uid = temp[1]
        
        if message == "Enter":
            result.append(user[uid] + "님이 들어왔습니다.")
        elif message == "Leave":
            result.append(user[uid] + "님이 나갔습니다.")
            
        # print('result = ', result, '\n')
        
    return result
