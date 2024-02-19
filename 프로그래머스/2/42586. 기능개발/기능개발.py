def solution(progresses, speeds):
    answer = []
    
    while progresses:

        done = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
                
        for i in progresses:
            if i >= 100:
                done += 1
            else:
                break
        
        if done:
            answer.append(done)
        for i in range(done):
            progresses.pop(0)
            speeds.pop(0)
    
    return answer