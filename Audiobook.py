import pyttsx3 
import PyPDF2 
file_name = input("Enter book name with path and suitable extension : ")
book = open(file_name, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()
n = int(input("Enter page no. to start with : "))
choice = 'N'
while(choice=='N'):
    print("Current rate of speaking = ",str(speaker.getProperty('rate')))
    speaker.setProperty('rate', int(input("Enter a rate or enter 150 ")))
    speaker.say("Hii .... Is this speed suitable to you ? Y/N")
    speaker.runAndWait()
    speaker.stop()
    choice = input()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[int(input("Enter 0 for male and  1 for female voice : "))].id)
print("Enjoy :)")
for num in range(n, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
