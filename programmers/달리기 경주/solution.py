// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    playing = {}
    playing2 = {}
    for idx, name in enumerate(players):
        playing[name] = idx
        playing2[idx] = name
        
    for name in callings:
        temp = playing[name]     
        temp2 = playing[name]-1  

# temp = playing['kai']
# temp2 = playing['kai']-1

        playing2[temp], playing2[temp2] = playing2[temp2], playing2[temp]

        playing[playing2[temp]] = temp
        playing[playing2[temp2]] = temp2
    
    answer = []
    for i in playing2:
        answer.append(playing2[i])
    return answer