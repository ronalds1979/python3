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

print ('### Functions as variables ###')

text = '''
this text is the test text to tested. Is it a valid text?

'''
print ('Original text!')
print (text)
Toolbox.addSingleLineSeparator

def lowercase(text):
    return text.lower()

def removePunctuation(text):
    punctuations = ['.','-', ',','*','?']
    for punctuation in punctuations:
        text = text.replace(punctuation, '')
    return text

def removeNewLines(text):
    text=text.replace('\n', ' ')
    return text

def removeShortWords(text):
    return ' '.join([word for word in text.split() if len(word)>3])

def removeLongWords(text):
    return ' '.join([word for word in text.split() if len(word)<4])

processingFunction = [lowercase,removePunctuation]

for func in processingFunction:
    text = func(text)
print(text)
Toolbox.addSingleLineSeparator()

Toolbox.addTripleLineSeparator()

print ('### Lambda function ###')
print ("(lambda x: x + 3)(5)")
print ((lambda x: x + 3)(5)) # lambda function has implicit return. This case sum 3 to the variable x, the call is the same line using x=5. No multline function with lambda functions

Toolbox.addSingleLineSeparator

myList = [5,4,3,2]
print (sorted(myList))

Toolbox.addSingleLineSeparator

myList = [{'num' : 5},{'num' : 4},{'num' : 3},{'num' : 2}]
print (myList)
#print (animals['a'])
print(myList, key=['num']) 
print(sorted(myList, key=lambda x: x['num'])) # lambda function allow to sort the function
