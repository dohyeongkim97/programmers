import numpy as np

def solution(survey, choices):
    answer = ''
    choices = np.array(choices) - 4

    categories = {
        'RT': 0,
        'CF': 0,
        'JM': 0,
        'AN': 0
    }

    for i in range(len(choices)):
        surv = survey[i]
        choice = choices[i]
        if surv[0] == 'T':
            categories['RT'] += choice*-1
        elif surv[0] == 'F':
            categories['CF'] += choice*-1
        elif surv[0] == 'M':
            categories['JM'] += choice*-1
        elif surv[0] == 'N':
            categories['AN'] += choice*-1

        else:
            categories[surv] += choice

    for i in categories.keys():
        if categories[i] > 0:
            answer += i[1]
        else:
            answer += i[0]
        
    
    return answer