from aocd.models import Puzzle
import string
import re

def extract_passports(INPUT):
    passports = []
    passport = dict()
    for line in INPUT:
        if len(line) == 0:
            passports.append(passport)
            passport = dict()
            continue
        tokens = line.split(' ')
        for token in tokens:
            x,y = token.split(':')
            passport[x] = y
    passports.append(passport)
    return passports

def valid_passport_part1(passport,REQ_KEYS):
    present_keys = [x in passport.keys() for x in REQ_KEYS]
    return all(present_keys)

def valid_passport_part2(passport,REQ_KEYS):
    if valid_passport_part1(passport,REQ_KEYS):
        byr = passport['byr']
        valid = True
        valid &= byr.isdigit() and len(byr) == 4 and int(byr) in range(1920,2003)
        iyr = passport['iyr']
        valid &= iyr.isdigit() and len(iyr) == 4 and int(iyr) in range(2010,2021)
        eyr = passport['eyr']
        valid &= eyr.isdigit() and len(eyr) == 4 and int(eyr) in range(2020,2031)
        hgt = passport['hgt']
        valid &= (hgt[-2:] == 'cm' and hgt[:-2].isdigit() and int(hgt[:-2]) in range(150,194)) or \
                 (hgt[-2:] == 'in' and hgt[:-2].isdigit() and int(hgt[:-2]) in range(59,77))
        hcl = passport['hcl']
        valid &= hcl[0] == '#' and len(hcl) == 7 and all(c in string.hexdigits for c in hcl[1:])
        ecl = passport['ecl']
        valid &= ecl in ['amb','blu','brn','gry','grn','hzl','oth']
        pid = passport['pid']
        valid &= len(pid) == 9 and pid.isdigit() and ' ' not in pid
        return valid
    else:
        return False

def part1(passports,REQ_KEYS):
    return sum([valid_passport_part1(x,REQ_KEYS) for x in passports])

def part2(passports,REQ_KEYS):
    return sum([valid_passport_part2(x,REQ_KEYS) for x in passports])

REQ_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
PUZZLE = Puzzle(year=2020,day=4)
INPUT = PUZZLE.input_data.split('\n')
# INPUT = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm

# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929

# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm

# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in
# """.split('\n')
passports = extract_passports(INPUT)
# PUZZLE.answer_a = part1(passports,REQ_KEYS)
print(part2(passports,REQ_KEYS))