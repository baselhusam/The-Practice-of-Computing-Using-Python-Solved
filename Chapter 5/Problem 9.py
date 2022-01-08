#Exercise 9

def vowel_cons_counter(sentence):
    full_letter = "qwertyuiopasdfghjklzxcvbnm" #string with all possible letters and without any sympol or special characters
    vowel, consonants = 0,0
    
    for i in sentence:
      if i in "aeiou": 
        vowel += 1 #counter for vowel letters
      elif i in full_letter: #if the letter wasn't vowel then check if it was a letter, not a sympol like dot, slash ... etc
        consonants += 1 #counter for consonatns letters
    
    
    print("number of vowel letters:",vowel)
    print("number of consonant letters:",consonants)
    #The end of the Function
    
inp = input("Please enter English sentence here: ").lower() #take a string as input and convert it to lower letters
vowel_cons_counter(inp)