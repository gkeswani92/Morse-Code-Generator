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
        item = line.split() #Split the line into the alphabet and the morse code
        value = item[0] #Alphabet chosen as the value
        key = modifyMorseToBinary(item[1]) #Morse Code modified into 0/1 and chosen as the key
        morseToEngDict[key] = value #Key and Value added to the dictionary
    
    #printDictionary(morseToEngDict)

def MorseToEnglish(morseSentence):
    '''This function takes the morse code as the input and converts into the corresponding 
    english sentence. There is a space left between each alphabet in the morse code
    while each word has a gap of 3 spaces'''
    
    englishSentence = ""
    
    for item in morseSentence.split("   "):
        for code in item.split(" "):
            if code in morseToEngDict:
                englishSentence += morseToEngDict[code]
            else:
                return "Invalid Morse Code"
        englishSentence += " "
    
    englishSentence = englishSentence.rstrip()
    return englishSentence

def main():
    '''This function is the main function of the module and acts as the controller for the 
    whole application'''
     
    #Loading the current configuration of the morse code into the dictionary
    loadMorseToEnglish()
    
    #Taking english input from user to convert to morse code
    global sentence
    sentence = input("Please enter the morse code--> ")
    
    #Sample input for "Hello There" is ".... . .-.. .-.. ---   - .... . .-. ."
    #Sample input for "My name is Gaurav" is "-- -.--   -. .- -- .   .. ...   --. .- ..- .-. .- ...-"
    
    sentence = processMorse(sentence) #Converting morse code to 0's and 1's
    
    #Calling function to convert user input into morse code
    english = MorseToEnglish(sentence)
    print ("English for '{0}' is '{1}'".format(sentence, english))

if __name__ == "__main__" : main()

#Please enter the word to be sent as morse code--> My name is Priyanka
#Morse code for 'My name is Priyanka' is '11 1011    10 01 11 0    00 000    0110 010 00 1011 01 10 101 01'