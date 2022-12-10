import Foundation

class Queue<T> {
    var enQueue: [T]
    var deQueue: [T] = []
    
    var count: Int {
        return enQueue.count + deQueue.count
    }
    
    var isEmpty: Bool {
        return enQueue.isEmpty && deQueue.isEmpty
    }
    
    init(_ queue: [T]) {
        self.enQueue = queue
    }
    
    func push(_ element: T) {
        enQueue.append(element)
    }
    
    func pop() -> T {
        if deQueue.isEmpty {
            deQueue = enQueue.reversed()
            enQueue.removeAll()
        }
        return deQueue.popLast()!
    }
    
}

func solution(_ queue1:[Int], _ queue2:[Int]) -> Int {
    var answer = 0
    var que1 = Queue<Int>(queue1)
    var que2 = Queue<Int>(queue2)
    var sum1 : CLong = queue1.reduce(0, +)
    var sum2 : CLong = queue2.reduce(0, +)
    
    if (sum1 + sum2) % 2 != 0 {
        return -1
    }
    let sum = (sum1 + sum2) / 2
    
    var count = 0
    while (!que1.isEmpty && !que2.isEmpty && count <= 600000) {
        if sum1 < sum {
            let temp = que2.pop()
            que1.push(temp)
            sum1 += temp
            answer += 1
        } else if sum1 > sum {
            let temp = que1.pop()
            que2.push(temp)
            sum1 -= temp
            answer += 1
        }
        if sum1 == sum {
            return answer
        }
        count += 1
    }
    
    if sum1 == sum {
        return answer
    } else {
        return -1
    }
    
    
}
