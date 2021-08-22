import pyttsx3
import PyPDF2
#import file book
book = open('BS.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

# Initialization
bot = pyttsx3.init()
# setup voice
voices = bot.getProperty('voices')
bot.setProperty('voice', voices[0].id) # 1 : voice female # 0 : voice male
# get page book
for num in range(1, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    bot.say(text)
    bot.runAndWait()