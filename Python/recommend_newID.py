def solution(new_id):
    answer = ''
    
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환
    new_id = new_id.lower()
    # print('1단계 -> ', new_id)

# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    for c in new_id:
        if not filter(c):
            new_id = new_id.replace(c, '')
    # print('2단계 -> ', new_id)
    
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    # print('3단계 -> ', new_id)

# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거
    if new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) >= 1:
        # print("new_id[-1] = ", new_id[-1])
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # print('4단계 -> ', new_id)

# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입
    if not new_id:
        new_id = "a"
    # print('5단계 -> ', new_id)
    
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
#  만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]

        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # print('6단계 -> ', new_id)

# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임

    if len(new_id) <= 2:
        while (len(new_id) < 3):
            new_id = new_id + new_id[-1]

    # print('7단계 -> ', new_id)
    
    return new_id

def filter(c):
    return ((c in ['-','_','.']) or (c.isdigit()) or (c.isalpha()))
