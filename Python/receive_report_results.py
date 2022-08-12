def solution(id_list, report, k):

    answer = [0] * len(id_list)
    
    # delete duplicate report
    report = set(report)
    
    # define dictionary 1 (key: user & value: reported user)
    # define deciotary 2 (key: user & value: reported count)
    d1 = {}
    d2 = {}
        
    for x in report:
        u1, u2 = x.split()
        if u1 not in d1:
            d1[u1] = [u2]
        else:
            d1[u1] += [u2]

        # print("d1 = ", d1)
        
        if u2 not in d2:
            d2[u2] = 1
        else:
            d2[u2] += 1

        # print("d2 = ", d2)

    
    # calculate stopped id
    for user, count in d2.items() :
        if count >= k:
            for u1, u2 in d1.items():
                if user in u2:
                    answer[id_list.index(u1)] += 1

    
    return answer
