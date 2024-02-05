import random
import hangman_art as ha
import hangman_words as hw

print(ha.logo)
stages = ha.stages
word_list = hw.word_list
chosen_word = random.choice(word_list)
print(chosen_word)
display = ['_']*(len(chosen_word))
print(display)

end_game = True
lives = 6

while end_game ==True:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    elif guess in chosen_word:
        for i in range(0,len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess
        print(f"{' '.join(display)}")
    else:
        print(f" You guess a letter {guess}, that is not in the word. You lose a life")
        print(stages[lives])
        print(f"{' '.join(display)}")
        lives-=1
    
    if '_' not in display:
        end_game = False
        print('You Win!')
    
    if lives < 0:
        end_game = False
        print('You Lose!')


