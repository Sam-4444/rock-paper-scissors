import random

def play():
    user=input("whats your choice ? 'r' for rock 'p' for paper 's' for scissors :")
    computer=random.choice(['r','p','s'])

    if user==computer:
        print( "it is a tie")
    # conditions to win : r>s   ,   s>p  ,   p>r
    elif (user=="r"and computer=="s")or(user=="s"and computer=="p")or(user=="p"and computer=="r"):

        print( "You won ! ")

    else:print( "You lost !")


play()
