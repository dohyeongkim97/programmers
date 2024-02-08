def solution(id_list, report, k):
    import collections
    from collections import Counter
    
    id = {i: set() for i in id_list}

    answer = [0 for _ in id_list]

    for i in report:
        name, reported = i.split()
        id[name].add(reported)

    reported = []
    for i in id_list:
        for j in id[i]:
            reported.append(j)

    reported = Counter(reported)
    i = 0
    for name in id.keys():
        for j in id[name]:
            if reported[j] >= k:
                answer[i] += 1
        i += 1
    
    # for i in reported:
    #     if reported >= k:
    #         for j in range(len(list(id.keys()))):
    #             if i in id[list(id.keys())[j]]:
    #                 answer[j] += 1

    return answer