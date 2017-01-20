#Sean Hoyt 
#
#Basic RC4 Implementation in Python, opens kings james bible and encrypts

import datetime

#key scheduling for RC4
#mixes bits from key in empty 256 byte "array"
def KSA(key):
    S = [0] * 256   
    j = 0
    i = 0
    for i in range(0, 256):
        S[i] = i
    
    for i in range(0, 256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        #  swap 
        swap(S, i, j)
    return S
#takes output from the KSA and then swaps input depending on value 
def PRGA(S):
    i = 0
    j = 0
    K = [] #blank key to fill in
    #pseudo randomizes the key    
    for c in S:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        swap(S,i, j)
        K.append(chr(S[(S[i] + S[j]) % 256]))
    return K
#simple swap function, but really necessary but wanted that algorithmic feel
def swap(S, i, j):
    temp = S[i]
    S[i] = S[j]
    S[j] = temp
#simple function to call to encrypt a given string of any length
def RC4_encrypt(message, key):
    i = 0
    C = []
    S = KSA(key)
    K = PRGA(S)
   # print "Encrypting message...\n%s\nkey: %s" % ( message, key)
    #Applies pseudo random key to each letter in message
    for m in message:
        for c in m:
            C.append(chr(ord(c) ^ ord(K[i])))
            i = (i + 1) % 256
    #print "Ciphertext is: %s" % (''.join(C))
    return ''.join(C)
#simple decryption function, exactly same as encrypting, but oh well
def RC4_decrypt(ciphertext, key):
    i = 0
    M = []
    S = KSA(key)
    K = PRGA(S)
 #   print "Decrypting ciphertext...\n%s\nkey: %s" % (''.join(ciphertext), key)
    #Applies pseudo random key to each letter in ciphertext
    for m in ciphertext:
        for c in m:
            M.append(chr(ord(c) ^ ord(K[i])))
            i =(i + 1) % 256
    ##print "Message is: %s" % (''.join(M))      
    return ''.join(M)    
    

input_file = open("kjv.txt", 'r')
encrypted_file = open("encrypted_kjv.txt", 'w')
decrypted_file = open("decrypted_kjv.txt", 'w')
key = "aoetuhaoehuantoeh231h23"
start_time = datetime.datetime.now()
c = RC4_encrypt(input_file, key)
time_to_encrypt = ((start_time - datetime.datetime.now()).microseconds) / 1e6


encrypted_file.write(c)
encrypted_file.close()
m = RC4_decrypt(c, key)
decrypted_file.write(m)
decrypted_file.close()
print "Time to encrypt %r seconds" % (str(time_to_encrypt))


