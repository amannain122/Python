#JUMBLE WORDS OFFERED BY COMPUTER
from jumble_02 import *
def play():
    name1=input('PLayer 1, Enter your name: ')
    name2=input('PLayer 2, Enter your name: ')
    pl1=0
    pl2=0
    turn=0
    while(1): 
        word=choose()
        ques=jumble(word) 
        print("What is this word? ", ques)
        #PLAYER 1
        if(turn%2==0):
            print(name1, 'your turn')
            ans=input("Guess the word: ")
            ans.lower()
            if(ans==word):
                print("Hurray")
                pl1+=1
                print('Your Score is: ',pl1)
            else:
                print("Ohh, that's not correct, try again!")
            c=int(input("Press 1 to continue, 0 to quit: "))
            if c==0:
                print("Thank you for playing")
                print('Scores are of P1 and P2: ',pl1,'',pl2)
                break
            
        #PLAYER 2
        else:
            print(name2, 'your turn')
            ans=input("Guess the word: ")
            ans.lower()
            if(ans==word):
                print("Hurray")
                pl2+=1
                print('Your Score is: ',pl2)
            else:
                print("Ohh, that's not correct, try again!")
            c=int(input("Press 1 to continue, 0 to quit: "))
            if c==0:
                print("Thank you for playing")
                print('Scores are of P1 and P2: ',pl1,'',pl2)
                break
        turn+=1
        
play()
