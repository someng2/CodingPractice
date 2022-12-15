import Foundation

func solution(_ n:Int, _ s:Int, _ a:Int, _ b:Int, _ fares:[[Int]]) -> Int {
    var answer = 0
    var node: [[Int]] = []
	
    // 자기 자신은 0, 나머지는 무한으로 초기화
    for i in 0..<n{
        node.append(Array(repeating: 999999, count: n))
        node[i][i] = 0
    }
    
    // fares에 있는 비용으로 초기화
    for i in fares{
        node[i[0]-1][i[1]-1] = i[2]
        node[i[1]-1][i[0]-1] = i[2]
    }

    // Floyd-Warshal 알고리즘
    for k in 0..<n{ // 거쳐가는 node
        for i in 0..<n{
            for j in 0..<n{
                // i->j로 가는 비용과 i -> k -> j 즉, k를 거쳐가는 비용을 비교
                node[i][j] = min(node[i][j] , node[i][k] + node[k][j])
            }
        }
    }
    answer = node[s-1][a-1] + node[s-1][b-1]
    
    for i in 0..<n{
    	// (s에서 i) + (i에서 a) + (i에서 b)의 최소 비용을 구해준다.
        answer = min(answer, node[s-1][i] + node[i][a-1] + node [i][b-1])
    }
    
    return answer
}
