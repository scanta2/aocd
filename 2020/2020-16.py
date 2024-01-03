from aocd.models import Puzzle
from collections import defaultdict
import re
from math import prod

def parse_fields(fields):
    parsed_fields = dict()
    ordered_fields = []
    for it in re.finditer('(.*): (\d+)\-(\d+) or (\d+)\-(\d+)',fields):
        f, r1, r2, r3, r4 = it.groups()
        parsed_fields[f] = (range(int(r1),int(r2)+1), range(int(r3),int(r4)+1))
        ordered_fields.append(f)
    return parsed_fields

def invalid_values(tickets, fields):
    for t in tickets:
        cumsum = 0
        for v in t:
            if sum(1 for r, val in fields.items() if v in val[0] or v in val[1]) == 0:
                cumsum += v
        yield(cumsum)

def is_ticket_valid(tickets, fields):
    for t in tickets:
        valid = True
        for v in t:
            if sum(1 for r, val in fields.items() if v in val[0] or v in val[1]) == 0:
                valid = False
                break
        yield(valid)

def part1(tickets, fields):
    return sum(invalid_values(tickets,fields))

def part2(my_ticket, tickets, fields):
    valid_mask = list(is_ticket_valid(tickets,fields))
    valid_tickets = [t for i,t in enumerate(tickets) if valid_mask[i]]
    num_valid = len(valid_tickets)
    field_list = list(f for f in fields)
    order = [None for i in range(len(field_list))]

    candidates = []
    for numbers in zip(*valid_tickets):
        valid = [sum(1 for n in numbers if n in fields[name][0] or n in fields[name][1]) == num_valid for name in field_list]
        cand = set([n for i,n in enumerate(field_list) if valid[i]])
        candidates.append(cand)
    
    while any([c is None for c in order]):
        for i,c in enumerate(candidates):
            if len(c) == 1 and order[i] == None:
                order[i] = list(c)[0]
                for cc in candidates:
                    if len(cc) != 0:
                        cc.remove(order[i])

    return prod(v for i,v in enumerate(my_ticket) if order[i].startswith('departure'))



PUZZLE = Puzzle(year=2020,day=16)
fields, my_ticket, tickets = PUZZLE.input_data.split('\n\n')
fields = parse_fields(fields)
my_ticket = list(map(int,my_ticket.splitlines()[1].split(',')))
tickets = tickets.splitlines()[1:]
tickets = [list(map(int,t.split(','))) for t in tickets]
PUZZLE.answer_a = part1(tickets,fields)
PUZZLE.answer_b = part2(my_ticket, tickets, fields)
