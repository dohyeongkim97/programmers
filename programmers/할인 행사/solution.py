// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):
    answer = 0
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    for i in range(len(discount)-10+1):
        day_dict = {}
        for j in range(i, i+10):
            if discount[j] in day_dict.keys():
                day_dict[discount[j]] += 1
            else:
                day_dict[discount[j]] = 1
            
        if day_dict == want_dict:
            answer += 1
            
    return answer