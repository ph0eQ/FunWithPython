
#Caesar Cipher Cracker
#Takes bruteforce approach and solves every shift of cipher
#Sean Hoyt
def crack(message):
	alpha = "abcdefghijklmnopqrstuvwxyz"
	possible_soln = [];
	for i in range(0, len(alpha)):
		temp = []
		for m in message:
			temp.append(alpha[(ord(m) - ord('a') + i) % 26])
		possible_soln.append(temp)
	#print possible_soln
	for p in possible_soln:
		print "".join(p)
		print

#encrypt/decrypt function for caesar's cipher
def crypt(message, shift):
	alpha = "abcdefghijklmnopqrstuvwxyz"
	temp = []	
	for m in message:
		temp.append(alpha[(ord(m) - ord('a') + shift) % 26])
	#print temp
	
#message
#shifted 1
message = "sdscsxceppsmsoxddyzbydomdyebcovfocgsdrvkgcgoxoondyzbydomdyebcovfocgsdrwkdrowkdsmc"
#BYNBYHZFYXZLIGNBYMWYHYMJYYXCFS
message2 = "bynbyhzfyxzlignbymwyhymjyyxcfs"
#crypt(message, 6)
crack(message2)

#crack(message)
#crack_caesar(message, 26)
		 
	
	


