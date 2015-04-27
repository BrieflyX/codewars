'''
use greedy algo to solve knapsack problem
'''

def knapsack(capacity, items):
    # Be greedy!
    wait_list = []
    result = [0] * len(items)
    for i, s in enumerate(items):
        wait_list.append((i, s[0], s[1]))
    wait_list.sort(key=lambda x:float(x[2])/x[1], reverse=True)
    while capacity > 0 and len(wait_list) > 0:
        if wait_list[0][1] <= capacity:
            capacity -= wait_list[0][1]
            result[wait_list[0][0]] += 1
        else:
            wait_list.pop(0)
    return result

if __name__ == '__main__':
    print knapsack(100, ((1, 1),(3, 4)))