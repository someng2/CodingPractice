import Foundation

func solution(_ k:Int, _ d:Int) -> Int64 {
    var answer: Int64 = 0
    var x = 0
    
    for x in stride(from: 0, through: d, by: k) {
        let max_y = Int(sqrt(Double(d*d - x*x)))
        answer += Int64((max_y/k) + 1)
    }
    
    return answer
}
