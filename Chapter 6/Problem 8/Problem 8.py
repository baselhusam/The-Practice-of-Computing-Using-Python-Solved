#Exercise 8

file = open("prplm_8.txt","r")
        
words = [word for line in file for word in line.split()] #putting all words in one list
text = " ".join(words) #putting all words in one variable as a string

sentences = text.split(".") #every sentence begin after the "." or beging of the words, so we split at (".")
cap = [i.strip().capitalize() for i in sentences] #for deletring the spaces between sentences ... then capitalize the sentences

output_file = open("output_prplm_8.txt","w")
for sen in cap:
    print(sen, file = output_file)#putting every sentence in a single line through for loop

file.close()
output_file.close()