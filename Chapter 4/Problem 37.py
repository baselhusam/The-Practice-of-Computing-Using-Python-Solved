#Exercise 37

first_word = input("Enter the first word: ")
second_word = input("Enter the second word: ")


if len(first_word) >= len(second_word):
    print(first_word.upper())
    print(second_word.capitalize())
else:
    print(second_word.upper())
    print(first_word.capitalize())


