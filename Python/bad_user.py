from itertools import permutations as perm

def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    perms = list(perm(user_id, len(banned_id)))
    ban_set = []
    
    for users in perms:
        if not check(users, banned_id):
            continue
        else:
            if set(users) not in ban_set:
                ban_set.append(set(users))

    return len(ban_set)
