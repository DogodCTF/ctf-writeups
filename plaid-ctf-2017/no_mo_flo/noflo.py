#!/usr/bin/env python3

import subprocess

#head="ACAFAnA_AlA?AmA_AiAeAaA_A3AlAnA}A"
#tail=""

head="PCTF{n"
tail="_AlA?AmA_AiAeAaA_A3AlAnA}"

bestchar=str()
bestval=9001

for ch in range(0x21, 0x7e):
    if chr(ch) == "\'" or chr(ch) == "&" or chr(ch) == "-":
        continue

    ret = subprocess.call("./noflo.sh \'"+head+chr(ch)+tail+"\'", shell=True)

    print(chr(ch)+"=",ret)
    if bestval > ret:
        bestval=ret
        bestchar=chr(ch)

print("BEST SCORE: ", bestval, bestchar)
