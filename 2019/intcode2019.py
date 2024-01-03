import re
import string
from collections import defaultdict

def address(par,mode,relative = 0):
    if mode == 0:
        return par
    elif mode == 1:
        raise
    elif mode == 2:
        return relative+par

def value(par,mode,intcode,relative =0):
    if mode == 0:
        return int(intcode[par])
    elif mode == 1:
        return par
    elif mode == 2:
        return int(intcode[relative+par])
    

def convert(line):
    intcode_list = line.split(',')
    # convert to dictionary to allow for large memory
    intcode = defaultdict(lambda:'0')
    for i,tok in enumerate(intcode_list):
        intcode[i] = tok
    return intcode


nummodes = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1}
def parse(intcode,input = None, resume = 0, relative_base = 0):
    i = resume
    step = 1
    output = []
    while True:
        opcode = int(intcode[i][-2:])
        if opcode == 99:
            break
        revintcode = intcode[i][::-1]
        modes = [int(w) for w in revintcode[2:]]
        if modes is None:
            modes = []
        while len(modes) < nummodes[opcode]:
            modes.append(0)
        par = []
        for imode,mode in enumerate(modes):
            par.append(int(intcode[i+imode+1]))

        if opcode == 1:            
            intcode[address(par[2],modes[2],relative_base)] = str(value(par[1],modes[1],intcode,relative_base)+value(par[0],modes[0],intcode,relative_base))
            step = 4
        elif opcode == 2:           
            intcode[address(par[2],modes[2],relative_base)] = str(value(par[1],modes[1],intcode,relative_base)*value(par[0],modes[0],intcode,relative_base))
            step = 4
        elif opcode == 3:
            if len(input) == 0:
                return intcode, output, i, relative_base
            intcode[address(par[0],modes[0],relative_base)] = input.popleft()
            step = 2
        elif opcode == 4:
            output.append(str(value(par[0],modes[0],intcode,relative_base)))
            step = 2
        elif opcode == 5:
            if value(par[0],modes[0],intcode,relative_base) != 0:
                step = 0
                i = value(par[1],modes[1],intcode,relative_base)
            else:
                step = 3
        elif opcode == 6:
            if value(par[0],modes[0],intcode,relative_base) == 0:
                step = 0
                i = value(par[1],modes[1],intcode,relative_base)
            else:
                step = 3
        elif opcode == 7:
            intcode[address(par[2],modes[2],relative_base)] = '1' if value(par[0],modes[0],intcode,relative_base) < value(par[1],modes[1],intcode,relative_base) else '0'
            step = 4
        elif opcode == 8:
            intcode[address(par[2],modes[2],relative_base)] = '1' if value(par[0],modes[0],intcode,relative_base) == value(par[1],modes[1],intcode,relative_base) else '0'
            step = 4
        elif opcode == 9:
            relative_base += value(par[0],modes[0],intcode,relative_base)
            step = 2
        else:
            raise LookupError
        i += step
    return intcode, output, -1, relative_base
