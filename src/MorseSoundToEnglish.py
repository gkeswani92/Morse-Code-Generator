import wave
import struct
from MorseToEnglish import MorseToEnglish
morse, dot, dash = [], [], []

def readMorseFile():
    '''This function unpacks the morse code sound file and returns a list with the string 
    bytes of the frames that have been processed'''
    
    waveFileMorse = wave.open(r"C:\Users\Gaurav Keswani\Documents\Eclipse\Morse-Code-Generator\src\resources\sound\morse.wav", 'r')
    #Read the number of frames that are present in the file
    x =waveFileMorse.readframes(waveFileMorse.getnframes())
    
    #Unpack the number of frames multiplied by the number of channels
    arg = "<"+str(waveFileMorse.getnframes()*waveFileMorse.getnchannels())+"H"
    tup_morse = struct.unpack(arg, x)
    
    #Since there are 2 channels, we only want one of the two duplicate entries
    list_morse = []
    for i in range(len(tup_morse)):
        if waveFileMorse.getnchannels()==2:
            if i % 2 ==0:
                list_morse.append(tup_morse[i])
    
    #print ("Morse File:",list_morse)
    return list_morse


def readDotFile():  
    '''This function unpacks the dot sound file and returns a list with the string 
    bytes of the frames that have been processed'''
    
    waveFileDot = wave.open(r"C:\Users\Gaurav Keswani\Documents\Eclipse\Morse-Code-Generator\src\resources\sound\dot.wav", 'r')
    
    #Read the number of frames that are present in the file
    x = waveFileDot.readframes(waveFileDot.getnframes())
    
    #Unpack the number of frames multiplied by the number of channels
    arg = "<"+str(waveFileDot.getnframes()*waveFileDot.getnchannels())+"H"
    tup_dot = struct.unpack(arg, x) 
    
    list_dot = []
    
    for i in range(len(tup_dot)):
        if waveFileDot.getnchannels()==2:
            if i % 2 ==0:
                list_dot.append(tup_dot[i]) 
    
    #print ("Dot File:",list_dot)
    return list_dot


def readDashFile():
    '''This function unpacks the dash sound file and returns a list with the string 
    bytes of the frames that have been processed'''
    
    waveFileDash = wave.open(r"C:\Users\Gaurav Keswani\Documents\Eclipse\Morse-Code-Generator\src\resources\sound\dash.wav", 'r')
    
    x =waveFileDash.readframes(waveFileDash.getnframes())
    
    #Unpack the number of frames multiplied by the number of channels
    arg = "<"+str(waveFileDash.getnframes()*waveFileDash.getnchannels())+"H"
    tup_dash = struct.unpack(arg, x)
    
    list_dash = []
    for item in tup_dash:
        list_dash.append(item)
        
    #print ("Dash File:", list_dash)
    return list_dash
    
    
def printMorseText():
    '''This function takes the morse, dot and dash byte string lists and prints out the 
    morse code in the text form'''
    
    global morse, dot, dash   
    morse_text = ""
    
    flag = False
    
    for i, item in enumerate(morse):
        if i+1 < len(morse):
            if item == dot[1] and morse[i+1]==dot[2]:
                if flag == True:
                    morse_text += " "
                    flag = False
                morse_text += "."
            
            elif item == dash[0] and morse[i+1]==dash[1]:
                if flag == True:
                    morse_text += " "
                    flag = False     
                morse_text += "-"
            
            elif item == dot[1] and morse[i+1]!=dot[2]:
                if flag == True:
                    morse_text += " "
                    flag = False
                morse_text += "   "
                
            elif item == 0:
                flag = True
             
    return morse_text  

def main():
    global morse, dot, dash
    
    morse = readMorseFile()
    dot = readDotFile()
    dash = readDashFile()
    
    morse_text = printMorseText()
    print("Morse Text retrieved from sound file: ",morse_text)
    print("English Text retrieved from sound file: ",MorseToEnglish(morse_text))
    
if __name__ == "__main__" : main()





'''Dot ends with 65535 starts with 1
Dash ends with 750 starts with 65089'''
