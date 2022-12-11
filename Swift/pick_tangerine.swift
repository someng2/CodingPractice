import Foundation

func solution(_ k:Int, _ tangerine:[Int]) -> Int {
    var answer = 0
    var tang = 0
    var cnt = Dictionary( tangerine.map { ($0, 1) }, uniquingKeysWith: +)
  
    while tang < k {
        let max = cnt.values.max()!
        let keys = cnt.filter { $0.value == max }
        for (key, _) in keys {
            let left = k - tang
            if left > 0 {
                answer += 1
                if max <= left {
                    tang += max
                    cnt[key]! = 0
                } else {
                    tang += left
                    cnt[key]! -= left
                    return answer
                }
            } else {
                return answer
            }
        }
    }
    return answer
}
