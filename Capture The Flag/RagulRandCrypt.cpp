/* Ragul's Random Number Stream Cipher (C) 2018
 * This is cool but never roll ur own crypto kids...
 *
 * Usage Examples:
 * ---------------
 * Compile g++ RagulRandCrypt.cpp -o ragulrandcrypt
 * Encrypt: ./ragulrandcrypt key + < pla > enc
 * Decrypt: ./ragulrandcrypt key - < enc > pla 
 */

#include <stdio.h>
#include <iostream>

//#define ENT 32767 // Normal
//#define ENT 2147483648 // EXTRA UNICODE SECURE
unsigned long long ENT = 32767; //Dynamic Mode

using namespace std;

// http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf
// ISO/IEC 9899:TC3 Committee Draft — Septermber 7, 2007 WG14/N1256
// The following functions define a CUSTOMISED portable implementation of rand and srand
static unsigned long long nextnum = 1;

void pSRAND(unsigned long long seed){
	nextnum = seed;
}

int pRAND(void){ // RAND_MAX assumed to be 32767 in std implementation
	nextnum = nextnum * 1103515245 + 12345;
	return (unsigned int)(nextnum/65536) % ENT;
}

// Main Cipher
int main(int argc, char* argv[]){
	string key;
	char mode;

	if(argc < 3) return 0; // Safe Death

	key = argv[1];

	unsigned long long seed = 3133731337;
	unsigned long long modu = 999999999999999999;

	for(unsigned int i = 0; i < key.length(); i++){
		if(ENT == 32767 && i >= key.length()/2) ENT = seed % 2147483648;
		seed = (seed + i) * int(key[i]);
		seed = seed % modu;
		//cout << seed << " " << ENT << "\n";
	}

	pSRAND(seed);
	mode = *argv[2];
	if(mode == '+'){
		char c;
		unsigned int num;
		while (cin.get(c)) {
			num = c ^ pRAND();
			printf("%x ", num);
		}
	}else if(mode == '-'){
		unsigned int num;
		while (scanf("%x ", &num) != EOF) {
			num = num ^ pRAND();
			cout << char(num);
		}
	}
}
