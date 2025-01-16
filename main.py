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