import api
import cli

class Hangman():

    def __definition__(definition: str, state: bool) -> str:
        if state == True: return ''.join(['~ ', definition, '\n'])
        return ''
    
    def play(nlives: int = None, show_definition: bool = None) -> bool:
        if nlives == None:
            nlives = 8
        if show_definition == None:
            show_definition = False
        lives = nlives
        
        response, json_keys = api.get_word()
        word = response[json_keys['word']].lower()

        row_of_letters = ['_'] * len(word)
        guessed_letters = []

        while lives > 0:
            damage = 1

            cli.clear()
            print(''.join([
                '{hangman.py}'
                '\nWord: ',
                ' '.join(row_of_letters),
                '\n',
                Hangman.__definition__(response[json_keys['definition']], show_definition),
                '\n- lives remaining: ',
                str(lives),
                '\n- letters guessed: ',
                ' '.join(guessed_letters),
            ]))
            guess = input('Guess (a letter or the word): ').lower()
            
            if len(guess) == 1:
                if guess not in guessed_letters:
                    guessed_letters.append(guess)
                    if guess in word:
                        occurences = [i for i, element in enumerate(word) if element == guess]
                        for i in occurences: 
                            row_of_letters[i] = guess
                        if '_' not in row_of_letters:
                            break
                else:
                    damage = 0
            elif guess == word:
                break
            
            lives -= damage
        
        print(''.join(['\nWord: ', word]))
        if lives > 0:
            print(''.join([
                'YOU WIN | lives remaining: ',
                str(lives)
            ]))
            return True
        else:
            print('YOU LOSE')
            return False

Hangman.play(
    show_definition = True 
)