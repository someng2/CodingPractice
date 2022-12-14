import Foundation

func solution(_ brown:Int, _ yellow:Int) -> [Int] {
    var yellow = yellow
    var arr: [(Int, Int)] = []
    let sqr = Int(trunc(sqrt(Double(yellow))))
    for n in (1...sqr) {
        if yellow % n == 0 {
            let result1 = (yellow/n , n)
            arr.append(result1)
        }
    }

    for (h, w) in arr {
        if (h+2)*(w+2) - yellow == brown { return [h+2, w+2] }
    }

    return []
}
