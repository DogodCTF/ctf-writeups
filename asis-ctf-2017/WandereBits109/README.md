# Asis CTF 2017 Wandere Bits
### Category: Reverse, 109 points

> I lost my flag's bit under a cherry tree... Can you find it?

### Write-up

This binary takes an input from arg1, then it will generate a new string from the given argument and compare this to the string "82a386a3b7983198313b363293399232349892369a98323692989a313493913036929a303abf". The same input character will always result in the same output, a is 92, b is 91 etc. The only exception is the last character of the input, which will result in value+1. To get the flag we can simply give all valid characters as a input and break at the string compare.

![strcmp](https://raw.githubusercontent.com/DogodCTF/ctf-writeups/master/asis-ctf-2017/WandereBits109/strcmp.PNG)

We run the program with 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_!@$1234567890{} ' as a argument, and after hitting the breakpoint we print the value RDI is pointing to:
'929193989a999b949695979c9e9d9fb0b2b1b3b8bab9bbb4b6b5828183888a898b848685878c8e8d8fa0a2a1a3a8aaa9aba4a6a5af128018323133383a393b343630b7be11'

We can now create a python script that converts the string to the flag, we also need to remove 1 from the last byte of the string it compares against. 

```python
import re

instr = re.findall('.', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_!@$1234567890{} ')
output = re.findall('..', '929193989a999b949695979c9e9d9fb0b2b1b3b8bab9bbb4b6b5828183888a898b848685878c8e8d8fa0a2a1a3a8aaa9aba4a6a5af128018323133383a393b343630b7be10')

alfa = dict(zip(output, instr))

flag = re.findall('..', '82a386a3b7983198313b363293399232349892369a98323692989a313493913036929a303abe')

for f in flag:
    print(alfa[f], end="")
print()
```

This gives us the flag

> ASIS{d2d2791c6a18da9ed19ade28cb09ae05}
