from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=1)

def num_increasing_depths(depths, window=1):
    def win_list(depths, window):
        it = iter(depths)
        win = [next(it) for i in range(window)]
        yield sum(win)
        for e in it:
            win[:-1] = win[1:]
            win[-1] = e
            yield sum(win)
    d = tuple(win_list(depths,window))
    return sum(first > second for first, second in zip(d[1:],d))

depths = [int(i) for i in puzzle.input_data.split('\n')]
print(num_increasing_depths(depths))
print(num_increasing_depths(depths,3))
