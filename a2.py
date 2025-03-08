class Flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+' ('+self.meaning+')'

flash = []
print('welcome to flashcard app')

while(True):
    word = input('enter the word you want to add to the flash card: ')
    meaning = input('enter the meaning of the word: ')

    flash.append(Flashcard(word, meaning))
    option= int(input('enter 0, if u want to add another card, otherwise enter 1: '))

    if (option):
        break

print('\n Your FlashCards: ')
for i in flash:
    print('>',i)