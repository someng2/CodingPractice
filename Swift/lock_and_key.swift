import Foundation

func check(_ arr:[[Int]],_ N:Int) -> Bool {
    for x in 0..<N {
        for y in 0..<N {
            if arr[x + N][y + N] != 1 {
                return false
            }
        }
    }
    return true
}

func solution(_ key:[[Int]], _ lock:[[Int]]) -> Bool {
    let M = key.count
    let N = lock.count
    var key = key
    // 3배 더 큰 자물쇠
    var new_lock = Array(repeating: Array(repeating: 1,count:3*N ), count: 3*N)
    
    func spin_left(_ arr: [[Int]]) -> [[Int]] {
        var rotatedKey = [[Int]](repeating: [Int](repeating: 0, count: M), count: M)
        for col in 0..<M {
            for row in (0..<M).reversed() {
                rotatedKey[col][M - 1 - row] = key[row][col]
            }
        }
        return rotatedKey
    }
    
    // 기존 자물쇠를 새로운 자물쇠 가운데에 위치
    for x in 0..<N {
        for y in 0..<N {
            new_lock[x+N][y+N] = lock[x][y]
        }
    }
    for _ in 0..<4 {
        key = spin_left(key)
        for lock_x in 0..<N*2 {
            for lock_y in 0..<N*2 {
                // key를 new_lock에 꽂음
                for key_x in 0..<M {
                    for key_y in 0..<M {
                        new_lock[lock_x + key_x][lock_y + key_y] += key[key_x][key_y]
                    }
                }
                // new_lock의 중앙 확인
                if check(new_lock, N) { return true }
                // key를 new_lock에서 뺌
                 for key_x in 0..<M {
                    for key_y in 0..<M {
                        new_lock[lock_x + key_x][lock_y + key_y] -= key[key_x][key_y]
                    }
                }
            }
        }
        
    }
    
    
    return false
}
