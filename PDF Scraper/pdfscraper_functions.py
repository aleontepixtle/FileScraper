# Developers: Andrew Leon, Leyton Hue
# 10/09/2022
# Version 1.0
# Purpose: Read PDF file and Parse text from the
# document in order to manipulate contents for further
# processing

import PyPDF2 # imports prebuilt PDF scraping module

# ################################################## #
# Global Lists that hold positions, and months       #
# Please do NOT modify these values, vital for loops # 
# ################################################## #
ATTD_POSITIONS = ['Entrance Attendant',
             'Security Attendant',
             'Auditorium Attendant',
             'Video Conference Attendant']

AV_POSITIONS = ['Audio Operator' ,'Video Operator', 'Stage', 'Microphones']

MONTH = ('January','February','March','April','May','June','July',
         'August','Septemeber','October', 'November', 'December')

# opens pdf file
def getFile():
    fileName = 'test_file' # change file name here w/out pdf extension
    pdfFile = open(fileName + '.pdf', 'rb') 
    return pdfFile

# reads pdf file
def readFile(pdfFile):
    readFile = PyPDF2.PdfFileReader(pdfFile)
    return readFile

# closes pdf file
def closeFile(pdfFile):
    pdfFile.close()

# gets page count
def getPageCount(readFile):
    pdfPages = readFile.numPages
    return pdfPages

# extracts all pdf text
def getText(pdfPages, readFile):
    for i in range(pdfPages):
        pageObj = readFile.getPage(i)
        # the actual text in each line
        text = pageObj.extractText().split('\n\n')
    return text

# reads each line
def getEachLine(text):
    lineCount = 0
    scrubbedText = []
    dateRange = []
    for i in text:
        if i.isspace():
            text.remove(i)
        elif i.strip() =='Attendant':
            text.remove(i)
        elif i in MONTH:
            dateRange.append(i)
            print(dateRange)
        else:
            lineCount += 1
            scrubbedText.append(i.strip())
            print('---', lineCount, i)
            
    return scrubbedText
    

def main():
    file = getFile()
    activePdfFile = readFile(file)
    pdfPages = getPageCount(activePdfFile)
    extractedText = getText(pdfPages, activePdfFile)
    line = getEachLine(extractedText)
    closeFile(file)
    
main()

# need to find a way to add Attendant to Line 2
# need t0 add 2nd Mic person on previous line starting on line 4