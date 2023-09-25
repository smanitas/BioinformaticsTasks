"""
Code Challenge: Solve the k-Universal Circular String Problem.

    Input: An integer k.
    Output: A k-universal circular string.

Sample Input:
3

Sample Output:
00111010
"""

import random

def generate_binary(k):
    return [bin(i)[2:].zfill(k) for i in range(2**k)]

def form_relation(k):
    nodes = generate_binary(k-1)
    d = {}
    for item in nodes:
        add1 = item[1:]+'0'
        add2 = item[1:]+'1'
        d[item] = [add1,add2]
    return d

def form_cycle(data):
    rgk = random.choice(list(data.keys()))
    rgv = random.choice(data[rgk])
    cycle = [rgk]
    while len(data) != 0:
        try:
            cycle.append(rgv)
            if len(data[rgk]) > 1:
                data[rgk].remove(rgv)
            else:
                del data[rgk]
            rgk = rgv
            rgv = random.choice(data[rgk])
            if rgv == cycle[0] and rgv == cycle[-1]:
                break
        except:
            break
    return cycle

def form_unCycle(data, rgk):
    choose = data[rgk]
    rgv = random.choice(choose)
    cycle = [rgk]
    while len(data) != 0:
        try:
            cycle.append(rgv)
            if len(data[rgk]) > 1:
                data[rgk].remove(rgv)
            else:
                del data[rgk]
            rgk = rgv
            rgv = random.choice(data[rgk])
            if rgv == cycle[0] and rgv == cycle[-1]:
                break
        except:
            break
    return cycle

def fuse(Cycle, new_Cycle):
    fuse_index = Cycle.index(new_Cycle[0])
    return Cycle[:fuse_index] + new_Cycle + Cycle[fuse_index+1:]

def eulerian_cycle(data, k):
    Cycle = form_cycle(data)
    while data:
        keys = list(data.keys())
        potential = list(set(Cycle) & set(keys))
        newStart = random.choice(potential)
        new_Cycle = form_unCycle(data, newStart)
        Cycle = fuse(Cycle, new_Cycle)
    return Cycle

def form_string(path):
    string = ''.join([item[-1] for item in path[1:]])
    return string

def k_universal_circular_string(k):
    data = form_relation(k)
    path = eulerian_cycle(data, k)
    result = form_string(path)
    return result

# Example usage
k = int(input("Enter the value of k: "))
result = k_universal_circular_string(k)
print(result)