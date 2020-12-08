import pyttsx3 
import PyPDF2 
file_name = input("Enter book name with path and suitable extension)
book = open(file_name, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()
n = int(input("Enter page no. to start with"))
for num in range(n, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
