from random import random, randint
 
final_number = randint(0, 100) 

for i in range(5):
    number = int(input('Enter yout number:'))

    if number == final_number:
        print('GG\'s you won!')
        break
    
    if number > final_number:
        if number - final_number <= 10:
            print('wrong , it\'s too much!')
            print(f'you have done {i + 1} try!')
        else:
            print('wrong!')
            print(f'you have done {i + 1} try!')

    else:
        if final_number - number <= 10:
            print('wrong , it\'s less!')
            print(f'you have done {i + 1} try!')
        else: 
            print('wrong!')
            print(f'you have done {i + 1} try!')

print(f'final number was {final_number}')

    
        

