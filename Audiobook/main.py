#pip install pyttsx3 | python to text speech version 3
#pip install PyPDF2 | python to pdf version 2
import pyttsx3
import PyPDF2
book=open('PYTHON_BASICS.pdf','rb') 		#Opening the pdf from open().....just replace the pdf name and put your pdf name
pdfReader=PyPDF2.PdfFileReader(book)		#pdfReader to read from pdf
pages=pdfReader.numPages					#finding the total no of pages 
print(pages)
speaker= pyttsx3.init()						#initialization of speaker
for num in range(1,pages):					# loop to go from initial page to final page
	page=pdfReader.getPage(1)
	text=page.extractText()
	speaker.say(text)
	print("The current Page Number is",num)
	#speaker.say('Python text to speech, One piece is out there! Go and Grab it. #Journey')
	speaker.runAndWait()