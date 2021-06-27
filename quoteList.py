#this is gonna grate a list of quotes singleQuoteList = [[quote,author,genre],[],[],]

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
quoteFile.close

