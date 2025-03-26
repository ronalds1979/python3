# Class to help to organize the output and document the code
class Toolbox:
    def addTripleLineSeparator():
        sep = ('__ . _ . __       ')
        print('')
        print (sep)
        print('')

    def addSingleLineSeparator():
        print('')


Toolbox.addTripleLineSeparator()

print ('### Static and instance methods ###')

Toolbox.addSingleLineSeparator()

class WordSet:
    replacePuncs = ['!','.',',','\'']
    def __init__(self):
        self.words = set()
    
    def addText(self, text): #instance method that belongs to a particular instance of the class
        #print(text)
        text = WordSet.cleanText(text)
        #print (text)
        for word in text.split():
            self.words.add(word)
    
    def cleanText(text): # static method they are not changing per instance. Like business logic
        #chaining function
        text = text.replace('!', '').replace('.','').replace(',','').replace('\'','')
        return text.lower()

wordSet = WordSet()

wordSet.addText('Hi, I\'m Ryan! Here is a setence I want to add!')
#wordSet.addText('Here is another sentence I want to add.')

print(wordSet.words)

Toolbox.addSingleLineSeparator()

class WordSet1:
    replacePuncs = ['!','.',',','\'']
    def __init__(self):
        self.words = set()
    
    def addText(self, text): #instance method that belongs to a particular instance of the class
        #print(text)
        text = WordSet1.cleanText(text)
        #print (text)
        for word in text.split():
            self.words.add(word)
    
    def cleanText(text): # static method they are not changing per instance. Like business logic
        #chaining function
        for punc in WordSet1.replacePuncs:
            text = text.replace(punc, '')
        return text.lower()

wordSet = WordSet1()

wordSet.addText('Hi, I\'m Ryan! Here is a setence I want to add!')
#wordSet.addText('Here is another sentence I want to add.')

print(wordSet.words)

Toolbox.addSingleLineSeparator()

print ('### Decorators ###')

Toolbox.addSingleLineSeparator()

class WordSet1:
    replacePuncs = ['!','.',',','\'']
    def __init__(self):
        self.words = set()
    
    def addText(self, text): #instance method that belongs to a particular instance of the class
        #print(text)
        text = self.cleanText(text)
        #print (text)
        for word in text.split():
            self.words.add(word)
    
    @staticmethod # static method decorator. It tells Python how to interpret the method. As static method instead of instance method.

    def cleanText(text): # static method they are not changing per instance. Like business logic
        #chaining function
        for punc in WordSet1.replacePuncs:
            text = text.replace(punc, '')
        return text.lower()

wordSet = WordSet1()

wordSet.addText('Hi, I\'m Ryan! Here is a setence I want to add!')
#wordSet.addText('Here is another sentence I want to add.')

print(wordSet.words)
