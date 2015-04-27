# use map & reduce for min dot product for 2 vectors
def min_dot(a, b):
    return reduce(lambda x,y: x+y, map(lambda x,y:x*y, sorted(a), sorted(b, reverse=True)))

if __name__ == '__main__':
    print min_dot([1,2,3,4,5,6], [0,1,1,1,0,0])
    
