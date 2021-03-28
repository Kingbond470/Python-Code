import pyttsx3
print("Enter your name")
name=input()
print("Enter the location of your country")
location=input()
def onStart():
   print('starting')
  
def onWord(name, location, length):
   print('Your Word', name, location, length)
  
def onEnd(name, completed):
   print('The End', name, completed)
  
engine = pyttsx3.init()
  
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
  
sen = 'My name is Mausam Singh and I am a computer science student from University of Mumbai'
  
engine.say(sen)
engine.runAndWait()