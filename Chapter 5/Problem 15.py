#Exercise 15

#A)

def check_message(message):
    if len(message) < 160:
        return message
    else :
        return message[:160]
    
inp = input("Enter a message here: ")
print(check_message(inp))


#B)

def check_message_in_words(message):
    message = message.split()
    if len(message) <= 20 :
        return " ".join(message)
    else :
        return " ".join(message[:20])
    
print(check_message_in_words(inp))