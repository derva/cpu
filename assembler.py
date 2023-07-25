#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('inputs', type=str, help="Inputs arguments, this will be shown on help");

args = parser.parse_args()

def remove_empty_lines(input_string):
    lines = input_string.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    return "\n".join(non_empty_lines)

def parseAssembly(ass): 
    func, rs, rt, rd, off = [],'','','','';
    if (ass[:3] == 'ADD'):
        func.append(format(0, '04b'))
    elif ass[:3] == 'ORR':
        func.append(format(1, '04b'))
    elif ass[:3] == 'AND':
        func.append(format(2, '04b'))
    elif ass[:3] == 'XOR':
        func.append(format(3, '04b'))

    if ass[4:7] == '$r0':
        func.append(format(0, '02b'))
    elif ass[4:7] == '$r1':
        func.append(format(1, '02b'))
    elif ass[4:7] == '$r2':
        func.append(format(2, '02b'))
    elif ass[4:7] == '$r3':
        func.append(format(3, '02b'))
    
    if ass[9:12] == '$r0':
        func.append(format(0, '02b'))
    elif ass[9:12] == '$r1':
        func.append(format(1, '02b'))
    elif ass[9:12] == '$r2':
        func.append(format(2, '02b'))
    elif ass[9:12] == '$r3':
        func.append(format(3, '02b'))

    return func, rs, rt, rd, off;

a = []
with open(args.inputs, 'r') as file:
    # content = file.read()
    ass = ''
    lines = file.read().split('\n');
    for line in lines: 
        line = line.strip()
        if not line.startswith('#'):
            ass += line + ('\n')
    ass = remove_empty_lines(ass)
    for line in ass.split('\n'):
        a.append("".join(parseAssembly(line)[0]))

print(a)
print("First instruction is " + str(a[0]))
#a, b, c, d , e = parseAssembly(ass)
