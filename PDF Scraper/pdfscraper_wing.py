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

# loop to go through each page, in this case only 1
count = 0 
for i in range(pdfPages):
    pageObj = pdfReader.getPage(i)
    
    # the actual text in each line
    text = pageObj.extractText().split("\n")
    #second loop to print each line separately
    for line in text:
        count +=1
        if 'October' in line:
            print('-------------------------------')
        print(line.strip() + '**')        
        
        # searches for month in line and omits rest
        # to do: add dates to list 
        #if 'October' in line:
            #print('-------------------------------')
        #else: 
            #continue
        #print(line.rstrip() + '**')
    
        
print("There are:" ,count, "lines in this file.")

# gotta close the file to avoid data corruption    
pdfFile.close()


# :) Mess around with it and let me know what you did
#    We need to recruit more People for this project!