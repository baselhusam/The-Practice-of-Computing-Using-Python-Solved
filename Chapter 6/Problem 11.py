#Exercise 11

def safe_input(prompt, type):
    if type in type(prompt) :
        return prompt
    else:
        print("Invalid input. Try again")
        prompt = input("Prompt input: ")
        typee= input("Enter the type you want: ")
        return safe_input(prompt, typee)
    
prompt = input("Prompt input: ")
typee = input("Enter the type you want: ")

print(safe_input(prompt,typee))