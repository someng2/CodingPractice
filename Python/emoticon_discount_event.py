from itertools import product

def solution(users, emoticons):
    answer = []
    discount_product = list(product([10, 20, 30, 40], repeat=len(emoticons)))
        
    for discounts in discount_product:
        count, profit = 0, 0
        for user_discount, user_money in users:
            user_expense = 0
            for emoticon, discount in zip(emoticons, discounts):
                if user_discount <= discount:
                    user_expense += emoticon*(100 - discount) / 100
                    if user_money <= user_expense:
                        break
            if user_expense >= user_money:
                count += 1
            else:
                profit += user_expense

        answer = max(answer, [count, profit])

    return answer
