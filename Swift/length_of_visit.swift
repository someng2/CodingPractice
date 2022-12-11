import Foundation

func solution(_ dirs:String) -> Int {
    var dict: [[Int]: Int] = [:]
    var now = [0,0]
    var prev = [0,0]
    var new = prev + now
    var answer = 0
    
    for x in dirs {
        prev = now
        switch x {
        case "L":
            if (-5 <= prev[0]-1) {
                now = [prev[0]-1, prev[1]]
                new = now + prev
            }
        case "R":
            if (prev[0]+1 <= 5) {
                now = [prev[0]+1, prev[1]]
                new = prev + now
            }
        case "U":
            if (prev[1]+1 <= 5) {
                now = [prev[0], prev[1]+1]
                new = prev + now
            }
        case "D":
            if (-5 <= prev[1]-1) {
                now = [prev[0], prev[1]-1]
                new = now + prev
            }
        default:
            break
        }
        if dict[new] == nil {
            dict[new] = 1
            answer += 1
        }
    }
    
    return answer
}
