'''
Union of Closed Intervals

Write a function interval_insert which takes as input a list myl of disjoint closed intervals with integer endpoints, sorted by increasing order of left endpoint, and an interval interval, and returns the union of interval with the intervals in myl, expressed as a union of disjoint intervals.

Example

[(1, 2)], (3, 4)-> [(1, 2), (3, 4)]
[(3, 4)], (1, 2)-> [(1, 2), (3, 4)]
[(1, 2), (4, 6)], (1, 4) -> [(1, 6)] [(0, 2), (3, 6), (7, 7), (9, 12)], (1, 8) -> [(0, 8), (9, 12)]
'''

# use hash to solve it
def interval_insert (myl, interval):
    d = {}
    space = range(0,100)
    for i in space:
        d[i] = 0
    for x,y in myl:
        for i in range(x,y):
            d[i] = 1
    for i in range(interval[0], interval[1]):
        d[i] = 1
    start = -1
    new_l = []
    for i in space:
        if d[i] == 1:
            if start == -1:
                start = i
        else:
            if start is not -1:
                new_l.append((start, i))
                start = -1
    return new_l

if __name__ == '__main__':
    print interval_insert([(1,2)], (3,4))
    print interval_insert([(1,2), (3,4)], (2,3))
    print interval_insert([(1,2), (3,4), (5,6)], (2,3))