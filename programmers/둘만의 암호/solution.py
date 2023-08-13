// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        alpha = alpha.replace(i, '')

    alphabet = {}
    alphabet_idx = {}
    for idx, char in enumerate(alpha):
        alphabet[char] = idx
        alphabet_idx[idx] = char

    S = []
    Skip = []

    answer = ''

    for i in s:
        char = alphabet_idx[(alphabet[i] + index)%(26-len(skip))]
        answer+=char


    return answer