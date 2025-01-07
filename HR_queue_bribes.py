# %%Hackerrank queue bribes

def minimumBribes(q):
    # Write your code here
    bribes = 0
    q = [ele - 1 for ele in q]
    for i in range(len(q)):
        diff = q[i] - i
        if diff > 2:
            print('Too chaotic')
        for k in q[max(q[i] - 1, 0):i]:
            if k > q[i]:
                bribes += 1
    print(bribes)

q = [1, 2, 5, 3, 7, 8, 6, 4]
# q = [2,1,5,3,4]
# q = [1, 2, 5, 3, 4, 7, 8, 6]
minimumBribes(q)