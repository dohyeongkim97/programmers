
def solution(people, limit):
    answer = 0
    people.sort()  # Sort the list once
    
    left = 0
    right = len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # Move left pointer to the right
        right -= 1    # Move right pointer to the left
        answer += 1   # Increment the number of boats
        
    return answer