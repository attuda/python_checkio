def verify_anagrams(first_word, second_word):
    if len(''.join(first_word.split())) != len(''.join(second_word.split())):
        return False
    for letter in first_word :
        if letter != ' ' and second_word.upper().count(letter.upper()) != first_word.upper().count(letter.upper()):
            return False
    return True
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"