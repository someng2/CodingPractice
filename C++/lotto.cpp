#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int rank(int count);
vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    
    vector<int> answer;
    int key = 0;
    int match_count = 0;
    int zero_count = 0;
    cout << "win_nums.size() = " << win_nums.size() << endl;
    
    for(int i = 0; i < win_nums.size(); i++) {
        key = win_nums[i];
        if (find(lottos.begin(), lottos.end(), key) != lottos.end()) {
            cout << "found matched number!" << endl;
            match_count ++;
            lottos.erase(remove(lottos.begin(),lottos.end(),key), lottos.end());
        }
    }
    cout << "match_count: " << match_count << endl;
    
    zero_count = count(lottos.begin(), lottos.end(), 0);
    cout << "zero_count: " << zero_count << endl;
    
    int total_count = match_count + zero_count;
    int ranking = 0;
    
    switch(total_count) {
        case 6:
            ranking = 1;
            break;
        case 5:
            ranking = 2;
            break;
        case 4:
            ranking = 3;
            break;
        case 3:
            ranking = 4;
            break;
        case 2:
            ranking =5;
            break;
        default:
            ranking =6;
    }
    
    answer.push_back(ranking);
    
        switch(match_count) {
        case 6:
            ranking = 1;
            break;
        case 5:
            ranking = 2;
            break;
        case 4:
            ranking = 3;
            break;
        case 3:
            ranking = 4;
            break;
        case 2:
            ranking =5;
            break;
        default:
            ranking =6;
    }
    answer.push_back(ranking);
    
    return answer;
}

