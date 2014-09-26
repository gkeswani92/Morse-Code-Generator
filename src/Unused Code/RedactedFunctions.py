def playSound(morse):
    '''This functions takes the morse code in text as input and converts it into the 
    audio format'''
    
    print ("Morse code in audio format is-->")
    
    #Splitting the morse sentence into various word codes
    codes = morse.split("   ")
    for morseWord in codes:
        #Splitting each word code into individual codes
        for item in morseWord:
            if item == "0":  #Playing dot sound in case of 0
                playSoundWin("dot")
            elif item == "1": #Playing dash sound in case of 1
                playSoundWin("dash")
            else:
                sleep(0.3) # Time in seconds between alphabets
        sleep(1) # Time in seconds between words
        
def findSpaces():
    global morse, dash
    
    #Input: is gaurav
    #Output: .. ...   --. .- ..- .-. .- ...-
    
    #Dot ends with 65535 starts with 1
    #Dash ends with 750 starts with 65089
    
    first_dot_end = morse.index(65535)
    second_dot_end = morse.index(65535, first_dot_end+1)
    third_dot_end = morse.index(65535,second_dot_end+1)
    fourth_dot_end = morse.index(65535, third_dot_end+1)
    fifth_dot_end = morse.index(65535, fourth_dot_end+1)
    
    third_dot_start = morse.index(1,second_dot_end+1)
    
    
    print (len(morse[second_dot_end+1:third_dot_start]))
    print ("Intra word: ",third_dot_start-second_dot_end)
    
    
    first_dash_begin=morse.index(65089)
    print (fifth_dot_end)
    print (first_dash_begin)
    print ("Interword: ",first_dash_begin - fifth_dot_end - 1)
    
    
def playSoundWin(name):
    '''This function is used to play the sound file depending on the parameter being passed'''
    if name == "dot":
        winsound.PlaySound(r"C:\Users\Gaurav Keswani\Documents\Eclipse\Morse-Code-Generator\src\resources\sound\dot.wav",0)
    elif name == "dash":
        winsound.PlaySound(r"C:\Users\Gaurav Keswani\Documents\Eclipse\Morse-Code-Generator\src\resources\sound\dash.wav",0)
    