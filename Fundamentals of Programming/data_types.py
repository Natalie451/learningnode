import datetime


name = 'John'
age = 100
money = 1.01
is_male = True
dobt = datetime.datetime(2000, 12, 12, 6, 30, 13)
toys = ['computer', 'chocolate', 'dog']
teachers = {
    'maths': 'John',
    'english': 'Ana',
    'history': 'George',
}
class Pet:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Pet: ' + self.name

    def __repr__(self):
        return self.__str__()

chloe = Pet('Chloe')

print('The variable name is of type', type(name), 'and has the value', name)
print('The variable age is of type', type(age), 'and has the value', age)
print('The variable money is of type', type(money), 'and has the value', money)
print('The variable is_male is of type', type(is_male), 'and has the value', is_male)
print('The variable dobt is of type', type(dobt), 'and has the value', dobt)
print('The variable toys is of type', type(toys), 'and has the value', toys)
print('The variable teachers is of type', type(teachers), 'and has the value', teachers)
print('The variable chloe is of type', type(chloe), 'and has the value', chloe)