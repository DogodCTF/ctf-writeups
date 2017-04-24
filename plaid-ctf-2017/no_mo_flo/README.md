# PlaidCTF 2017: no_mo_flo
### Category: Reverse, 125

> Can you go with the flow?

### Write-up

The binary expects 32 bytes input. If we enter less we get a "Short input" error message. If we enter an invalid input
the binary will return "You aint goin with the flow...." and with the correct input ""Good flow!!".

The first thing the binary does is to split the input string into two strings.
```C
for ( i = 0; i <= 15; ++i )
{
  buf1[i] = buf[2 * i];
  buf2[i] = buf[2 * i + 1];
}
```

It will when setup some signal with the sigaction syscall. Then it runs buf1 and buf2 through two different functions to validate the input.

![main](https://raw.githubusercontent.com/DogodCTF/ctf-writeups/master/plaid-ctf-2017/no_mo_flo/01_main.PNG)

Running the binary through strace with 32 A's as input, i noticed we got 42 SIGFPE(Floating point exception). Maybe we can use this to get the flag? I wrote a small python script to test for SIGFPE and print the input with the best score. This approach works for the characters in buf2. 
 
> ACAFAnA_AlA?AmA_AiAeAaA_A3AlAnA}

This looks like it could be a flag, the default head of the flag PCTF{ fits, and it ends with }.

I then went to the check_buf1 function to get the rest of the flag. In total 23 different checks are done on a string,
which is weird since the string only have 16 characters. Some chars are checked twice with different results!?

![main](https://raw.githubusercontent.com/DogodCTF/ctf-writeups/master/plaid-ctf-2017/no_mo_flo/02_checkbuf1.PNG)

Here the first character is checked twice, 'P' will pass the first check, and 'V' will pass the second check. I'm not sure whats going on here and i didn't debug it any further, for the characters with two possible results i simply guessed which one was likeliest to belong to the flag.


This gives us the flag:
> PCTF{n0_fl0?_m0_like_ah_h3ll_n0}
