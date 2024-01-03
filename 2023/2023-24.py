from aocd.models import Puzzle
import re
import string
from math import prod, lcm
from itertools import chain, product, combinations, permutations
import operator
from collections import defaultdict, OrderedDict, Counter
from copy import copy, deepcopy
from sympy.ntheory.modular import crt
import functools
import numpy as np
import sympy

day = 24
year = 2023
puzzle = Puzzle(day=day, year=year)

debug = False
if debug == False:
    data = puzzle.input_data.split('\n')
else:
    data = puzzle.examples[0].input_data.split('\n')

paths = []
for line in data:
    px, py, pz, vx, vy, vz = map(int, re.findall(r"-?\d+", line))
    paths.append(((px,py,pz), (vx, vy, vz)))

def eval(path, time):
    ps, vs = path
    return np.array([p+v*time for p,v in zip(ps,vs)])

def part1():
    minc = 200000000000000
    maxc = 400000000000000

    inter = 0
    for pa, pb in combinations(paths,2):
        (pax, pay, paz), (vax, vay, vaz) = pa
        (pbx, pby, pbz), (vbx, vby, vbz) = pb
        if vbx*vay == vby*vax:
            continue
        u = (vay*(pax-pbx)+vax*(pby-pay))/(vbx*vay-vby*vax)
        t = (pbx+vbx*u-pax)/vax
        if u > 0 and t > 0 and minc <= pbx+u*vbx <= maxc and minc <= pby+u*vby <= maxc:
            inter += 1
    return inter

puzzle.answer_a = part1()

def part2():
    x = sympy.var('x')
    y = sympy.var('y')
    z = sympy.var('z')

    xv = sympy.var('xv')
    yv = sympy.var('yv')
    zv = sympy.var('zv')

    t1 = sympy.var('t1')
    t2 = sympy.var('t2')
    t3 = sympy.var('t3')

    p1, v1 = paths[0]
    p2, v2 = paths[1]
    p3, v3 = paths[2]

    equations = []

    equations.append(sympy.Eq(x + t1*xv, p1[0] + v1[0]*t1))
    equations.append(sympy.Eq(y + t1*yv, p1[1] + v1[1]*t1))
    equations.append(sympy.Eq(z + t1*zv, p1[2] + v1[2]*t1))

    equations.append(sympy.Eq(x + t2*xv, p2[0] + v2[0]*t2))
    equations.append(sympy.Eq(y + t2*yv, p2[1] + v2[1]*t2))
    equations.append(sympy.Eq(z + t2*zv, p2[2] + v2[2]*t2))

    equations.append(sympy.Eq(x + t3*xv, p3[0] + v3[0]*t3))
    equations.append(sympy.Eq(y + t3*yv, p3[1] + v3[1]*t3))
    equations.append(sympy.Eq(z + t3*zv, p3[2] + v3[2]*t3))

    d = sympy.solve(equations)[0]
    return d[x] + d[y] + d[z]

def part2elegant():
    # The unknown line is defined by f(x) = P + xV
    # Intersecting this line with three known lines gives
    # a non-linear system of 9 equations in 9 unknowns.
    # We could use sympy, but we can do better
    # The three vector equations are:
    # P-P0 = (V0-V)t
    # P-P1 = (V1-V)u
    # P-P2 = (V2-V)w
    #
    # These imply
    # (P-P0)x(V0-V) = 0
    # (P-P1)x(V1-V) = 0
    # (P-P2)x(V2-V) = 0
    # We now have too many equations, and a non-linear term
    # PxV. Since this term is present in all equations,
    # we can reduce the system to two vector equations by
    # subtracting eq 2 from 1 and eq 3 from 1
    # (P-P0)x(V0-V) = (P-P1)x(V1-V)
    # (P-P0)x(V0-V) = (P-P2)x(V2-V)
    #
    # (V1-V0)xP + (P0-P1)xV = P0xV0 - P1xV1
    # (V2-V0)xP + (P0-P2)xV = P0xV0 - P2xV2
    # The operator (A x) can also be expressed in matrix form,
    # using the Levi-Civita tensor.

    def crossToMatrix(A):
        return np.cross(np.eye(3, dtype=np.int64), A)
    
    P0, V0 = paths[0]
    P1, V1 = paths[1]
    P2, V2 = paths[2]

    P0 = np.array(P0, dtype=np.int64)
    P1 = np.array(P1, dtype=np.int64)
    P2 = np.array(P2, dtype=np.int64)
    V0 = np.array(V0, dtype=np.int64)
    V1 = np.array(V1, dtype=np.int64)
    V2 = np.array(V2, dtype=np.int64)
  
    A11 = crossToMatrix(V1-V0)
    A12 = crossToMatrix(P0-P1)
    A21 = crossToMatrix(V2-V0)
    A22 = crossToMatrix(P0-P2)
    A = np.block([[A11, A12], [A21, A22]])
    B = np.concatenate([np.cross(P0,V0)-np.cross(P1,V1),
                        np.cross(P0,V0)-np.cross(P2,V2)])
    X = np.linalg.solve(A,B)
    return int(sum(X[0:3]))
    
puzzle.answer_b = part2elegant() 




