def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        return len(cities)*5
    
    caches = []
    for i in cities:
        i = i.lower()
        if i in caches:
            answer += 1
            caches.remove(i)
            caches.append(i)
        else:
            answer += 5
            if len(caches) < cacheSize:
                caches.append(i)
            else:
                caches.pop(0)
                caches.append(i)
    
    return answer