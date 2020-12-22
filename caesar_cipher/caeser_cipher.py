from nltk.corpus import words
word_list = words.words()

all_word_list = set([word.lower() for word in word_list])

letter_string = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(words, key):
    encrypted_words = ''

    for x in words.lower():
        if x in letter_string:
            encrypted_letter = letter_string[(letter_string.index(x.lower()) + key) % len(letter_string)]
            encrypted_words += encrypted_letter
        else:
            encrypted_words += x
    return encrypted_words    

def decrypt(words):

    def english_words(words_list):
        num = 0
        for y in words_list:
            if y in all_word_list:
                num += 1
        if num/len(words_list) >= 0.5:
            return True
        return False

    for j in range(len(letter_string)):    
        first = encrypt(words, (-1*(j)))
        second = english_words(first.split(' '))
        if second:
            return first