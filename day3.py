# guess a number

import random
secretnumber = random.randint(1, 10)  

print("Guess a number 1-10.")

for attempt in range(3):  
    guess = int(input("Take a guess: "))

    if guess == secretnumber:
        print("you got it!!", secretnumber)
        break
    else:
        print("Nope, try again!")
else:
    print("Srry, you're out of attempts. the number was", secretnumber)
