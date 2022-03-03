#Exercise 11

class sentence(object):
    
    def __init__(self, sent):
        self.sentence = sent
    
    def get_first_word(self):
        return self.sentence.split()[0]
    
    def get_all_words(self):
        return self.sentence
    
    def replace(self, index,new_word):
        words = self.sentence.split()
        words[index] = new_word
        return " ".join(words)
    
    
    
one = sentence("I'm going back")


print(one.get_first_word())
print(one.get_all_words())
print(one.replace(2, "home"))
    
    
        