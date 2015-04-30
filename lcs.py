'''
    Longest Common Subsequence
    Typical Dynamic Programming problem, containing my memory of OI career~
'''

def lcs(x, y):
    import numpy as np
    n = len(x)
    m = len(y)
    f = np.zeros((n+1, m+1),dtype='int')
    for i in range(n):
        for j in range(m):
            if x[i] == y[j]:
                f[i+1][j+1] = f[i][j] + 1
            else:
                f[i+1][j+1] = max(f[i+1][j], f[i][j+1])
    
    longest = ''
    i = n ; j = m ;
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            longest = x[i-1] + longest
            i -= 1; j -= 1;
        else:
            if f[i][j-1] > f[i-1][j]:
                j -= 1
            else:
                i -= 1
    return longest

if __name__ == '__main__':
    print lcs('a', 'b')
    print lcs('abcde', 'cdefg')