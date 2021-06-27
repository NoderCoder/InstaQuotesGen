import os
parentDir = '/Users/Mantra/InstaQuotesGenerator/Output/'

#reading the quote file
quoteFile = open('/Users/Mantra/InstaQuotesGenerator/QuoteFile/QuotesFile.txt')
line = quoteFile.read().replace("\n", "***")
quoteList = []
tempSingleQuoteList =[]
singleQuoteList = []
print("Print start")
#split the text at the *
quoteList = line.split('***')
# perform removal of blanks form quote list
while("" in quoteList) :
    quoteList.remove("")
#making the list of all the qutes
for quote in quoteList:
        tempSingleQuoteList = quote.split(';')
        singleQuoteList.append(tempSingleQuoteList)

index = 0
genre = ""
genre = singleQuoteList[0][2]
for q in singleQuoteList:
    if (genre == singleQuoteList[index][2]):
        if(index==len(singleQuoteList)-1):
            break
        else:
            if(genre != singleQuoteList[index+1][2]):
                print(genre)
                path = os.path.join(parentDir, genre)
                os.mkdir(path)
    else:
        genre = singleQuoteList[index+1][2]
    index = index+1







print(genre)
print(len(singleQuoteList))
quoteFile.close
print("scrap  working for now")