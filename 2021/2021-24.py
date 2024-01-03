from copy import copy, deepcopy
import itertools as it
from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=24)
from collections import Counter
from math import prod
import networkx as nx
    
# for i0 in range(999,100,-1):
#     if any(j == '0' for j in str(i0)):
#         continue
#     z = [int(str(i0)[0])+8]
#     z.append(z[-1]*26+int(str(i0)[1])+16)
#     z.append(z[-1]*26+int(str(i0)[2])+4)
#     x0 = z[-1]%26-11
#     if x0 <= 0:
#         z.pop()
#         z.pop()
#         z.pop()
#         continue
#     r0 = range(1,10,1) if x0 <= 0 or x0 > 9 else range(x0,x0+1)
#     z[-1] //= 26
#     for i1 in r0:
#         if i1 != x0:
#             z.append(z[-1]*26+i1+1)
#         else:
#             z.append(z[-1])
#         for i2 in range(999,100,-1):
#             if any(j == '0' for j in str(i2)):
#                 continue
#             z.append(z[-1]*26+int(str(i2)[0])+13)
#             z.append(z[-1]*26+int(str(i2)[1])+5)
#             z.append(z[-1]*26+int(str(i2)[2])+0)
#             x1 = z[-1]%26-5
#             if x1 <= 0:
#                 z.pop()
#                 z.pop()
#                 z.pop()
#                 continue
#             r1 = range(1,10,1) if x1 <= 0 or x1 > 9 else range(x1,x1+1)
#             z[-1] = z[-1]//26
#             for i3 in r1:
#                 if i3 != x1:
#                     z.append(z[-1]*26+i3+10)
#                 else:
#                     z.append(z[-1])
#                 for i4 in range(1,10,1):
#                     z.append(z[-1]*26+i4+7)
#                     x2 = z[-1]%26
#                     if x2 <= 0:
#                         z.pop()
#                         continue
#                     r2 = range(1,10,1) if x2 <= 0 or x2 > 9 else range(x2,x2+1)
#                     z[-1] = z[-1]//26
#                     for i5 in r2:
#                         if i5 != x2:
#                             z.append(z[-1]*26+i5+2)
#                         else:
#                             z.append(z[-1])
#                         x3 = z[-1]%26-11
#                         if x3 <= 0:
#                             z.pop()
#                             continue
#                         r3 = range(1,10,1) if x3 <= 0 or x3 > 9 else range(x3,x3+1)
#                         z[-1] = z[-1]//26
#                         for i6 in r3:
#                             if i6 != x3:
#                                 z.append(z[-1]*26+i6+13)
#                             else:
#                                 z.append(z[-1])
#                             x4 = z[-1]%26-13
#                             if x4 <= 0:
#                                 z.pop()
#                                 continue
#                             r4 = range(1,10,1) if x4 <= 0 or x4 > 9 else range(x4,x4+1)
#                             z[-1] //= 26
#                             for i7 in r4:
#                                 if i7 != x4:
#                                     z.append(z[-1]*26+i7+15)
#                                 else:
#                                     z.append(z[-1])
#                                 x5 = z[-1]%26-13
#                                 if x5 <= 0:
#                                     z.pop()
#                                     continue
#                                 r5 = range(1,10,1) if x5 <= 0 or x5 > 9 else range(x5,x5+1)
#                                 z[-1] //= 26
#                                 for i8 in r5:
#                                     if i8 != x5:
#                                         z.append(z[-1]*26+i8+14)
#                                     else:
#                                         z.append(z[-1])
#                                     x6 = z[-1]%26-11
#                                     if x6 <= 0:
#                                         z.pop()
#                                         continue
#                                     r6 = range(1,10,1) if x6 <= 0 or x6 > 9 else range(x6,x6+1)
#                                     z[-1] //= 26
#                                     for i9 in r6:
#                                         if i9 != x6:
#                                             z.append(z[-1]*26+i9+9)
#                                         else:
#                                             z.append(z[-1])
#                                         if z[-1] == 0:
#                                             answer = "".join([str(i0),str(i1),str(i2),str(i3),str(i4),str(i5),str(i6),str(i7),str(i8),str(i9)])
#                                             puzzle.answer_a = answer
#                                             z.pop()
#                                             exit()
#                                         z.pop()
#                                     z.pop()
#                                 z.pop()
#                             z.pop()
#                         z.pop()
#                     z.pop()
#                 z.pop()
#             z.pop()
#             z.pop()
#             z.pop()
#         z.pop()
#     z.pop()
#     z.pop()
#     z.pop()
    
