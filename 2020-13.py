from aocd.models import Puzzle
import math
import string
import re

def part1(INPUT):
    min_ts = int(INPUT[0])
    bus_ids = re.finditer(r"[\d]+", INPUT[1])
    min_time_diffs = {}
    for id in bus_ids:
        i = int(id.group())
        min_time_diffs[i-min_ts%i] = i
    sol = min(min_time_diffs.keys())
    return sol*min_time_diffs[sol]

def mod_mult_inv(n, mod):
    '''Calculates and returns the modular multiplicative inverse of n % mod
    such that (n * n_inv) % mod == 1
    '''
    if mod == 1:
        return 1

    assert(math.gcd(n, mod) == 1)
    initial_mod = mod
    x, y = 0, 1
    while n > 1:
        q = n // mod
        n, mod = mod, n % mod
        x, y = y - q * x, x
    if y < 0:
        y += initial_mod
    return y

def chinese_remainder(congruencies):
    '''Efficiently calculates and returns the smallest number which works for
    all given congruences. For example, given the following:
    x % 5 == 2
    x % 7 == 3
    x % 11 == 8
    The smallest x which satisfies all three is 52.
    If no solution exists, returns None.
    Arguments:
    congruencies -- The list of congruencies to use. Expected to be a list of
    (mod, remainder) tuples.
    '''
    n = 1
    rem = 0
    for mod, r in congruencies:
        common_denom = math.gcd(n, mod)
        if common_denom > 1:
            # n and mod are not coprime, check for conflicts
            if rem % common_denom != r % common_denom:
                # There are no solutions as the congruences conflict
                # That is, the first congruence (sol % n == rem) and the
                # second congruence (sol % mod == r) imply *different* answers
                # mod common_denom!
                return None
            # These can be reduced by dividing out common_denom from one of the
            # congruences
            mod_cand = mod // common_denom
            if math.gcd(n, mod_cand) == 1:
                mod = mod_cand
                r %= mod
            else:
                # Dividing out common_denom from mod did *not* make n and mod coprime
                # Thus dividing common_denom from n should make them coprime
                n //= common_denom
                rem %= n
        next_n = n*mod
        mod_inv = mod_mult_inv(mod, n)
        n_inv = mod_mult_inv(n, mod)
        # Given two congruences: (x % mod == a) and (x % q == b)
        # If mod and q are coprime then multiplicative inverses exist such that
        # mod*mod_inv % q == 1 and q*q_inv % mod == 1
        # We can construct the following
        # y = (a*q*q_inv + b*mod*mod_inv) % (mod*q)
        # Then y % mod == a and y % q == b. Thus y is a solution
        # We can then merge these into a "super congruence" and merge in the next one!
        next_rem = (rem*mod*mod_inv + r*n*n_inv) % next_n
        n = next_n
        rem = next_rem
    # The final remainder is the smallest number which works for all congruencies!
    return rem

def offset_chinese_remainder(congruencies):
    '''Efficiently calculates and returns the smallest number which works for
    all given *offset* congruences. For example, given the following:
    (x + 2) % 5 == 0
    (x + 3) % 7 == 0
    (x + 8) % 11 == 0
    The smallest x which satisfies all three is 52.
    If no solution exists, returns None.
    Arguments:
    congruencies -- The list of congruencies to use. Expected to be a list of
    (mod, remainder) tuples.
    '''
    # Convert congruencies to chinese remainder form
    congruencies = [(mod, (mod - (offset % mod)) % mod)
                    for mod, offset
                    in congruencies]
    return chinese_remainder(congruencies)

def part2(INPUT):
    bus_ids = INPUT[1].split(',')
    bus_pos = {int(x): i for i,x in enumerate(bus_ids) if x.isdigit()}
    return offset_chinese_remainder([(x,bus_pos[x]) for x in bus_pos])

PUZZLE = Puzzle(year=2020,day=13)
INPUT = PUZZLE.input_data.splitlines()
PUZZLE.answer_a = part1(INPUT)
PUZZLE.answer_b = part2(INPUT)