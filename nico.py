#!usr/bin/python

def nico(key, message):
	l = len(key)
	s = sorted(key)
	numkey = [s.index(x) + 1 for x in key]
	padding = " " * (l - (len(message) % l))
	message += padding
	r = {x:message[i::l] for i, x in enumerate(numkey)}
	a = "".join([r[x + 1] for x in range(l)])
	cipher = [a[i::len(message) // l] for i in range(l)]
	return "".join(cipher) 
