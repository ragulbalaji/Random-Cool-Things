# CSAW Capture The Flag 2017 -- Misc Serial Challenge 50 points
# Ragul Balaji 2017
# flag{@n_int3rface_betw33n_data_term1nal_3quipment_and_d@t@_circuit-term1nating_3quipment}

from pwn import *
import binascii

r = remote('misc.chal.csaw.io', 4239)

m = r.recvuntil('retransmit.\n')

flag = ""

for c in range(1000):
	m = str(r.recvline())
	count = 0
	for i in range(0,9+1):
		count += int(m[i])

	if(count%2 == int(m[10])):
		print(m[:-1], "PARITY FAIL")
		r.send('0\n')
	else:
		print(m[1:9])
		thisc = chr(int("0b"+str(m[1:9]),2))
		flag += thisc
		print("correct", m, thisc)
		print(flag)
		r.send('1\n')


#r.interactive()
