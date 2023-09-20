import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_map=[rock,paper,scissors]
player_ans = input("What do you choose ? Rock , paper or scissors \n")
print(f'\n You chose {player_ans}')
if player_ans == 'rock':
  position =game_map[0]
  print(position)
elif player_ans == 'paper':
  position =game_map[1]
  print(position)
elif player_ans =='scissors':
  position =game_map[2]
  print(position)
else:
  print("Enter valid inuput")
  exit(0)


computer_ans= random.randint(0,2)
ai_answer = game_map[computer_ans]
if ai_answer == rock:
  print(f"The computer chose rock \n{ai_answer} ")
elif ai_answer == paper:
  print(f"The computer chose paper \n{ai_answer} ")
else:
  print(F"The computer chose scissors \n {ai_answer}")

if(position==ai_answer):
  print("Game Drawn")
elif(position==game_map[0] and ai_answer==game_map[1]):
  print("Paper beats rock ! Computer won.")
elif(position==game_map[0] and ai_answer==game_map[2]):
  print("Rock beats Scissors ! You won")
elif(position==game_map[1] and ai_answer==game_map[0]):
  print("Paper beats Rock ! You won")
elif(position==game_map[1] and ai_answer==game_map[2]):
  print("Scissors beats Paper ! Computer won")
elif(position==game_map[2] and ai_answer==game_map[0]):
  print("Rock beats Scissors ! Computer won")
else:
  print("Scissors beats Paper ! You won")
 
