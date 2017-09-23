# CSAW Capture The Flag 2017 -- Misc CVV Challenge 100 points
# Ragul Balaji 2017
# flag{ch3ck-exp3rian-dat3-b3for3-us3}

from pwn import *
from random import Random
import random
import copy

## PURELY RANDOMLY GENERATED CARD NUMBERS WITH PREFIX CONSTRAINTS

amex = [] # INSERT UR OWN ARRAY OF NUMBERS

master = [] # INSERT UR OWN ARRAY OF NUMBERS

visa = [] # INSERT UR OWN ARRAY OF NUMBERS

discover = [] # INSERT UR OWN ARRAY OF NUMBERS


def completed_number(prefix, length):
    """
    'prefix' is the start of the CC number as a string, any number of digits.
    'length' is the length of the CC number to generate. Typically 13 or 16
    """

    ccnumber = prefix

    # generate digits

    while len(ccnumber) < (length - 1):
        digit = str(generator.choice(range(0, 10)))
        ccnumber.append(digit)

    # Calculate sum

    sum = 0
    pos = 0

    reversedCCnumber = []
    reversedCCnumber.extend(ccnumber)
    reversedCCnumber.reverse()

    while pos < length - 1:

        odd = int(reversedCCnumber[pos]) * 2
        if odd > 9:
            odd -= 9

        sum += odd

        if pos != (length - 2):

            sum += int(reversedCCnumber[pos + 1])

        pos += 2

    # Calculate check digit

    checkdigit = ((sum / 10 + 1) * 10 - sum) % 10

    ccnumber.append(str(checkdigit))

    return ''.join(ccnumber)


def credit_card_number(rnd, prefixList, length, howMany):

    result = []

    while len(result) < howMany:

        ccnumber = copy.copy(rnd.choice(prefixList))
        result.append(completed_number(ccnumber, length))

    return result


def output(title, numbers):

    result = []
    result.append(title)
    result.append('-' * len(title))
    result.append('\n'.join(numbers))
    result.append('')

    return '\n'.join(result)

def P(x):D=map(int,x);return sum(D+[d-d/5*9for d in D[-2::-2]])%10==0 #luhn's credit card number test, code golf'd

generator = Random()
generator.seed()

r = remote('misc.chal.csaw.io', 8308)

while True:
	m = str(r.recvline())
	print(m)
	if "Express" in m:
		r.send(str(amex.pop())+'\n')
	elif "Discover" in m:
		r.send(str(discover.pop())+'\n')
	elif "Visa" in m:
		r.send(str(visa.pop())+'\n')
	elif "Master" in m:
		r.send(str(master.pop())+'\n')
	elif "starts with" in m:
		num = str(m.split("I need a new card that starts with ")[1].split('!')[0])
		tempPrefixList = [[]]
		for c in num:
			tempPrefixList[0].append(c)
		cc = credit_card_number(generator, tempPrefixList, 13, 1)[0]
		print(cc)
		r.send(str(cc)+'\n')
	elif "ends with" in m:
		end = str(m.split("I need a new card which ends with ")[1].split('!')[0])
		#if(len(end) > 1):
		#	break;
		#else:
		while True:
			tempPrefixList = [[]]
			num = str(random.randint(1111,9999))
			for c in num:
				tempPrefixList[0].append(c)
			cc = credit_card_number(generator, tempPrefixList, 16, 1)[0]
			if end in str(cc)[-len(end):]:
				print(cc)
				r.send(str(cc)+'\n')
				break;
	elif "is valid! (0 = No, 1 = Yes)" in m:
		ccnum = m.split("I need to know if ")[1].split(" is valid! (0 = No, 1 = Yes)")[0]
		if P(ccnum):
			print(1)
			if len(ccnum) == 15:
				print("OVERRIDE", 0)
				r.send('0\n')
			else:
				r.send('1\n')
		else:
			print(0)
			r.send('0\n')
	elif "Thanks" in m:
		continue
	elif "flag" in m:
		while True:
			print(m[:-1]) # GO NUTS
	else:
		#r.interactive()
		continue
