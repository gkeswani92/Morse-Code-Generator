from pydub import AudioSegment

def createSoundFile(morse):
    dot = AudioSegment.from_wav(r"C:\Users\Gaurav Keswani\Documents\Eclipse\Morse-Code-Generator\src\resources\sound\dot.wav")
    dash = AudioSegment.from_wav(r"C:\Users\Gaurav Keswani\Documents\Eclipse\Morse-Code-Generator\src\resources\sound\dash.wav")
    #word_gap = AudioSegment.from_wav(r"C:\Users\Gaurav Keswani\Documents\Eclipse\Morse-Code-Generator\src\resources\sound\void.wav")
    
    sound_config = AudioSegment.empty()
    
    #Splitting the morse sentence into various word codes
    codes = morse.split("   ")
    for morseWord in codes:
        #Splitting each word code into individual codes
        for item in morseWord:
            #Adding dot sound for zero
            if item == "0":
                sound_config += dot
            #Adding dash sound for one
            elif item == "1":
                sound_config += dash
            #Adding a 100ms wait between each alphabet
            else:
                sound_config += AudioSegment.silent(300)
        sound_config += dot[0.1:0.2]
    
    #Exporting the sound file as output.wav
    sound_config.export(r"C:\Users\Gaurav Keswani\Documents\Eclipse\Morse-Code-Generator\src\resources\sound\morse.wav", format="wav")
    
def printDictionary(dictionary):
    for key in dictionary:
        print ("{0}:{1}".format(key, dictionary[key]))
       
       
def modifyMorseToBinary(originalValue):
    '''This function converts the morse code from the . and - format to 0 and 1
    format respectively for easier processing'''
    
    modifiedMorse = ""
    for char in originalValue:
        #Converting . to 0's
        if char == ".":
            modifiedMorse += "0"
        #Convering - to 1's
        elif char == "-":
            modifiedMorse += "1"
            
    return modifiedMorse


def processMorse(sentence):
    '''This function replaces .'s with 0, -'s with 1 and keeps the spaces as it is. It also
    ignores all other characters'''
    
    modifiedSentence = ""
    
    for char in sentence:
        if char == ".":
            modifiedSentence += "0"
        elif char == "-":
            modifiedSentence += "1"
        elif char == " ":
            modifiedSentence += " " 
    
    return modifiedSentence
