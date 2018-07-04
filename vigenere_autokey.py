class VigenereAutokeyCipher:
    def __init__(self, key, abc):
        self.key = key
        self.abc = abc

    def __create_key(self, text):
        return (self.key + "".join([x for x in text if x in self.abc]))[:len(text)]

    def encode(self, text):
        key = self.__create_key(text)
        key = [self.abc.find(x) for x in key]
        cipher = ""
        for c in text:
            if c in self.abc:
                ck = key.pop(0)
                cipher += (2 * self.abc)[ck:ck + len(self.abc)][self.abc.find(c)]
            else:
                cipher += c
        return cipher

    def decode(self, text):
        key = [self.abc.find(x) for x in self.key]
        msg = ""
        for c in text:
            if c in self.abc:
                ck = key.pop(0)
                decrypted_letter = self.abc[(2 * self.abc)[ck:ck + len(self.abc)].find(c)]
                key.append(self.abc.find(decrypted_letter))
            else:
                decrypted_letter = c
            msg += decrypted_letter
        return msg
