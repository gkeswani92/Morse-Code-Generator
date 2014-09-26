from util import modifyMorseToBinary
from util import processMorse

morseToEngDict = {}

def loadMorseToEnglish():
    '''This functions opens the file that contains the English to Morse code
    conversions. It then proceeds to convert the dots into 0's and dashes into
    1's before storing the English to Morse conversion as a dictionary'''
    
    file = open (r"C:\Users\Gaurav Keswani\Documents\Eclipse\Morse-Code-Generator\src\resources\English to Morse Code.txt","r")
    lines= file.readlines()
    
    global morseToEngDict
    
    #Reading each line and adding it to the dictionary
    for line in lines:
        #Split the line into the alphabet and the morse code
        item = line.split() 
        #Alphabet chosen as the value
        value = item[0] 
        #Morse Code modified into 0/1 and chosen as the key
        key = modifyMorseToBinary(item[1]) 
        #Key and Value added to the dictionary
        morseToEngDict[key] = value 
    

def MorseToEnglish(morseSentence):
    '''This function takes the morse code as the input, converts it into binary form for processing
    and converts into the corresponding english sentence. 
    
    There is a space left between each alphabet in the morse code while each word has a gap of 3 spaces'''
    
    #Loading the current configuration of the morse code into the dictionary
    loadMorseToEnglish()
    
    #Converting morse code to 0's and 1's
    morseSentence = processMorse(morseSentence)
    
    englishSentence = ""
    
    #Splitting the morse code into different words
    for item in morseSentence.split("   "):
        #Splitting the morse code word in alphabets
        for code in item.split(" "):
            if code in morseToEngDict:
                englishSentence += morseToEngDict[code]
            else:
                return "Invalid Morse Code"
        englishSentence += " "
    
    #Removing the extra spaces on the right side
    englishSentence = englishSentence.rstrip()
    return englishSentence


def main():
    '''This function is the main function of the module and acts as the controller for the 
    whole application.
    
    It is the function which is called when this script is the main module. Otherwise, the Morse
    To English function is directly called'''
    
    sentence = input("Please enter the word to be converted to English--> ")
    
    #Calling function to convert user input into morse code
    english = MorseToEnglish(sentence)
    print ("English for '{0}' is '{1}'".format(sentence, english))


if __name__ == "__main__" : main()

#Please enter the word to be sent as morse code--> My name is Priyanka
#Morse code for 'My name is Priyanka' is '11 1011    10 01 11 0    00 000    0110 010 00 1011 01 10 101 01'