import Foundation

func solution(_ t:String, _ p:String) -> Int {
    
    var answer = 0
    let len = p.count
    var last = t.count-(len-1)
    let target = Int(p)!
    
    for i in 0..<last {
        // let num = Int(t.substring(from: i, to: i+len-1))!
        let num = Int(t.dropFirst(i).prefix(p.count))!
        if num <= target {
            answer += 1
        }
    }
    
    return answer
}

extension String {
    func substring(from: Int, to: Int) -> String {
        guard from < count, to >= 0, to - from >= 0 else {
            return ""
        }
        
        let startIndex = index(self.startIndex, offsetBy: from)
        let endIndex = index(self.startIndex, offsetBy: to + 1) // '+1'이 있는 이유: endIndex는 문자열의 마지막 그 다음을 가리키기 때문
        
        return String(self[startIndex ..< endIndex])
    }
}
