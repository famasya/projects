import nacl.secret
import nacl.utils
import sys

key = 'W\x15g\xd6X\xfc\x19\x9e}F\xb7\xaa\xcf\xcf\xd8\x06\xdf\xc3\xa1\x9a\x7f\xa0,\xb9\x1e\x0cE\xc2=)\x85\x8a'
txt = [45,192,195,112,62,1,118,232,122,250,90,215,46,174,123,230,127,94,157,146,160,195,98,194,25,24,88,44,31,151,150,35,150,219,193,139,170,106,190,87,88,212]

box = nacl.secret.SecretBox(key)
s = ''
for i in txt:
	s += chr(i)

print box.decrypt(s)