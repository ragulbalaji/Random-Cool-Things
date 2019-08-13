import math

vars = {}
plain = ""
cipher = ""

def makeKeys():
        vars['p'] = int(input("Prime P? "))
        vars['q'] = int(input("Prime Q? "))
        vars['n'] = vars['p'] * vars['q']
        vars['z'] = (vars['p'] - 1)*(vars['p'] - 1)
        for k in range(2,int(math.floor(math.sqrt(vars['z'])))):
                if vars['z'] % k != 0:
                        vars['k'] = k
                        break;
        print("NEED YOU TO SOLVE ( "+str(vars['k'])+" * j ) % "+str(vars['z'])+" = 1")
        vars['j'] = int(input("integer J? "))
        print("p,q,n,z,k,j =", vars['p'], vars['q'], vars['n'], vars['z'], vars['k'], vars['j'])
        print("Public Key: N = ", vars['n'], " K = ", vars['k']);

def encrypt():
        plain = str(raw_input("Msg: "))
        print(plain)
        cipher = [(ord(char) ** vars['k']) % vars['n'] for char in plain]
        print("CIPHER: ", cipher)

def decrypt():
        cipher = input("Cipher: ")
        print(cipher)
        plain = [chr((char ** vars['j']) % vars['n']) for char in cipher]
        print("PLAIN: ", plain)

funcs = {0:makeKeys, 1:encrypt, 2:decrypt}

def main():
        while True:
                print("\nSimpleRSA (C) Ragul Balaji 2017\n\n[0] Make Keys\n[1] Encrypt\n[2] Decrypt")
                option = int(input("> "))
                funcs[option]()

main()
