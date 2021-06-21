#collections: counter, namedtuple, orderdict, default dict, deque

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque


""" a = 'aaaaaabbbbbbcc'
mycounter = Counter(a)

print(mycounter.items())
print(mycounter.most_common(1)[0][0])
print(list(mycounter.elements())) """
 

""" point = namedtuple('point','x,y')
pt = point(1,-4)
print(pt) """

""" Ordict=OrderedDict()
Ordict['a'] = 1
Ordict['b'] = 2
Ordict['c'] = 3
Ordict['d'] = 4

print(Ordict) """


""" d = defaultdict(int)
d['a'] = 1
d['b'] = 2

print(d['c']) """

""" d = deque()
d.append(1)
d.append(2)

d.appendleft(3)
print(d) """

