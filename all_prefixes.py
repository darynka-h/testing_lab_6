"""Task implementing"""

def all_prefixes(word: str):
    word = word.lower()
    zero_letter = word[0]
    words_start_with_word_0 = []
    for i, letter in enumerate(word):
        if letter == zero_letter:
            words_start_with_word_0.append(word[i:])
    prefixes = []
    for word_ in words_start_with_word_0:
        counter = 1
        while counter <= len(word_):
            new_pref = word_[:counter]
            prefixes.append(new_pref)
            counter += 1
    return set(prefixes)

