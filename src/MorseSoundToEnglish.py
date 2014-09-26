import wave
import struct
from MorseToEnglish import MorseToEnglish

morse, dot, dash = [], [], []
morse_text = ""

def unpackWaveFile(path):
    '''This function unpacks the sound file and returns a list with the string 
    bytes of the frames that have been processed'''
    
    file = wave.open(path, 'r')
    
    #Read the number of frames that are present in the file
    n = file.readframes(file.getnframes())
    
    #Unpack the number of frames multiplied by the number of channels
    arg = "<"+str(file.getnframes()*file.getnchannels())+"H"
    tuple_file = struct.unpack(arg, n)

    #Read elements from the tuple and add to the list filtering based on the number of channels
    list_file = []
    for i in range(len(tuple_file)):
        #If number of channels is 2, then each element is repeated twice
        if i % file.getnchannels() ==0:
            list_file.append(tuple_file[i]) 
    
    return list_file

    
def checkForSpace(flag):
    '''This function is used to check for and thus add spaces between the morse code alphabets'''
    global morse_text
    
    #If flag is true and the call has reached here, it means that all 0's are over and we have reached the next element
    if flag == True:
        morse_text += " "
        flag = False
    return flag   


def printMorseText():
    '''This function takes the morse, dot and dash byte string lists and prints out the 
    morse code in the text form'''
    
    global morse, dot, dash, morse_text   
    flag = False
    
    for i, item in enumerate(morse):
        #Checking if the next character exists
        if i+1 < len(morse):
            #If the current and next item match the corresponding elements in the dot wav file
            if item == dot[1] and morse[i+1]==dot[2]:
                flag = checkForSpace(flag) 
                morse_text += "."
            
            #If the current and next item match the corresponding elements in the dash wav file
            elif item == dash[0] and morse[i+1]==dash[1]:
                flag = checkForSpace(flag)     
                morse_text += "-"
            
            #If the current matches the corresponding element in the dot wav file and the next does not
            #Local logic that inserts only the first element and nothing else in case of printing 3 spaces after every word
            elif item == dot[1] and morse[i+1]!=dot[2]:
                flag = checkForSpace(flag) 
                morse_text += "   "
            
            #Checking if the item is zero    
            elif item == 0:
                flag = True
             
    return morse_text  


def main():
    '''Controller function for the program'''
    global morse, dot, dash
        
    morse = unpackWaveFile(r"C:\Users\Gaurav Keswani\Documents\Eclipse\Morse-Code-Generator\src\resources\sound\morse.wav")
    dot = unpackWaveFile(r"C:\Users\Gaurav Keswani\Documents\Eclipse\Morse-Code-Generator\src\resources\sound\dot.wav")
    dash = unpackWaveFile(r"C:\Users\Gaurav Keswani\Documents\Eclipse\Morse-Code-Generator\src\resources\sound\dash.wav")
    
    morse_text = printMorseText()
    
    print("Morse Text retrieved from sound file: ",morse_text)
    print("English Text retrieved from sound file: ",MorseToEnglish(morse_text))
    
if __name__ == "__main__" : main()


#Dot ends with 65535 starts with 1
#Dash ends with 750 starts with 65089
