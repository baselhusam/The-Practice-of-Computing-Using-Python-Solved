#Exercise 36

def rev_words(string):
    list_of_words = string.split()
    output_string = ""
    for i in reversed(list_of_words):
        output_string += i + ' '
    
    return output_string

inp = "What is your quest" #This could be as input
print(rev_words(inp))