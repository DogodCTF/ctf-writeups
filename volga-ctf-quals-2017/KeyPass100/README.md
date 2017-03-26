# Volga CTF Quals 2017 Keypass
### Category: Reverse, 100 points

>For reasons unknown an amature cryptographer wrote an application to generate 
>"strong encryption keys". One of these keys was used to encrypt a tar archive 
>with the flag. They used openssl command line util with -aes-128-cbc. 
>Could you please get the flag? It shouldn't take much time...

### Write-up


After messing about with the keypass program it was obvious that the passphrase generation was weak

´´´
$ ./keypass A
Ah=j&FQpX).Y!x2?H
$ ./keypass AA
BWf81zF%SdkxL*jL.
$ ./keypass AAA
Ah=j&FQpX).Y!x2?H
$ ./keypass AAAA
BWf81zF%SdkxL*jL.
´´´
Oops.
Lets generate some keys
´´´
for x in {0..255}
do
	export x
	./keypass $(perl -le 'print chr $ENV{x}')
done
´´´
>$sh generatekeys.sh > keys

Some of these inputs are invalid, the keyfile can be cleaned up or not, doesn't matter.
Now let's check how many unique keys there are.
´´´
with open("keys", "r") as ins:
    array = []
    a = 0;
    for line in ins:
        if line not in array:
            array.append(line)
            a = a + 1

print(a)
´´´
>$python uniquekeys.py
>251
>$ wc keys
>251  251 4518 keys
Cool, seems like all these keys are unique atleast.
Now let's try to crack that zip-file using the following script.

´´´
KEYS=`cat keys`

for k in $KEYS; do
        openssl aes-128-cbc -d -in flag.zip.enc -out a -pass pass:"$k"
        if [ $? -eq 0 ]
        then
                exit
        fi
done
´´´
However, no luck. After this, generation of keys of all possible inputs with 2 bytes was tested but this didn't
generate any more unique keys and took a long time.

After flailing around for a bit this hint was dropped

>$ openssl 
>OpenSSL> version
>OpenSSL 1.1.0e  16 Feb 2017

However, when we check this on the running machine
>$ openssl
>OpenSSL> version
>OpenSSL 1.0.2k  26 Jan 2017

Oops. Lets try this operation on a kali machine instead.


´´´
root@kali:~# apt-get update
root@kali:~# apt-get install openssl
root@kali:~# sh decrypt.sh
root@kali:~# unzip a
Archive:  a
 extracting: flag.txt                
root@kali:~# cat flag.txt 
VolgaCTF{L0ve_a11_trust_@_few_d0_not_reinvent_the_wh33l}
´´´

Much better.