from copy import copy, deepcopy
import itertools as it
from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=22)
from collections import Counter
from math import prod

on = set()
valid_range_p1 = set(it.product(range(-50,51),range(-50,51),range(-50,51)))

input = """on x=-5..47,y=-31..22,z=-19..33
on x=-44..5,y=-27..21,z=-14..35
on x=-49..-1,y=-11..42,z=-10..38
on x=-20..34,y=-40..6,z=-44..1
off x=26..39,y=40..50,z=-2..11
on x=-41..5,y=-41..6,z=-36..8
off x=-43..-33,y=-45..-28,z=7..25
on x=-33..15,y=-32..19,z=-34..11
off x=35..47,y=-46..-34,z=-11..5
on x=-14..36,y=-6..44,z=-16..29
on x=-57795..-6158,y=29564..72030,z=20435..90618
on x=36731..105352,y=-21140..28532,z=16094..90401
on x=30999..107136,y=-53464..15513,z=8553..71215
on x=13528..83982,y=-99403..-27377,z=-24141..23996
on x=-72682..-12347,y=18159..111354,z=7391..80950
on x=-1060..80757,y=-65301..-20884,z=-103788..-16709
on x=-83015..-9461,y=-72160..-8347,z=-81239..-26856
on x=-52752..22273,y=-49450..9096,z=54442..119054
on x=-29982..40483,y=-108474..-28371,z=-24328..38471
on x=-4958..62750,y=40422..118853,z=-7672..65583
on x=55694..108686,y=-43367..46958,z=-26781..48729
on x=-98497..-18186,y=-63569..3412,z=1232..88485
on x=-726..56291,y=-62629..13224,z=18033..85226
on x=-110886..-34664,y=-81338..-8658,z=8914..63723
on x=-55829..24974,y=-16897..54165,z=-121762..-28058
on x=-65152..-11147,y=22489..91432,z=-58782..1780
on x=-120100..-32970,y=-46592..27473,z=-11695..61039
on x=-18631..37533,y=-124565..-50804,z=-35667..28308
on x=-57817..18248,y=49321..117703,z=5745..55881
on x=14781..98692,y=-1341..70827,z=15753..70151
on x=-34419..55919,y=-19626..40991,z=39015..114138
on x=-60785..11593,y=-56135..2999,z=-95368..-26915
on x=-32178..58085,y=17647..101866,z=-91405..-8878
on x=-53655..12091,y=50097..105568,z=-75335..-4862
on x=-111166..-40997,y=-71714..2688,z=5609..50954
on x=-16602..70118,y=-98693..-44401,z=5197..76897
on x=16383..101554,y=4615..83635,z=-44907..18747
off x=-95822..-15171,y=-19987..48940,z=10804..104439
on x=-89813..-14614,y=16069..88491,z=-3297..45228
on x=41075..99376,y=-20427..49978,z=-52012..13762
on x=-21330..50085,y=-17944..62733,z=-112280..-30197
on x=-16478..35915,y=36008..118594,z=-7885..47086
off x=-98156..-27851,y=-49952..43171,z=-99005..-8456
off x=2032..69770,y=-71013..4824,z=7471..94418
on x=43670..120875,y=-42068..12382,z=-24787..38892
off x=37514..111226,y=-45862..25743,z=-16714..54663
off x=25699..97951,y=-30668..59918,z=-15349..69697
off x=-44271..17935,y=-9516..60759,z=49131..112598
on x=-61695..-5813,y=40978..94975,z=8655..80240
off x=-101086..-9439,y=-7088..67543,z=33935..83858
off x=18020..114017,y=-48931..32606,z=21474..89843
off x=-77139..10506,y=-89994..-18797,z=-80..59318
off x=8476..79288,y=-75520..11602,z=-96624..-24783
on x=-47488..-1262,y=24338..100707,z=16292..72967
off x=-84341..13987,y=2429..92914,z=-90671..-1318
off x=-37810..49457,y=-71013..-7894,z=-105357..-13188
off x=-27365..46395,y=31009..98017,z=15428..76570
off x=-70369..-16548,y=22648..78696,z=-1892..86821
on x=-53470..21291,y=-120233..-33476,z=-44150..38147
off x=-93533..-4276,y=-16170..68771,z=-104985..-24507"""

input = puzzle.input_data

# for line in input.split('\n'):
#     instruction, rest = line.split(' ')
#     rest = rest.replace('x=','').replace('y=','').replace('z=','').replace('..',',')
#     nr = [int(i) for i in rest.split(',')]
#     for i in range(0,len(nr),2):
#         nr[i] = max(-50,nr[i])
#     for i in range(1,len(nr),2):
#         nr[i] = min(50,nr[i])
#     new_set = set(it.product(range(nr[0], nr[1]+1),range(nr[2], nr[3]+1),range(nr[4], nr[5]+1)))
#     if instruction == 'on':
#         on = on.union(new_set)
#     else:
#         on = on.difference(new_set)

# print(len(on))

cubes = []

def intersect(mold, stamp):
    def split_comps(comp):
        c = []
        moldc, stampc = mold[comp], stamp[comp]
        if stampc[0] > moldc[1] or stampc[1] < moldc[0]:
            return c
        clist = sorted(set.union(set(moldc),set(stampc)))
        for i in range(len(clist)-1):
            c.append((clist[i],clist[i]))
            c.append((clist[i]+1,clist[i+1]-1))
        c.append((clist[-1],clist[-1]))
        return c
    
    x = split_comps(0)
    y = split_comps(1)
    z = split_comps(2)
    if len(x)*len(y)*len(z) == 0:
        yield mold
    
    for cube in it.product(x,y,z):
        if all(cube[c][0] >= mold[c][0] and cube[c][1] <= mold[c][1] for c in range(3)) and \
           not all(cube[c][0] >= stamp[c][0] and cube[c][1] <= stamp[c][1] for c in range(3)):
           yield cube


    

def add(cube):
    new_set = []
    for old_cube in cubes:
        new_set.extend(intersect(old_cube,cube))
    new_set.append(cube)
    return new_set
        
    

def delete(cube):
    new_set = []
    for old_cube in cubes:
        new_set.extend(list(intersect(old_cube,cube)))
    return new_set

for line in input.split('\n'):
    instruction, rest = line.split(' ')
    rest = rest.replace('x=','').replace('y=','').replace('z=','').replace('..',',')
    cube = [int(i) for i in rest.split(',')]
    cube = ((cube[0],cube[1]),(cube[2],cube[3]),(cube[4],cube[5]))
    if instruction == 'on':
        cubes = add(cube)
    else:
        cubes = delete(cube)

volume = sum(prod(cube[i][1]-cube[i][0]+1 for i in range(3)) for cube in cubes)
puzzle.answer_b = volume