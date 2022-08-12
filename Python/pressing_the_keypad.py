import math

def solution(numbers, hand):
    answer = ''
    
    #  define dictionary (key: number , value: position)
    a = {1 : (0,0), 2:(1,0), 3 : (2,0), 4 : (0,1), 5 : (1,1), 6:(2,1), 7 : (0,2), 8 : (1,2), 9 : (2,2) , '*' : (0,3), 0 : (1,3), '#':(2,3)}
    # print(a)
    l = a['*']
    r = a['#']
    now = 'l'
    
    # use dictionary

    for n in numbers :
        print ("n = ", n)
        if (n in [1,4,7]) :
            l = a[n]
            answer = answer + 'L'
        elif (n in [3,6,9]) :
            r = a[n]
            answer = answer + 'R'
        else :
            # print("l = ", l)
            # print("r = ", r)
            # distance between current left finger & number
            
            dist_l = calculate_dist(l, a[n])
            print("dist_l : ", dist_l)
            # distance between current right finger & number
        
            dist_r = calculate_dist(r, a[n])
            print("dist_r : ", dist_r)
            if (dist_l < dist_r) :
                # print("dist_l < dist_r")
                l = a[n]
                answer = answer + 'L'
            elif (dist_l > dist_r) :
                r = a[n]
                answer = answer + 'R'
            else :
                if (hand == "left") :
                    l = a[n]
                    answer = answer + 'L'
                else :
                    r = a[n]
                    answer = answer + 'R'
    

    
    return answer

def calculate_dist(tuple_a, tuple_b):
    distance = 0
    for i in range(2):
        distance += abs(tuple_a[i] - tuple_b[i])
        
    return distance
    
