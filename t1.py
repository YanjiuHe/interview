def minimumCnt(source, target):
    next = [{} for i in range(len(source))]

    for i in range(ord('a'), ord('z')+1):
        next[-1][chr(i)] = -1

    i = len(next)-2

    while (i>=0) :
        next[i] = next[i+1].copy()
        next[i][source[i+1]] = i+1
        i-=1

    head = next[0].copy()
    head[source[0]] = 0


    ans = 0
    idx = -1

    for i in range(len(target)):
        if (head[target[i]]==-1): return -1
        if (idx==-1):
            ans+=1
            idx = head[target[i]]
        else:
            idx = next[idx][target[i]]
            if (idx==-1):
                ans+=1
                idx = head[target[i]]
    return ans

test_cases = [
    ('abc', 'abcbc'),
    ('abc', 'acdbc'),
    ('xyz', 'xzyxz')
]

for source, target in test_cases:
    print(minimumCnt(source, target))