import math
def solution(arr):
    def lcm(a,b):
        return (a * b) // math.gcd(a,b)
    
    lcm_ = 1
    for i in arr:
        lcm_ = lcm(lcm_, i)
    
    answer = lcm_
    return answer