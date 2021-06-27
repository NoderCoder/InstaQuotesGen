#reading the quote file
quoteFile = open('/Users/Mantra/InstaQuotesGenerator/QuoteFile/sampleQuotesFile.txt')
line = quoteFile.read().replace("\n", "*")
quoteList = []
tempSingleQuoteList =[]
singleQuoteList = []
print("Print start")
#split the text at the *
quoteList = line.split('*')
# perform removal of blanks form quote list
while("" in quoteList) :
    quoteList.remove("")
#making the list of all the qutes
for quote in quoteList:
        tempSingleQuoteList = quote.split(';')
        singleQuoteList.append(tempSingleQuoteList)
print(singleQuoteList[1][0])
print(len(singleQuoteList))
quoteFile.close
print("scrap  working for now")