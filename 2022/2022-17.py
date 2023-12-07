from aocd.models import Puzzle

rocks = {0: [0, 1, 2, 3],
         1: [1, 1j, 1+1j, 2+1j, 1+2j],
         2: [0, 1, 2, 2+1j, 2+2j],
         3: [0, 1j, 2j, 3j],
         4: [0, 1, 1j, 1+1j]}

width = 7
puzzle = Puzzle(day=17,year=2022)
wind = puzzle.input_data
# wind = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
dirs = {'d': -1j, '>': 1, '<': -1}

class State:
    def __init__(self,move,maxh,wind,enc):
        self.move = move
        self.maxh = maxh
        self.enc = enc
        self.wind = wind
    def key(self):
        return (self.move%5, self.wind, self.enc)
    def __repr__(self):
        return str(int(self.maxh.imag))



def solve(num):
    occupied = set()
    cache_h = 4
    row_enc = []
    def can_move(offset,rock):
        new_rock = [offset+i for i in rock]
        if any(i.real < 0 or i.real >=7 for i in new_rock):
            return False
        if any(i.imag < 0 for i in new_rock):
            return False
        if any(i in occupied for i in new_rock):
            return False
        return True

    def coderow(h):
        return sum(1<<int(i.real) for i in occupied if i.imag==h)
    
    max_height = 0
    w_idx = 0
    for ir in range(0,num):
        rock = rocks[ir%5]
        pos = max_height + 2+3j
        while True:
            if can_move(pos+dirs[wind[w_idx]],rock):
                pos += dirs[wind[w_idx]]
            w_idx = (w_idx+1)%len(wind)
            if can_move(pos-1j,rock):
                pos += -1j
            else:
                break
        occupied = occupied.union(set([pos+i for i in rock]))
        max_height = 1j*(max([i.imag for i in occupied])+1)
        key = (ir%5, w_idx, tuple(coderow(max_height.imag-i) for i in range(min(int(max_height.imag),20))))
        if key in (i.key() for i in row_enc):
            row_enc.append(State(ir,max_height,w_idx,key[2]))
            break
        else:
            row_enc.append(State(ir,max_height,w_idx,key[2]))
    if ir == num-1:
        return int(max_height.imag)
    idx = tuple(i.key() for i in row_enc).index(key)
    h0 = int(row_enc[idx].maxh.imag)
    h1 = int(row_enc[ir].maxh.imag)
    dh = h1-h0
    ndh = (num-1-idx)//(ir-idx)
    idx2 = num-idx-ndh*(ir-idx)+idx-1
    h2 = int(row_enc[idx2].maxh.imag)

    final = h0 + ndh*dh + h2-h0
    print(final)
solve(2022)
solve(1000000000000)
    
    
    

