from aocd.models import Puzzle
import re

def valid_password_part1(line):
    policy, password = line.split(':')
    password = password.replace(' ', '')
    policy_min, policy_max = [int(x) for x in re.findall(r"\d+", policy)]
    policy_letter = policy[-1]
    num_policy_letters = password.count(policy_letter)
    return num_policy_letters >= policy_min and num_policy_letters <= policy_max

def part1(input):
    return sum([valid_password_part1(x) for x in input])

def valid_password_part2(line):
    policy, password = line.split(':')
    password = password.replace(' ', '')
    indexes = [int(x) for x in re.findall(r"\d+", policy)]
    policy_letter = policy[-1]
    return sum([password[x-1] == policy_letter for x in indexes]) == 1

def part2(input):
    return sum([valid_password_part2(x) for x in input])

PUZZLE = Puzzle(year=2020,day=2)
INPUT = PUZZLE.input_data.split('\n')
PUZZLE.answer_a = part1(INPUT)
PUZZLE.answer_b = part2(INPUT)