from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import binascii
import random
import math
import sys
import random
import string

def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength)) 

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, int(math.sqrt(x))):
        if x % n ==0:
            return False
    return True

def randprime():
  prime1= [i for i in range(500,1000) if is_prime(i)]
  n = random.choice(prime1)
  return n

def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b) 

def encrypt(plain_text, iv, key):
    obj = AES.new(key, AES.MODE_CFB, iv)

    enc_text = obj.encrypt(plain_text)
    return enc_text

def decrypt(enc_text, iv, key):
    obj = AES.new(key, AES.MODE_CFB, iv)

    plain_text = obj.decrypt(enc_text)
    return plain_text


print('Hello there, Please wait while we set up encryption for you', '\n')


print('SENDER SIDE: ', '\n')
print('Beginning to set up RSA')

print('Generating two primes p & q for RSA encryption')

p = randprime()
q = randprime()
while(p == q):
    q = randprime()

print('Generated primes are: p = ', p, ' and q = ', q,)

#RSA code for generation of e & d (encryption & decryption pair)
n = p*q
l = (p-1) * (q-1)

for e in range(2,l): 
    if gcd(e,l)== 1: 
        break

for i in range(1,100): 
    x = 1 + i*l 
    if x % e == 0: 
        d = int(x/e) 
        break

print('Generated the encryptor e:', e, ' and the decryptor d:', d, '\n')
print('Sending the encryptor key to the receiver and requesting for AES key for further communications', '\n')

print('RECEIVER SIDE:')
print('Received public encryption key: ', e, 'and modulo number n: ', n)


#Empty strings for storing 128-bit binary AES keys
AESkey=randomString(16)          #original AES key
encrypt_RSA=[]                      #Empty list to store ascii values of encrypted AES string
decrypt_RSA=[]                      #Empty list to store ascii values of decrypted AES string
AES_key = [ord(c) for c in AESkey]  #Converting the string to a list of characters
#RSA function for Encryption
for i in range(16):
    encrypt_RSA.append(1)
    for j in range(e):
        encrypt_RSA[i] = encrypt_RSA[i]*AES_key[i]
        encrypt_RSA[i]  = encrypt_RSA[i]%n      #(key^e)mod_n

print('Delivering the Encrypted AES key to sender', '\n')

print('SENDER SIDE: ', '\n')
print('Received encrypted AES key')

#RSA function for Decryption
for i in range(16):
    decrypt_RSA.append(1)
    for j in range(d):
        decrypt_RSA[i] = decrypt_RSA[i]*encrypt_RSA[i]
        decrypt_RSA[i]  = decrypt_RSA[i]%n      #(encrypted_key^d)mod_n

AESkey_decrypted=''.join(chr(i) for i in decrypt_RSA)   #Reconverting the Ascii value list back to original string

print('Ready to begin secure transmission, AES setup completed')
print('AES key is: ', AESkey_decrypted)

iv = "TestMeInitVector"

# print('Converting your audio to hex')
filename = './Input/input.mp4'
with open(filename, 'rb') as f:
    content = f.read()
hexa = binascii.hexlify(content) 
file=open("./Output/converted.txt", "wb")
file.write(hexa)
file.close()

print("Encrypting your audio using AES")

file1=open("./Output/encrypted.txt", "wb")
encdata = encrypt(hexa, iv, AESkey_decrypted)
file1.write(encdata)

print("Data received on other side, beginning decryption")
file2=open("./Output/decrypted.txt", "wb")
file2.write(decrypt(encdata, iv,AESkey_decrypted))

print("Converting .txt back to audio file")
filename2 = './Output/decrypted.txt'
with open(filename2, 'rb') as f:
    content = f.read()

file=open("./Output/decrypted.mp4", "wb")
file.write(binascii.unhexlify(content))
file.close()