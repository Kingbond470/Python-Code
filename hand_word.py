'''
hand: initalization of a hand
n: integer, the hand of size
new hand: deal with new hand....and sets the hand attribute to the new hand
dummy hand: allows you to set a dummy hand and useful for testings implementation
handstring: a string of letters in hand and length of this string must be equal to self.hand_size,this method converts sets the hand attribute to a dictionary and display a string representation of the hand
it does not assume that self.hand has all the letters in word 
updates the hand: if self.hand does have all the letters to make the word and modifies self.hand by using up the letters in the given word
returns true if the word was able to be made with letters in the hand ; false otherwise
word: string
returns: booleam (if word made or not)
''' 
import random
class Hand(object):
    def __init__(self, n):
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
       

    def dealNewHand(self):
        self.hand = {}
        numVowels = self.HAND_SIZE / 3
        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1

        for i in range(numVowels, self.HAND_SIZE):
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1
    
    def setDummyHand(self, handString):
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1

    def calculateLen(self):
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans

    def __str__(self):
        output = ''
        for letter in sorted(self.hand.keys()):
            output += letter * self.hand[letter]
        return output

    def update(self, word):
        made_word = True
        hand_copy = self.hand.copy()

        for char in word:
            if hand_copy.get(char, 0) != 0:
                hand_copy[char] -= 1
            else:
                made_word = False
                break

        if made_word:
            self.hand = hand_copy

        return made_word
n=int(input('enter the size of the word: '))
myHand = Hand(n)
dummy_word=input('enter the dummy word: ')
myHand.setDummyHand(dummy_word)
update_word=input('enter the updated some words: ')  
print(myHand.update(update_word))
print(myHand)