import random
def hangman():
    list_words=["mamatha","hangman","thirupathi","moriram","nirmala"]
    word =random.choice(list_words)
    turn =10
    guessmade=" "
    valid_entry =("abcdefghijklmnopqrstuvwxyz")
    while len(word)>0:
        main_word =" "
        for letter in word:
            if letter in guessmade:
                main_word =main_word+letter
            else:
                main_word = main_word+"_"
        if main_word == word:
            print(main_word)
            print("you won !!!!")
            break
        print("guess the words",main_word)
        guess = input("enter guess")
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("enter the valid character")
            guess=input("enter guess")
        if guess not in word:
            turn =turn-1
            if turn ==9:
                print("9 turn left!!!")
                print("----------------")
            if turn ==8:
                print("8 turn left!!!")
                print("----------------")
                print("       0        ")
            if turn ==7:
                print("7 turn left!!!")
                print("----------------")
                print("       0        ")
                print("       |        ")
            if turn ==6:
                print("6 turn left!!!")
                print("----------------")
                print("       0        ")
                print("       |        ")
                print("      /         ")
            if turn ==5:
                print("5 turn left!!!")
                print("----------------")
                print("       0        ")
                print("       |        ")
                print("      / \       ")
            if turn ==4:
                print("4 turn left!!!")
                print("----------------")
                print("      \0        ")
                print("       |        ")
                print("      / \       ")
            if turn ==3:
                print("3 turn left!!!")
                print("----------------")
                print("      \0/        ")
                print("       |        ")
                print("      / \       ")
            if turn ==2:
                print("2 turn left!!!")
                print("---------------- ")
                print("      \0/|       ")
                print("       |         ")
                print("      / \        ")
            if turn ==1:
                print("1 turn left!!!")
                print("----------------")
                print("      \0/|       ")
                print("       | |      ")
                print("      / \       ")
            
name=input("enter your name")
print("Welcome to hangman game",name,"!!")
print("---------------",name,"-------------")
print("Try to guess the word in less than 10 attempts")
hangman()














