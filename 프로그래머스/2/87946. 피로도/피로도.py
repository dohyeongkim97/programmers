from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0
    
    for permutation in permutations(dungeons):
        current_fatigue = k
        count = 0
        
        for min_fatigue, fatigue_cost in permutation:
            if current_fatigue >= min_fatigue:
                current_fatigue -= fatigue_cost
                count += 1
            else:
                break
        
        max_dungeons = max(max_dungeons, count)
    
    return max_dungeons
