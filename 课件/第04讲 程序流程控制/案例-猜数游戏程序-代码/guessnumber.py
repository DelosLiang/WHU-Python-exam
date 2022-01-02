import random

secretNumber = random.randint(1,100)
guessedNumber = -1;

print('有一个1~100内的数，请你猜一猜。')
while guessedNumber != secretNumber:
    guessedNumber = int(input('输入你想到的数：'))

    deviation = abs(guessedNumber - secretNumber)
    if deviation >=10:
        print('太', end='')
    elif deviation >=5:
        print('有点', end='')
    elif deviation != 0:
        print('稍微', end='')
        
    if guessedNumber > secretNumber:
        print('大了，再试试。')
    elif guessedNumber < secretNumber:
        print('小了，再试试。')

print('祝贺你猜对了！')

