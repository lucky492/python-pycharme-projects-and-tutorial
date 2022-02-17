import pyttsx3
import PyPDF2

book = open('w.pdf','rb')

filereader = PyPDF2.PdfFileReader(book)
print(filereader.numPages)

from_page = filereader.getPage(12)

text = from_page.extractText()
speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()
























