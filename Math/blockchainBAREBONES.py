import random
import hashlib

challengelen = 2
chain = []



def mine(lastblock, txns):
	hash = '1'*challengelen
	nonce = 0
	while hash[:challengelen] != '0'*challengelen:
		hash = hashlib.md5(lastblock[4] + '|' + txns + '|' + str(nonce)).digest()
		nonce += 1
		#print(txns, nonce, hash[:challengelen])
	return (lastblock[0]+1, lastblock[4], txns, nonce, hash)



# Genesis Block
genlasthash = 'Genesis'
gentxns = '<3 R4gul'
genhash = '1'*challengelen
gennonce = 0

while genhash[:challengelen] != '0'*challengelen:
	genhash = hashlib.md5(genlasthash + '|' + gentxns + '|' + str(gennonce)).digest()
	gennonce += 1

genblock = (0, 'Genesis', '<3 R4gul', gennonce, genhash)
chain.append(genblock)
print('Genesis Block', genblock)
# Chain is born.



# Fly Free!
while True: #Forever
#for i in range(1000):
	block = mine(chain[-1], 'Rn' + str(random.random())[2:])
	chain.append(block)
	print(block)

#print(chain)
