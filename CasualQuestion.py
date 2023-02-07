import random
from termcolor import colored

f = open("C:\\Users\\loren\\Desktop\\GitHub\\CasualQuestion\\Questions.txt", "r")

list_questions = []
for x in f:
        list_questions.append(x)

number_of_questions = len(list_questions) - 1 

mistake_number = 0 
i = 0
numeri_usciti = []
exit = False
while True:
    i = i + 1

    random_number = random.randint(1, number_of_questions)
    while True:
        if random_number in numeri_usciti:
            random_number = random.randint(1, number_of_questions)
            if len(numeri_usciti) == number_of_questions: 
                print(colored('Domande finite', 'red'))
                exit = True
                break
        else: 
            break
    if exit: 
        break

    print('\n' + colored(list_questions[random_number], 'green'))
    numeri_usciti.append(random_number)
    mistake_counter = input('Press "f" if you made a mistake ')
    if mistake_counter == 'f':
        mistake_number = mistake_number + 1 

    loop_exit = input('Press "q" if you want to to quit ')
    if loop_exit == 'q': 
        break
    
   

print(str(i - mistake_number) + '/' + str(i))
input('')