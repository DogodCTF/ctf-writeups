import re

instr = re.findall('.', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_!@$1234567890{} ')
output = re.findall('..', '929193989a999b949695979c9e9d9fb0b2b1b3b8bab9bbb4b6b5828183888a898b848685878c8e8d8fa0a2a1a3a8aaa9aba4a6a5af128018323133383a393b343630b7be10')

alfa = dict(zip(output, instr))

flag = re.findall('..', '82a386a3b7983198313b363293399232349892369a98323692989a313493913036929a303abe')

for f in flag:
    print(alfa[f], end="")
print()

