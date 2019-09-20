#Chloe Skillman
def function1(secret_word, lives): 
    """
    Takes words and lives as arguments
    Creates dictionary object with the supplied argument
    Returns dictionary object(Dict)
    """
    Dict = {}
    currentGuessed = "*" * len(secret_word)
    Dict["currentGuessed"]=str(currentGuessed)
    Dict["lives"]=int(lives)
    Dict["secret_word"]=str(secret_word)
    return Dict

def function2(Dict):
     """
     Takes the dictionary object(Dict) as an arguement
     Returns a Boolean result which says if the word has been guessed or not
     """
     if Dict["currentGuessed"] == Dict["secret_word"]:
         return 1
     else: return 0   

def function3(Dict):
    """
    Takes the dictionary object(Dict) as an arguement
    Will return number of lives left from the dictionary
    """
    return Dict["lives"]

def function4(Dict):
    """
    Takes a dictionary object(Dict) as arguement
    Will print how many lives you have left
    """
    s = "WORD:" + Dict["currentGuessed"] + \
        ": you have " + str(Dict["lives"]) + " lives left"
    print(s)


def function5(Dict,letter):
    """
    Takes dictionary object(Dict) and letter as arguements
    Will check if the letter is in the secret word (secret_word)
    if letter in the secret word, it will update guesses so far
    if it is no in the secret word minus one life
    returns occurences of the letter in the secret word
    """
    plist = []
    position=0
    occurs=0
    for i in Dict["currentGuessed"]:
        plist.append(i)
    for i in Dict["secret_word"]:
        if i == letter:
            plist[position]=letter
            occurs+=1
        position=position+1
    if occurs == 0: Dict["lives"]= function3(Dict)-1
    else :
        Dict["currentGuessed"]=""
        for i in plist:
            Dict["currentGuessed"]=Dict["currentGuessed"]+i
    return occurs


        
"""
Function takes two arguements and supplies them to function1
and storing the result in variable hm.
While loop uses variable hm
A check is made to check letter is uppercase.
Then indicates number of occurences of typed letter
Then message player telling them if they won or lost all lives.
"""

def playgame(secret_word,lives): 
    hm=function1(secret_word,lives)
    #While loop uses variable hm and outputs lives left and the imcomplete word                          
    while function3(hm)>0 and hm["currentGuessed"] !=hm["secret_word"]:
        function4(hm)
        letter = input("Guess a letter:")
        #A check is made to check letter is uppercase and display message if it is not                      
        while letter.isalpha() ==False or letter.isupper()==False:
            letter = input("That is not an upper-case letter - try again")
        occurs=function5(hm,letter)
        if occurs==0:
            print("The letter " + letter + " does not occur in the word")
        else: print("The letter " + letter + " occurs " + str(occurs) + " in the word")      
    #will output message to say if you won or lost    
    if function2(hm)==1:
        print("WORD: " + hm["secret_word"])
        print("Well done - you have guessed the word correctly")
    else:
        print("You have no lives left - you have been hung!")
        print("The word was " + hm["secret_word"])
    
"""
Main Body
Will ask the user for a file name to type in
Will open the file if file is available, if not it will terminate immediately

Will then ask user to choose a level difficulty
Lives will change depending on what level is chosen
A random word is then selected from the list
Will ask if user wants to play again
"""

#will ask the user to specify a file name
#main body
n=input("Please specify file: ")
try:
    file =open(n,'r')
except:
    print("Cannot open file ~ program will terminate")
    quit()
List=[]
line =file.readline()
while len(line) >0:
    List.append(line[:-1])
    line=file.readline()


# Allows the player to choose a level by typing it in
import random
running=True
while running:
    select = input(str("Choose a level (easy/intermediate/hard):"))
    if select=="hard":playgame(random.choice(List), 5)
    elif select=="intermediate":playgame(random.choice(List), 7)
    elif select=="easy":playgame(random.choice(List), 10)
    else: print("Input invalid ~ try again")

    select=str(input("Would you like to play again? (yes/no) :"))
    if select == 'yes' : running = True
    elif select == 'no': running = False
    else:
        while select!='yes' and select!='no':
            print("Input invalid ~ try again")
            select = (input("Try again - Would you like to play again? (yes/no) :"))
            if select == 'yes' : running = True
            elif select == 'no':
                running = False
                exit
        

file.close

                               
        



