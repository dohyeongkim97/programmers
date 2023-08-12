// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    ALPHA = alpha.upper()

    alpha_dict = {}
    alpha_dict2 = {}
    ALPHA_DICT = {}
    ALPHA_DICT2 = {}
    for idx, val in enumerate(alpha):
        alpha_dict[idx] = val
        ALPHA_DICT[idx] = val.upper()
        alpha_dict2[val] = idx
        ALPHA_DICT2[val.upper()] = idx

    answer = []
    for i in s:
        if i == ' ':
            answer.append(i)
        elif i.lower()==i:
            answer.append(alpha_dict[(alpha_dict2[i]+n)%26])

        elif i.upper() == i:
            answer.append(ALPHA_DICT[(ALPHA_DICT2[i]+n)%26])

    answer = ''.join(answer)
    return answer