import random

lives = 6

word_list=["car", "bike", "mango", "orange", "cycle"]

computer_value=random.choice(word_list)
word_length = len(computer_value)

placeholder =''
for i in range(word_length):
   placeholder +='_'
print("### Computer guesses a random word from list:###\n",placeholder)

condition = False
correct_letter =[]
while not condition:
   
   user_guess = input("** A letter gussed by the user to be in game.**--\n").lower()
   display =""

   for letter in computer_value:
      if letter == user_guess:
         display += letter
         correct_letter.append(letter)

      elif letter in correct_letter:
         display +=letter

      else:
         display += '_'
    

   print("display:",display)

   if user_guess not in computer_value:
        print("You have guessed wrong letter. Lives will be reduced\n")
        lives -= 1
        if lives == 0:
            print(f"You loose. Correct word is {computer_value}")
            condition = True

   if '_' not in display:
      condition= True
      print("Yo Won!")
