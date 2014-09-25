from util import modifyMorseToBinary
from util import createSoundFile
 
engToMorseDict = {} 
sentence = ""

def loadEnglishToMorse():
    '''This functions opens the file that contains the English to Morse code
    conversions. It then proceeds to convert the dots into 0's and dashes into
    1's before storing the English to Morse conversion as a dictionary'''
    
    file = open (r"C:\Users\Gaurav Keswani\Documents\Eclipse\Morse-Code-Generator\src\resources\English to Morse Code.txt","r")
    lines= file.readlines()
    
    global engToMorseList
    
    #Reading each line and adding it to the dictionary
    for line in lines:
        item = line.split() #Split the line into the alphabet and the morse code
        key = item[0] #Alphabet chosen as the key
        value = modifyMorseToBinary(item[1]) #Morse Code modified into 0/1 and chosen as the value
        engToMorseDict[key] = value #Key and Value added to the dictionary
        
def englishToMorse(englishSentence):
    '''This function takes the english word as the input and converts into the corresponding 
    morse code. There is a space left between each alphabet'''
    
    sentenceMorse = ""
    words = englishSentence.upper().split(" ")
    
    #Splitting the sentence into individual words
    for englishWord in words:
        wordMorse = ""
        
        #Splitting the word into individual characters
        for char in englishWord: 
            if char in engToMorseDict: #Attempts to find value only if key exists in the dictionary
                alphabetMorse = engToMorseDict[char]
                wordMorse += alphabetMorse + " "
        sentenceMorse += wordMorse + "  "
    
    sentenceMorse = sentenceMorse.rstrip() #Unnecessary four spaces at the end of the string
    
    return sentenceMorse

def main():
    '''This function is the main function of the module and acts as the controller for the 
    whole application'''
     
    #Loading the current configuration of the morse code into the dictionary
    loadEnglishToMorse()
    
    #Taking english input from user to convert to morse code
    global sentence
    sentence = input("Please enter the word to be sent as morse code--> ")
    
    #Calling function to convert user input into morse code
    morse_binary = englishToMorse(sentence)
    
    morse_text = ""
    for char in morse_binary:
        if char == "0":
            morse_text += "."
        elif char == "1":
            morse_text += "-"
        else:
            morse_text += char 
    
    print ("Morse code for '{0}' is '{1}'".format(sentence,morse_text))

    #Creating the sound file for the morse code
    createSoundFile(morse_binary)

if __name__ == "__main__" : main()