for i0 in range(100,1000,1):
    if any(j == '0' for j in str(i0)):
        continue
    z = [int(str(i0)[0])+8]
    z.append(z[-1]*26+int(str(i0)[1])+16)
    z.append(z[-1]*26+int(str(i0)[2])+4)
    x0 = z[-1]%26-11
    if x0 <= 0:
        z.pop()
        z.pop()
        z.pop()
        continue
    r0 = range(1,10,1) if x0 <= 0 or x0 > 9 else range(x0,x0+1)
    z[-1] //= 26
    for i1 in r0:
        if i1 != x0:
            z.append(z[-1]*26+i1+1)
        else:
            z.append(z[-1])
        for i2 in range(100,1000,1):
            if any(j == '0' for j in str(i2)):
                continue
            z.append(z[-1]*26+int(str(i2)[0])+13)
            z.append(z[-1]*26+int(str(i2)[1])+5)
            z.append(z[-1]*26+int(str(i2)[2])+0)
            x1 = z[-1]%26-5
            if x1 <= 0:
                z.pop()
                z.pop()
                z.pop()
                continue
            r1 = range(1,10,1) if x1 <= 0 or x1 > 9 else range(x1,x1+1)
            z[-1] = z[-1]//26
            for i3 in r1:
                if i3 != x1:
                    z.append(z[-1]*26+i3+10)
                else:
                    z.append(z[-1])
                for i4 in range(1,10,1):
                    z.append(z[-1]*26+i4+7)
                    x2 = z[-1]%26
                    if x2 <= 0:
                        z.pop()
                        continue
                    r2 = range(1,10,1) if x2 <= 0 or x2 > 9 else range(x2,x2+1)
                    z[-1] = z[-1]//26
                    for i5 in r2:
                        if i5 != x2:
                            z.append(z[-1]*26+i5+2)
                        else:
                            z.append(z[-1])
                        x3 = z[-1]%26-11
                        if x3 <= 0:
                            z.pop()
                            continue
                        r3 = range(1,10,1) if x3 <= 0 or x3 > 9 else range(x3,x3+1)
                        z[-1] = z[-1]//26
                        for i6 in r3:
                            if i6 != x3:
                                z.append(z[-1]*26+i6+13)
                            else:
                                z.append(z[-1])
                            x4 = z[-1]%26-13
                            if x4 <= 0:
                                z.pop()
                                continue
                            r4 = range(1,10,1) if x4 <= 0 or x4 > 9 else range(x4,x4+1)
                            z[-1] //= 26
                            for i7 in r4:
                                if i7 != x4:
                                    z.append(z[-1]*26+i7+15)
                                else:
                                    z.append(z[-1])
                                x5 = z[-1]%26-13
                                if x5 <= 0:
                                    z.pop()
                                    continue
                                r5 = range(1,10,1) if x5 <= 0 or x5 > 9 else range(x5,x5+1)
                                z[-1] //= 26
                                for i8 in r5:
                                    if i8 != x5:
                                        z.append(z[-1]*26+i8+14)
                                    else:
                                        z.append(z[-1])
                                    x6 = z[-1]%26-11
                                    if x6 <= 0:
                                        z.pop()
                                        continue
                                    r6 = range(1,10,1) if x6 <= 0 or x6 > 9 else range(x6,x6+1)
                                    z[-1] //= 26
                                    for i9 in r6:
                                        if i9 != x6:
                                            z.append(z[-1]*26+i9+9)
                                        else:
                                            z.append(z[-1])
                                        if z[-1] == 0:
                                            answer = "".join([str(i0),str(i1),str(i2),str(i3),str(i4),str(i5),str(i6),str(i7),str(i8),str(i9)])
                                            puzzle.answer_b = answer
                                            z.pop()
                                            exit()
                                        z.pop()
                                    z.pop()
                                z.pop()
                            z.pop()
                        z.pop()
                    z.pop()
                z.pop()
            z.pop()
            z.pop()
            z.pop()
        z.pop()
    z.pop()
    z.pop()
    z.pop()

    


    
