#import into main
def sort_on(dictionary):
    return dictionary["num"]

def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words
    

def character_count(text):
    alphabet = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
    'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
    's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }
    lcasetext = text.lower()
    for letter in alphabet:
        value = lcasetext.count(letter)
        alphabet[letter] = value
    return alphabet

def sort_char_dict(dictionary):
    dict_list = []
    for char in dictionary:
        new_dict = {"char": char, "num": dictionary[char]}
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list



        
