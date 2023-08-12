// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    answer = 0
    speak = ['aya', 'ye', 'woo', 'ma']
    speak2 = ['ayaaya', 'yeye', 'woowoo', 'mama']
    for i in babbling:
        for word in speak2:
            if word in i:
                break
            
        else:
            for word in speak:
                i = i.replace(word, '-')
                if set(i) == {'-'}:
                    answer += 1
                    break

    return answer