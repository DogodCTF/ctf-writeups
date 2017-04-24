#!/bin/bash

RETN=`printf $1"\n" | strace ./no_flo_f51e2f24345e094cd2080b7b690f69fb 2>&1 | grep SIG | wc | cut -f 6 -d ' '`
exit $RETN

