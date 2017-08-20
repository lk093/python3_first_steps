from random import randint

# Input
randNum = randint(1, 10)

print('you have 3 times left,')
guessNum = int(input('guess a number between 1 and 10: '))

#  count with initial guess
count = 1

# Processing
while (guessNum != randNum) and count < 3:
     count += 1
     if guessNum < randNum:
         print(guessNum, 'is too small, try again!')
     else:
         print(guessNum, 'is too big, try again!')
     guessNum = int(input('guess: '))

# Evaluation
if count == 3 and guessNum != randNum:
    print('sry, you lost!', randNum , 'was the answer')
else:
    print('you were right!')

