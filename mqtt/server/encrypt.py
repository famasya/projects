import nacl.secret
import nacl.utils
import sys
import pickle
import json

def main():
	key = 'W\x15g\xd6X\xfc\x19\x9e}F\xb7\xaa\xcf\xcf\xd8\x06\xdf\xc3\xa1\x9a\x7f\xa0,\xb9\x1e\x0cE\xc2=)\x85\x8a'
	box = nacl.secret.SecretBox(key)
	nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
	encrypted = box.encrypt("{\"message\":\"kill\",\"uuid\":\"jlk321n-32jks9-3iosapq\"}", nonce)
	val = []
	for i in encrypted:
		o = ord(i)
		val.append(o)
	print json.dumps(val)
	# s = ''
	# for i in val:
	# 	s += chr(i)
	# print box.decrypt(s)

if __name__ == '__main__':
	main()
