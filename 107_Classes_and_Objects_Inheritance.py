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

print ('### Inheritance ###')

Toolbox.addSingleLineSeparator()

class Dog:
    _legs = 4 # class attribute legs
    def __init__(self, name):
        self.name = name # instance attribute name
    
    def speak(self):
        print(self.name + ' says: Bark!')
        return 'ok'

    def getLegs(self):
        return self._legs

Toolbox.addSingleLineSeparator()

my_dog = Dog('Rex')
print ('The dog name is ' + my_dog.name)                                    # print instance attribute name
print ('The dog ' + my_dog.name + ' has ' + str(my_dog._legs) + ' legs')     # print instance attribute name and legs
print (my_dog.speak())                                                      # use method speak
print (Dog('Rex1').speak())

Toolbox.addTripleLineSeparator()

class Chihuahua (Dog):
    def speak(self): # this overwrite the parent class method
        print(f'{self.name} says: Yap yap yap!')
    def wagTails(self):
        print('Vigorous wagging!')

Toolbox.addSingleLineSeparator()

dog = Chihuahua('Roxy')
dog.speak()
dog.wagTails()

Toolbox.addTripleLineSeparator()

print ('Extending built-in classes')

Toolbox.addSingleLineSeparator()

print('list')

List = list()
List.append(1)
List.append(1)
List.append(2)
print(List)

Toolbox.addSingleLineSeparator()

print('Unique list')

myList = list()
class UniqueList(list):
    def append(self, item):
        if item in self:
            return
        super().append(item)

UniqueList = UniqueList()
UniqueList.append(1)
UniqueList.append(1)
UniqueList.append(2)
print(UniqueList)

Toolbox.addSingleLineSeparator()

Toolbox.addSingleLineSeparator()

print('Unique list extend attribute')

myList = list()
class UniqueList(list):
    def __init__(self):
        super().__init__() # keep attributes from the original class
        self.someProperty = 'Unique List!' # add a new attribute extending the original class

    def append(self, item):
        if item in self:
            return
        super().append(item)

UniqueList = UniqueList()
UniqueList.append(1)
UniqueList.append(1)
UniqueList.append(2)
print(UniqueList)

print(UniqueList.someProperty)

Toolbox.addSingleLineSeparator()

Toolbox.addTripleLineSeparator()

class RyansMom() : # parent class
    def __init__(self):
        self.height = 'tall'
        self.humor = 'ok'
        self.occupation = 'teacher'
        self.hair = 'blond'
    def buyCoffee (self, type) :
        return f'Ok, I bought {type} type'
    def makeCoffee(self, pot) :
        return self.buyCoffee(pot)


class Ryan(RyansMom) : # child class. The (RyanMom) in parenthesis says that Ryan class is extending RyanMom class
    def __init__(self):
        super().__init__()
        self.height = 'very tall'
        self.humor = 'dry'
        self.occupation = 'software engineer'
    def rinseCoffeePot(self, pot) :
        rinseCoffeePot = pot
    def measureWater(self, pot) :
        measureWater = pot
    def addGrounds(self, pot) :
        addGrounds = pot

    def pot(self):
        isBrewing = True

    def makeCoffee(self, pot) :
        self.rinseCoffeePot(pot)
        self.measureWater(pot)
        self.addGrounds(pot)
        #while pot.isBrewing() :
        #    self.readNews()
        #return pot.coffee
    def goToWork(self) :
        while self.isWorkTime() :
            if self.isMeetingTime() :
                self.goToMeeting()
            self.checkEmail()
            self.writeCode()
        self.goHome()
    def cleanStuff(self) :
        if not self.husbandSaysHeWillClean():
            self.grumble()
            self.doLaundry()
            self.doDishes()

Toolbox.addSingleLineSeparator()

mom = RyansMom()
Ryan = Ryan()

print (mom.height)
print (mom.humor)
print (mom.occupation)
print (mom.hair)
print (mom.makeCoffee('strong'))

Toolbox.addSingleLineSeparator()

print (Ryan.height)
print (Ryan.humor)
print (Ryan.occupation)
print (Ryan.hair)
print (Ryan.makeCoffee('strong'))

Toolbox.addSingleLineSeparator()


