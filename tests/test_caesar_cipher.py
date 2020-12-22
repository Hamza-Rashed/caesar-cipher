from caesar_cipher.caeser_cipher import *
import random

def test_decrypt():
    encrypted_string = encrypt(words, 10)
    assert decrypt(encrypted_string) == "klm"

def test_decrypt_random_key():
    encrypted_string = encrypt(words, random.randint(1, len(letter_string)))
    assert decrypt(encrypted_string) == "It was the best of times, it was the worst of times."
