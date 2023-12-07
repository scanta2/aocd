from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, deque, Counter, OrderedDict
import queue
from itertools import combinations
from math import sqrt, floor, ceil

puzzle = Puzzle(year=2015,day=20).input_data.split('\n')

num_factors = dict()

def find_num_factors(num):
    temp1=sqrt(num)
    temp2=int(temp1)
    factors=set()
    factors.add(1)
    factors.add(num)
    if(temp1==temp2):
        for i in range (2,temp2):
            if(num%i==0):
                factors.add(i)
                factors.add(num//i)
        factors.add(temp2)
    else:
        for i in range (2,temp2+1):
            if(num%i==0):
                factors.add(i)
                factors.add(num//i)
    return sum([i for i in factors if i*50 >= num])


house_nr = 0
while True:
    house_nr += 1
    num_presents = find_num_factors(house_nr)*11
    if  num_presents >= 36000000:
        print(house_nr)
        break

