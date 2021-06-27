from os import PRIO_PGRP
import quoteList
from PIL import Image, ImageDraw, ImageFont

# Blank Image 
img = Image.new('RGB', (612, 612), color = (255, 255, 255))

# variables
totalQuotes = len(quoteList.singleQuoteList)
index = 0
genre = quoteList.singleQuoteList[index][2]

print(genre)


#loop code
for x in quoteList.singleQuoteList:
    if x[2] == genre:
        #Staging the quotes for the inputSentence
        sentence = quoteList.singleQuoteList[index][0] + "-" + quoteList.singleQuoteList[index][1]
        inputSentence = sentence

        #fonts
        fnt = ImageFont.truetype('/Users/Mantra/InstaQuotesGenerator/Fonts/Cinzel-VariableFont_wght.ttf', 70)
        # fnt = ImageFont.truetype('/Users/Mantra/InstaQuotesGenerator/Fonts/Benne-Regular.ttf', 70)

        #image background
        greenBackground = Image.open('/Users/Mantra/InstaQuotesGenerator/Background/Green.jpg')
        img = greenBackground
        #variables for image size
        imgWidth , imgHeight = img.size
        d = ImageDraw.Draw(img)


        #find the average size of the letter
        sum = 0
        for letter in inputSentence:
            sum += d.textsize(letter, font=fnt)[0]

        average_length_of_letter = sum/len(inputSentence)

        

        #find the number of letters to be put on each line
        number_of_letters_for_each_line = (imgWidth/1.618)/average_length_of_letter
        incrementer = 0
        fresh_sentence = ''

        #add some line breaks
        for letter in inputSentence:
            if(letter == '-'):
                fresh_sentence += '\n\n' + letter
            elif(incrementer < number_of_letters_for_each_line):
                fresh_sentence += letter
            else:
                if(letter == ' '):
                    fresh_sentence += '\n'
                    incrementer = 0
                else:
                    fresh_sentence += letter
            incrementer+=1
     
        #render the text in the center of the box
        dim = d.textsize(fresh_sentence, font=fnt)
        textWidth = dim[0]
        textHeight = dim[1]

        #Positions are refrenced from top left corner
        textWidthPos = (imgWidth/2 - textWidth/2)
        #adjusting so that text starts a little above the center
        textHeightPos = (imgHeight/2.7-textHeight/2) 
        #prevent inputSentence clipping
        if(textHeightPos < 30):
            textHeightPos = 30
        d.text((textWidthPos,textHeightPos), fresh_sentence ,align="center",  font=fnt, fill=(0,0,0,0))
        # Saving the file
        # img.save('/Users/Mantra/InstaQuotesGenerator/Output/age/Age'+ str(index)+'.png')


    else:
        break
    print(index)
    index = index + 1
#End of loop






