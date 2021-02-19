#hangman game project
word_list=["cat","dog","parrot","cheese","computer","chicken","elbow","arm","head","ball","peanut","chair"]
pick_word = input("pick a number between 0 and 11! ")
num = int(pick_word)
choice = word_list[num]#   allows user to pick number that pulls word from a list.

def hangman(word):
    win = False
    wrong_answer = 0#  this variable keeps track of wrong guesses.
    hanging_man =["",
                  "-------------!-------         ",
                  "||           |                ",
                  "||           |                ",
                  "||           |                ",
                  "||          (Q)               ",
                  "||         / | \              ",
                  "||        /  |  \             ",
                  "||           |                ",
                  "||          / \               ",
                  "||         /   \              ",
                  "||                            ",
                  "||                            ",
                  "=============================="
                  ]
    rletters = list(word)#keeps track of the word that is to be guessed in a list.
    board = ["_"]*len(word)#this is to provide a line for every letter not yet guessed.
    print("welcome to hang man!")
    while wrong_answer<len(hanging_man)-1: #a loop comparing wrong answers to lenght of hanging man list
        print("\n")
        msg="guess a letter:  "
        guess = input(msg)#input the guess
        if guess in rletters:
            cind =rletters.index(guess)#cind will become the index number of the letter guessed
            board[cind] = guess# reassigns the list in board from _ to the letter that is correct
            rletters[cind] = '$'#workaround for making index work on words with duplicate letters example: ( 3 'a' in word now two a and a $.)
            print("yes!")
        else:
            print("wrong!")
            wrong_answer += 1
            print((" ".join(board)))
            e = wrong_answer + 1
            print("\n".join(hanging_man[0:e]))#this prints the next segment of the hanging man. e has been advanced, and so it prints from 0 to the matching index.
            if "_"not in board:#this section checks if there are any spaces left in board. in not all letters have been guessed.
                print("you win!")
                print(" ".join(board))      
                win = True
                break
    if not win:
        print("\n".join(hanging_man[0:wrong_answer+1]))
        print("you lose! it was {}.".format(word))
            
hangman(choice)                      
