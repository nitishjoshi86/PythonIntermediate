import copy



origi = [1,2,3,4,5,6]
cpy = copy.deepcopy(origi) #deepcopy or for shallow, just type copy
cpy[0] = -99
print(origi)
print(cpy)