// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alpha_dict = {}
    alpha_dict2 = {}
    
    for idx, val in enumerate(alphabet):
        alpha_dict[val] = idx
        alpha_dict2[idx] = val

    answer = []
    for i in s:
        if i == ' ':
            answer.append(i)
        elif i.islower():
            shifted_idx = (alpha_dict[i] + n) % 26
            answer.append(alpha_dict2[shifted_idx])
        elif i.isupper():
            shifted_idx = (alpha_dict[i.lower()] + n) % 26
            answer.append(alpha_dict2[shifted_idx].upper())
    
    return ''.join(answer)