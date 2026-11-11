from re import match
from functools import lru_cache
from sys import stdout
rls = {}


@lru_cache(137)
def cmp(ind, dpth=0):
    curr = rls[ind]
    return ('' if dpth > 4 else (
            curr[1] if '"' in curr else
            (f'''({"|".join([''.join([cmp(i) if i != ind
                                      else f'({cmp(ind, dpth+1)})'  
                                      for i in prt.split()])
                             for prt in curr.split('|')])})''' if '|' in curr
             else r''.join([cmp(i) for i in curr.split()]))))


def first_part(exps):
    return sum([match('^'+cmp('0')+'$', exp) is not None for exp in exps])


def second_part(exps):
    rls['8'], rls['11'] = '42 | 42 8', '42 31 | 42 11 31'
    return sum([match('^'+cmp('0')+'$', exp) is not None for exp in exps])


with open('input_19a.txt', 'r') as inp:
    inp_str = inp.read().split('\n\n')
    rls, exps = {exp[:exp.find(':')]: exp[exp.find(':') + 2:]
                 for exp in inp_str[0].split('\n')}, inp_str[1].split('\n')
    stdout.write(f'Day 19\nFirst part: {first_part(exps)}\n')
    cmp.cache_clear()
    stdout.write(f'Second part: {second_part(exps)}\n')