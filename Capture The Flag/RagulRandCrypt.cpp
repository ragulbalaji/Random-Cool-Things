/* Ragul's Random Number Stream Cipher (C) 2018
 * This is cool but never roll ur own crypto kids...

 * Usage Examples:
 * ---------------
 * Compile g++ ragulrandcrypt.cpp -o ragulrandcrypt
 * Encrypt: ./ragulrandcrypt key + < pla > enc
 * Decrypt: ./ragulrandcrypt key - < enc > pla 
 */

#include <bits/stdc++.h>

using namespace std;

// http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf
// ISO/IEC 9899:TC3 Committee Draft — Septermber 7, 2007 WG14/N1256
// The following functions define a portable implementation of rand and srand
static unsigned long int next = 1;

void pSRAND(unsigned int seed){
	next = seed;
}

int pRAND(void){ // RAND_MAX assumed to be 32767 
	next = next * 1103515245 + 12345;
	return (unsigned int)(next/65536) % 32768; 
}

// Main Cipher
int main(int argc, char* argv[]){
	string key;
	char mode;
	
	key = argv[1];

	int seed = 42;
	int modu = 999999;

	for(int i = 0; i < key.length(); i++){
		seed = seed * int(key[i]);
		seed = seed % modu;
		//cout << seed << "\n";
	}
	pSRAND(seed);
	mode = *argv[2];
	if(mode == '+'){
		char c;
		int num;
		while (cin.get(c)) {
			num = c ^ (pRAND() % 64);
			printf("%x ", num);
		}
	}else if(mode == '-'){
		char c;
		int num;
		while (scanf("%x ", &num) != EOF) {
			num = num ^ (pRAND() % 64);
			cout << char(num);
		}
	}
}
