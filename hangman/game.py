from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []

def _get_random_word(list_of_words):
    if list_of_words == []:
        raise InvalidListOfWordsException
    else:
        return random.choice(list_of_words)
    

def _mask_word(word):
    if len(word) == 0:
        raise InvalidWordException('Those words cannot.')
    
    word_length = len(word)
    masked_word = word.replace(word, "*"*word_length)
    return(masked_word)


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) == 0 or len(masked_word) == 0:
        raise InvalidWordException('Those words are invalid.')
    
    if len(character) > 1:
        raise InvalidGuessedLetterException('Those guess letters are invalid.')

    if len(answer_word) != len(masked_word):
        raise InvalidWordException('Those words are invalid.')

    result = ''
    index = 0
    for i in answer_word:
        if (i.lower()) == (character.lower()):
            result += (character.lower())
        else:
            result += masked_word[index]
        index += 1
    final_result = ''.join(result)
    return(final_result)
        

def guess_letter(game, letter):
    if game['masked_word'] == game['answer_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException('The game has finished.')
    
    from game import _uncover_word
    
    if (letter.lower()) in ((game['answer_word']).lower()):
        new_masked_word = _uncover_word(game['answer_word'], game['masked_word'], letter)
        game.update(masked_word = new_masked_word)
    else:
        game['remaining_misses'] -= 1

    game['previous_guesses'].append(letter.lower())
    
    if game['masked_word'].lower() == game['answer_word'].lower():
        raise GameWonException
    
    if game['remaining_misses'] == 0 and game['masked_word'] != game['answer_word']:
        raise GameLostException
    

    return game
        


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }


    return game
    


