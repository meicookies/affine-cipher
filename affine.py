import string

class cipher:
    def __init__(self, text, slope, intercept):
        self.alphabet = string.ascii_lowercase
        self.slope = slope
        self.intercept = intercept
        self.text = text.lower()
    def process(self, tujuan):
        result = str()
        for char in self.text:
            if char.isalpha():
                index = self.alphabet.index(char)
                if tujuan == "encrypt":
                    e = ((self.slope * index) + self.intercept) % 26
                    result += chr(e + 97)
                elif tujuan == "decrypt":
                    count = int()
                    while True:
                        if (self.slope * count) % 26 == 1: break
                        count += 1
                    d = (count * (index - self.intercept)) % 26
                    result += chr((d + 97))
            else:
                result += char
        return result
# coded by ./meicookies
