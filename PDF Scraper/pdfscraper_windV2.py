# Developers: Andrew Leon, Leyton Hue
# 10/09/2022
# Version 1.0
# Purpose: Read PDF file and Parse text from the
# document in order to manipulate contents for further
# processing

import PyPDF2 # imports prebuilt PDF scraping module

# opens file and assigns it to variable, then sends to PyPDF
# for processing
pdfFile = open('test_file.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFile)

# read num of pages
pdfPages = pdfReader.numPages
month = ('January','February','March','April','May','June','July',
         'August','Septemeber','October', 'November', 'December')

attendantPosistions = ('Entrance Attendant',
             'Security Attendant',
             'Auditorium Attendant',
             'Video Conference Attendant')
avPositions = ('Audio Operator' ,'Video Operator', 'Stage', 'Microphones')
attendantNames = []
dateRange = []

# loop to go through each page, in this case only 1
lineCount = 0 
for i in range(pdfPages):
    pageObj = pdfReader.getPage(i)
    
    # the actual text in each line
    text = pageObj.extractText().split("\n")
    
    #second loop to print each line separately
    for line in text:
        lineCount +=1
        print(line, 'Line#', lineCount)   
        # searches for month in line and omits rest
        for i in month:
            if i in line:
                print('-------------------------------')
                dateRange.append(line.strip())
            else: 
                continue
        if lineCount == 6:
            names = line.split('  ')
            names.remove('')
        else:
            continue
           
        #print(line.rstrip() + '**')
    #print(dateRange, '\n')

print('\n-------------------------------------------------------\n', 
      'Get names from 1st week and all week ranges from data ',
      '\n-------------------------------------------------------',)
index2 = 0
for i in names:
    print(names[index2])
    index2 += 1

index = 0
for i in dateRange:
    print('\nWeek of', dateRange[index])   
    index += 1
    
print("\nThere are:" ,lineCount, "lines in this file.")

# gotta close the file to avoid data corruption    
pdfFile.close()


# :) Mess around with it and let me know what you did
#    We need to recruit more People for this project!