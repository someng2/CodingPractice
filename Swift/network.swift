import Foundation

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    var sets: Set<Set<Int>> = []
    
    if computers.contains(Array(repeating: 1, count: n)) {
        return 1
    }
    
    for (i, c) in computers.enumerated() {
        var set: Set<Int> = [i+1]
        for (index, x) in c.enumerated()  {
            if i != index && x == 1 {
                set.insert(index+1)
            }
        }

        var isSame = false
        for other in sets {
            if !set.intersection(other).isEmpty {
                sets.remove(other)
                sets.insert(set.union(other))
                isSame = true
                set = set.union(other)
            }
        }
        if !isSame {
            sets.insert(set)
        }
    }
    
    return sets.count
}
