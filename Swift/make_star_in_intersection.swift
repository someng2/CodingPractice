import Foundation

func solution(_ line:[[Int]]) -> [String] {
    
    var intersection: [(Int,Int)] = []
    var answer: [String] = []
    
    // 교점 좌표 구하기
    for i in 0..<line.count-1 {
        for j in i+1..<line.count {
            let A = line[i][0];   let B = line[i][1];   let E = line[i][2]
            let C = line[j][0];   let D = line[j][1];   let F = line[j][2]
            if (A*D-B*C) != 0 {
                if (B*F-E*D)%(A*D-B*C) == 0 && (E*C-A*F)%(A*D-B*C) == 0 {
                    let x = Double(B*F-E*D)/Double(A*D-B*C)
                    let y =  Double(E*C-A*F) / Double(A*D-B*C)
                    intersection.append((Int(x),Int(y)))
                }
            }   
        }
    }
    
    let row_s = intersection.map{$0.0}.min()!
    let row_e = intersection.map{$0.0}.max()!
    let col_s = intersection.map{$0.1}.min()!
    let col_e = intersection.map{$0.1}.max()!
    
    func containsTuple(_ array: [(Int, Int)], _ tuple:(Int,Int)) -> Bool {
        let (x, y) = tuple
        for (i, j) in array {
            if i == x && j == y { 
                return true 
            } 
        }
        return false
    }

    for i in (col_s...col_e).reversed() {
        var str = ""
        for j in row_s...row_e {
            let tupe = (j, i)
            if containsTuple(intersection,(j,i)) {
                str += "*"
            } else {
                str += "."
            }
        }
        answer.append(str)
    }
    
    return answer
}
