from collections import Counter, deque

options = {"key" : lambda e: e[1], "reverse" : True}
lenkey = {"key" : lambda e: len(e)}

def encode(freq, string):
    dic = coding(freq[:])
    return ''.join([dic[c] for c in string])

def decode(freq, string):
    decode_dict = coding(freq[:])
    decode_dict = {y: x for x, y in decode_dict.items()}
    s, dec_str = deque(string), ''
    while len(s) > 0:
        part = s.popleft()
        while part not in decode_dict:
            part += s.popleft()
        dec_str += decode_dict[part]
    return dec_str

def frequencies(s):
    return list(Counter(s).items())

def coding(tree):
    while len(tree) > 1:
        tree.sort(**options)
        last, secondlast = tree.pop(), tree.pop()
        subtree = (sorted([last[0], secondlast[0]], **lenkey), last[1] + secondlast[1])
        tree.append(subtree)
    return dict(_coding(tree[0][0]))

def _coding(tree, prefix='')):
    if len(tree) == 1:
        return [(tree[0], prefix)]
    else:
        return _coding(tree[0], prefix + '0') + _coding(tree[1], prefix + '1')


string = 'Hallooooo'
dct = frequencies(string)
encoded = encode(dct, string)
print(dct)
print(encoded)
print(decode(dct, encoded))
