import Foundation

// solution1: Queue 이용

func solution1(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var answer: [Int] = []
    var daysleft: [Int] = []
    
    for (i, pro) in progresses.enumerated() {
        if (100-pro)%speeds[i] == 0 {
            daysleft.append((100-pro)/speeds[i] )
        } else {
            daysleft.append(Int((100-pro)/speeds[i])+1 )
        }
    }

    var today = 0
    while !daysleft.isEmpty {
        var count = 1
        today = daysleft.removeFirst()
        
        while !daysleft.isEmpty && daysleft[0] <= today {
            count += 1
            daysleft.removeFirst()
        }
        
        answer.append(count)
    }
    
    
    return answer
}

// solution2

func solution2(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var lastReleaseDate: Int = 0
    var numOfReleases: [Int] = []
    for i in 0..<progresses.count {
        let progress = Double(progresses[i])
        let speed = Double(speeds[i])
        let day = Int(ceil((100 - progress) / speed))
        if day > lastReleaseDate {
            lastReleaseDate = day
            numOfReleases.append(1)
        } else {
            numOfReleases[numOfReleases.count - 1] += 1
        }
    }
    return numOfReleases
}
