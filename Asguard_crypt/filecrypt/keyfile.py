import random, os, string,hashlib

def make_key():

	password= ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))
	key = hashlib.sha256(password).digest()
	return key
	

