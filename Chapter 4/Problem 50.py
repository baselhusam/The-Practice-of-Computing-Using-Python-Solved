#Exercise 50

vowel_set = set()
vowels = ['a', 'e', 'i', 'o', 'u']
trials = 0
while len(vowel_set) < 5:
    # (1) prompt for input
    user_input = input('Enter a word: ')

    # (2) extract all the vowels in the input string and make them lowercase
    # (3) add all the nonduplicate vowels you found into a temporary string
    temp_string = "".join([letter.lower() for letter in user_input if letter.lower() in vowels])

    # (3.5) add any unique vowels to the set if they haven't been encountered before
    for vowel in temp_string:
        if vowel not in vowel_set:
            vowel_set.add(vowel)

    # (4) stop the code when you have collected all five vowels (aeiou)
    # and print the number of trials that you did to collect all five vowel characters
    trials += 1

print("It took {} trials to fill the vowel set".format(trials))

