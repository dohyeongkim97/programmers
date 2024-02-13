import itertools
from itertools import permutations
def solution(word):
    texts = 'AAAAAEEEEEIIIIIOOOOOUUUUU'
    texts_list = []
    for number in range(1, 6):
        for i in permutations(texts, number):
            words = ''
            for _ in i:
                words += _
                texts_list.append(words)
                

    texts_list = list(set(texts_list))
    texts_list.sort()
    answer = texts_list.index(word) + 1
    return answer