import re
from collections import defaultdict
from functools import reduce, cmp_to_key

def cmp(s1, s2):
	if len(s1) < len(s2):
		return -1
	elif len(s1) > len(s2):
		return 1
	else:
		if s1 > s2:
			return 1
		elif s1 < s2:
			return -1	
	return 0

def simplify(polynomial):
	f = re.compile(r"[+-]?\w+")
	n = re.compile(r"[+-]?\d+")
	terms = re.findall(f, polynomial.replace(" ", ""))
	print(f"Found terms: {terms}")
	multiplicity = defaultdict(int)
	for term in terms:
		base = "".join(sorted([c for c in term if c.isalpha()]))
		try:
			mult = reduce(lambda x,y: x*y, [int(x) for x in re.findall(n, term)])
		except TypeError:
			mult = 1 if "-" not in term else -1
		multiplicity[base] += mult
	print(multiplicity)
	res = ""
	for term in sorted(multiplicity.keys(), key=cmp_to_key(cmp)):
		m = multiplicity[term]
		if m == 0:
			continue
		if m == 1:
			r = "+"+term
		elif m == -1:
			r = "-"+term
		else:
			r = f"{+m}{term}"
		res += r
	return res[1:] if res[0] == "+" else res
	

if __name__ == "__main__":
	a = "2yx - xy"
