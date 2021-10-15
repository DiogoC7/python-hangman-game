import random
import hangman_art
import hangman_words

def listToString(s):
    str1 = ""
    for ele in s: 
        str1 += ele
    return str1 

word_list = hangman_words.word_list

stages = hangman_art.stages

chosen_word = random.choice(word_list)

player_lives = 6
player_guess = []
hangman = ''
aux = []
current_stage = stages[6]

for n in range(0, len(chosen_word)):
  player_guess.append('_')

end_game = 1

print(hangman_art.logo)

while end_game > 0:
  guess = input("Guess a letter: ").lower()
  aux.clear()

  for n in player_guess:
    aux.append(n)

  for l in range(0, len(chosen_word)):
    if guess == chosen_word[l]:
      player_guess[l] = chosen_word[l]
  
  display = listToString(player_guess)

  if player_guess != aux: 
    print(current_stage)
    print(f"{display}")
    print(f"\nYou guessed {guess}, that's correct. You have {player_lives} lives left.\n")
  else:
    player_lives -= 1
    if player_lives == 5:
      current_stage = stages[5]
      print(current_stage)
    elif player_lives == 4:
      current_stage = stages[4]
      print(current_stage)
    elif player_lives == 3:
      current_stage = stages[3]
      print(current_stage)
    elif player_lives == 2:
      current_stage = stages[2]
      print(current_stage)
    elif player_lives == 1:
      current_stage = stages[1]
      print(current_stage)
    else:
      current_stage = stages[0]
      print(current_stage)

    print(f"{display}")
    print(f"\nYou guessed {guess}, that's not in the word. You have {player_lives} lives left.\n")
  
  if str(chosen_word) == display or player_lives == 0:
    end_game = 0

if player_lives > 0:
  print("You won!\n")
else:
  print(current_stage)
  print("You lose.\n")
