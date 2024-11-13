from util import read_input, solve, test
import re

def part1(lines):
    cd = 'N'
    p = [0, 0]
    for e in lines[0].split(', '):
        q = int(e[1:])
        cd = {'N':{'R':'E','L':'W'},'E':{'R':'S','L':'N'},'S':{'R':'W','L':'E'},'W':{'R':'N','L':'S'}}[cd][e[0]]
        p = [p[0],p[1]+q] if cd=='N' else [p[0]+q,p[1]] if cd=='E' else [p[0],p[1]-q] if cd=='S' else [p[0]-q,p[1]]
    return abs(p[0]) + abs(p[1])

def part2(lines):
    cd = 'N'
    visited = set()
    p = (0, 0)
    for e in lines[0].split(', '):
        q = int(e[1:])
        cd = {'N':{'R':'E','L':'W'},'E':{'R':'S','L':'N'},'S':{'R':'W','L':'E'},'W':{'R':'N','L':'S'}}[cd][e[0]]
        for _ in range(q):
            p = (p[0],p[1]+1) if cd=='N' else (p[0]+1,p[1]) if cd=='E' else (p[0],p[1]-1) if cd=='S' else (p[0]-1,p[1])
            if p in visited:
                return abs(p[0]) + abs(p[1])
            visited.add(p)
    return None

day = __file__.split('day')[-1].split('.py')[0]
solve(part1, day)
solve(part2, day)
#test(part1, lines=['R5, L5, R5, R3'])
#test(part2, lines=['R8, R4, R4, R8'])