from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, deque, Counter
import queue
from itertools import combinations
buckets = Puzzle(year=2015,day=17).input_data.split('\n')
buckets = [int(x) for x in buckets]

num_combs = Counter()

for i in range(1,len(buckets)+1):
    for j in combinations(buckets,i):
        if sum(j) == 150:
            num_combs[i] += 1
print(num_combs)



