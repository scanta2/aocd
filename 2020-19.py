from aocd.models import Puzzle
import re
from itertools import product

def parse_rules(RULES):
    memory = {}
    for line in RULES.splitlines():
        i, rule = line.split(': ')
        if "\"" in rule:
            memory[i] = eval(rule)
        else:
            groups = rule.split(' | ')
            memory[i] = [g.split(' ') for g in groups]
    return memory

def part1(i,MSGS,RULES):
    def extract_rule(i,RULES):
        if isinstance(RULES[i],str):
            return [RULES[i]]
        else:
            r = []
            for g in RULES[i]:
                rule_parts = [extract_rule(j,RULES) for j in g]
                for i in product(*rule_parts):
                    r.append(''.join(i))
            return r
    rule0 = extract_rule(i,RULES)
    return sum(1 for m in MSGS.splitlines() if m in rule0)

def part2(i,MSGS,RULES):
    def extract_rule(i,RULES):
        if isinstance(RULES[i],str):
            return [RULES[i]]
        else:
            r = []
            for g in RULES[i]:
                rule_parts = [extract_rule(j,RULES) for j in g]
                for i in product(*rule_parts):
                    r.append(''.join(i))
            return r
    rule42 = extract_rule('42',RULES)
    rule31 = extract_rule('31',RULES)
    lenrule = len(rule42[0])
    count = 0
    for m in MSGS.splitlines():
        if len(m)%lenrule != 0:
            continue
        n_chunks = len(m)//lenrule
        chunks = [m[i:i+lenrule] for i in range(0,len(m),lenrule)]
        f = 1
        while n_chunks-2*f > 0:
            i = n_chunks-f
            if all(c in rule42 for c in chunks[:i]) and all(c in rule31 for c in chunks[i:]):
                count += 1
                break
            f += 1
    print(count)

PUZZLE = Puzzle(year=2020,day=19)
INPUT = PUZZLE.input_data
RULES, MSGS = INPUT.split('\n\n')
RULES = parse_rules(RULES)
PUZZLE.answer_a = part1('0',MSGS,RULES)
PUZZLE.answer_b = part2('0',MSGS,RULES)



