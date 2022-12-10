import Foundation

func solution(_ s:String) -> [Int] {
    var dict: [String: Int] = [:]
    var arr: [Int] = []
    
    for (index, value) in Array(s).map{String($0)}.enumerated() {
        if dict[value] != nil {
            arr.append(index - dict[value]!)
        }
        else {
            arr.append(-1)
        }
        dict[value] = index
    }
    return arr
}
