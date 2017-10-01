#!usr/bin/python
#stream generator
def PRGA(S,text):
	i = 0
    	j = 0
	k=[]
	for x in range(256):
		i = (i + 1) % 256
		j = (j + S[i]) % 256
		S[i], S[j] = S[j], S[i]  # swap
		K = S[(S[i] + S[j]) % 256]
    	for x in range(len(text)):
		i = (i + 1) % 256
		j = (j + S[i]) % 256
		S[i], S[j] = S[j], S[i]  # swap
		K = S[(S[i] + S[j]) % 256]
		k.append(K)
	return k
