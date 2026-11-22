from wonderwords import RandomWord
from collections import Counter
from spellchecker import SpellChecker
generator = RandomWord()
spell = SpellChecker()
class WordGame:
    def __init__(self):
        pass
    def word_generator(self):
        word = generator.word(word_max_length=10, word_min_length=5)
        print(f'\n================ {word.upper()} ================')
        return word
    def valid_word(self, word):
        if word not in spell:
            return False
        return True
    def is_correct_word(self, generated_word, submitted_word):
        generated = Counter(generated_word)
        submitted = Counter(submitted_word)
        if generated >= submitted:
            return True
        else:
            return False

if __name__ == '__main__':
    print(f'============ Welcome to WORDGAME ============')
    print(f'Instructions in  glimpse: Extract the meaningfull words as many as you can from the given Word. Each correct words points one score.')
    user_name = input('Your name: ')
    wordgame = WordGame()
    generated_word = wordgame.word_generator()
    score = 0
    words = []

    while True:
        print('============================================')
        is_willing = input('Do you have word in mind [Y|N] default [Y]: ')
        if is_willing.lower() not in ['y', 'n', '']:
            print(f'Invalid Option. Try again ❌')
            continue
        if is_willing.lower() == 'n':
            print('SCORE: ', score)
            break
        word = input('Enter an english word: ')
        if word not in words:
            words.append(word)
        else:
            print(f'The word is already entered. Try something else.')
            continue
        if wordgame.valid_word(word) and wordgame.is_correct_word(generated_word, word):
            score +=1
            print(f'✔️')
        else:
            print("❌")

        


