import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
    var index = 1
    var max = 0
    var arr: [(Int, Int)] = []
    
    for (i, x) in priorities.enumerated() {
        arr.append((x,i))
    }
    
    while !arr.isEmpty {
        max = arr.map{$0.0}.max()!
        while arr[0].0 < max {
            arr.append(arr.removeFirst())
        }
        if arr[0].1 == location {
            return index
        }
        arr.removeFirst()
        index += 1
    }
    
    return index
}
