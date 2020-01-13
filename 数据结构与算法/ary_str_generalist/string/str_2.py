def is_cycle_word(word1, word2):
    if not word1 or not word2 or len(word1) != len(word2):
        return False
    new_word = word2 + word2
    if word1 in new_word:
        return True
    else:
        return False


print(is_cycle_word('123', '213'))

