'''
 Generate a pascal (Yang Hui) triangle
'''
def pascal(p):
    # my version
    tri = [[1]]
    for i in range(1,p):
        tri.append([1] + [tri[i-1][j]+tri[i-1][j+1] for j in range(len(tri[i-1])-1)] + [1])
    return tri

def pascal_2(p):
    # another implement
    t = [[1]]
    for _ in range(2, p + 1):
        t.append([1] + [a + b for a, b in zip(t[-1][:-1], t[-1][1:])] + [1])
    return t