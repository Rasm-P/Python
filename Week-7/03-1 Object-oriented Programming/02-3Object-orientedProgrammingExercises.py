import string

class TextContainer:
    def __init__(self, text):
        self.text = text
    
    def words(self):
        res = len(self.text.split()) 
        return res

    def chars(self):
        count = len(self.text)
        return count

    def letters(self):
        count = 0
        for letter in self.text:
            if letter in string.ascii_letters:
                count += 1
        return count

