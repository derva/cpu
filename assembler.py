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
    func, rs, rt, rd, off = [0, 0, 0, 0, 0, 0],'','','','';
    if (ass[:3] == 'ADD'):
        func[0] = 0x0
    elif ass[:3] == 'ORR':
        func[0] = 0x1
    elif ass[:3] == 'AND':
        func[0] = 0x2
    elif ass[:3] == 'XOR':
        func[0] = 0x3

    if ass[4:7] == '$r1':
        func[1] = 0x1  
    elif ass[4:7] == '$r2':
        func[1] = 0x2
    elif ass[4:7] == '$r3':
        func[1] = 0x3
    elif ass[4:7] == '$r4':
        func[1] = 0x4
    
    if ass[9:12] == '$r1':
        func[2] = 0x1  
    elif ass[9:12] == '$r2':
        func[2] = 0x2
    elif ass[9:12] == '$r3':
        func[2] = 0x3
    elif ass[9:12] == '$r4':
        func[2] = 0x4

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
        a.append(parseAssembly(line)[0])

print(a)
#a, b, c, d , e = parseAssembly(ass)
