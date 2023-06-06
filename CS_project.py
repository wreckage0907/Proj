""" Group Members :
1. Janeshvar S
2. M Girish Raghav
3. Rohan Sameen
Topic: Implementation of 2 player tic-tac-toe in python and Word Guess  """
def scoreboard():
    import csv
    f=open("player.csv","a")
    writer=csv.writer(f)
    #writer.writerow(["Name","Tictac wins","Word wins"])
    while True:
        player=input("Enter name of player:")
        record=[player,int(0),int(0)]
        writer.writerow(record)
        ans=input("Do you want to enter another player?(y/n)")
        if ans.lower()=='n':
            break
    f.close()

def tictactoe():
    import csv
    theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,# making the board using dictionary
                '4': ' ' , '5': ' ' , '6': ' ' , #the keys represent the position in a 3x3 table
                '1': ' ' , '2': ' ' , '3': ' ' } #the empty spaces declared are updated for every move in the game down the program 

    board_keys = []

    for key in theBoard:
        board_keys.append(key)

    ''' We will have to print the updated board after every move in the game and 
        thus we will make a function in which we'll define the printBoard function
        so that we can easily print the board everytime by calling this function. '''

    def printBoard(board):
        print(board['7'] , '|' , board['8'] , '|' , board['9'])
        print('- + - + -')
        print(board['4'] , '|' , board['5'] , '|' ,board['6'])
        print('- + - + -')
        print(board['1'] , '|' , board['2'] , '|' , board['3'])
    print(" key positions " )
    print("7 | 8 | 9")
    print("4 | 5 | 6")
    print("1 | 2 | 3")

    # Now we'll write the main function which has all the gameplay functionality.
    def game():
        f=open("player.csv","r+")       
        reader=csv.reader(f)
        read=[]
        p1=input('enter name of player1')
        p2=input('enter name of player2')
        for line in reader:
            if line[0]==p1:
                name1,tic1,mad1=line[0],int(line[1]),line[2]
            if line[0]==p2:
                name2,tic2,mad2=line[0],int(line[1]),line[2]
        ini1,ini2=tic1,tic2
        
        turn = 'X'
        count=0

        for i in range(10):
            printBoard(theBoard)
            print("It's your turn," + turn + ".Move to which place?")
            move = input()        

            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue

            # Now we will check if player X or O has won,for every move after 5 moves. 
            if count >= 5:
                if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # top
                    printBoard(theBoard)
                    print("\nGame Over.\n")                
                    if turn=='X':
                        tic1+=4
                        tic2-=1
                        print(" **** " ,p1 , " won. ****")
                
                    else:
                        tic1-=1
                        tic2+=4
                        print(" **** " ,p2, " won. ****")
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': #  middle
                    printBoard(theBoard)
                    print("\nGame Over.\n")                
                    if turn=='X':
                        tic1+=4
                        tic2-=1
                        print(" **** " ,p1 , " won. ****")
                
                    else:
                        tic2+=4
                        tic1-=1
                        print(" **** " ,p2, " won. ****")
                    break
                elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': #  bottom
                    printBoard(theBoard)
                    print("\nGame Over.\n")                
                    if turn=='X':
                        tic2-=1
                        tic1+=4

                        print(" **** " ,p1 , " won. ****")
                
                    else:
                        tic2+=4
                        tic1-=1
                        print(" **** " ,p2, " won. ****")
                    break
                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                    printBoard(theBoard)
                    print("\nGame Over.\n")                
                    if turn=='X':
                        tic2-=1
                        tic1+=4
                        print(" **** " ,p1 , " won. ****")
                
                    else:
                        tic1-=1
                        tic2+=4
                        print(" **** " ,p2, " won. ****")
                    break
                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                    printBoard(theBoard)
                    print("\nGame Over.\n")                
                    if turn=='X':
                        tic1+=4
                        tic2-=1
                        print(" **** " ,p1 , " won. ****")
                
                    else:
                        tic1-=1
                        tic2+=4
                        print(" **** " ,p2, " won. ****")
                    break
                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                    printBoard(theBoard)
                    print("\nGame Over.\n")                
                    if turn=='X':
                        tic2-=1
                        tic1+=4
                        print(" **** " ,p1 , " won. ****")
                
                    else:
                        tic1-=1
                        tic2+=4
                        print(" **** " ,p2, " won. ****")
                    break 
                elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                    printBoard(theBoard)
                    print("\nGame Over.\n")                
                    if turn=='X':
                        tic2-=1
                        tic1+=4
                        print(" **** " ,p1 , " won. ****")
                
                    else:
                        tic1-=1
                        tic2+=4
                        print(" **** " ,p2, " won. ****")
                    break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    if turn=='X':
                        tic2-=1
                        tic1+=4

                        print(" **** " ,p1 , " won. ****")
                
                    else:
                        tic1-=1
                        tic2+=4
                        print(" **** " ,p2, " won. ****")
                    break
            
            # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            if count == 9:
                print("\nGame Over.\n")                
                print("It's a Tie!!")
        

            # Now we have to change the player after every move.
            if turn =='X':
                turn = 'O'
            else:
                turn = 'X'        
        
        replace([p1,ini1,mad1],[p1,tic1,mad1])
        replace([p2,ini2,mad2],[p2,tic2,mad2])
        # Now we will ask if player wants to restart the game or not.
        restart = input("Do want to play Again?(y/n)")
        if restart == "y" or restart == "Y":
            for key in board_keys:
                theBoard[key] = " "
            game()
        if restart == "n" or restart == "N":
            print('''Thank you for playing!!!
    you are true gamer
    stay safe ヽ(•‿•)ノ''')
    game()
    f=open("player.csv","r")
    r=csv.reader(f)
    for i in r:
        print(i)

        
def replace(initial,new):
    import os
    import csv
    x=open("player.csv","r")
    y=open("temp.csv","w")
    reader=csv.reader(x)
    csv_w=csv.writer(y)
    for record in reader:
        if record[0]==initial[0]:
            csv_w.writerow(new)
        else:
            csv_w.writerow(record)
    x.close()
    y.close()
    os.remove("player.csv")
    os.rename("temp.csv","player.csv")

def madlibs():
    import random
    import csv
    f=open("MAD.txt","r")
    data=f.readlines()
    n=len(data)
    b=random.randint(0,n-1)
    x=data[b]
    word=x.split()
    d=len(word)
    f.close()
    player=input("Enter player name:")
    f=open("player.csv","r+")
    data1=csv.reader(f)
    p=0
    for line in data1:
        if line[0]==player:
            name1,tic1,mad1=line[0],line[1],int(line[2])
            p=1
            print("PlayerFound")
    if p==0:
        print("Player is not saved")
        madlibs()
    inimad1=mad1
    f.close()
    def playmadlibs():
        b=random.randint(0,n-1)
        x=data[b]
        word=x.split()
        d=len(word)

        nonlocal mad1
        l=["is","we","than","as","if","but","A","An","the","a","of","to","it","in"]
        while True:
            y=word[random.randint(0,d-1)] 
            if y not in l:
                break
        temp=" "
        for i in word:
            if i!=y:
                temp=temp+" "+i
            else:
                temp=temp+" "+"_____"
        print(temp)
        
        ans=input("Enter the correct word to fill in the blanks.")
        if ans==y or ans==y.lower():
            print("You are corect")
            mad1+=4
        else:
            print("You are wrong,T_T")
            mad1-=1
    playmadlibs()
    while True:
        ans=input("do u want to continue(y/n)?")
        if ans.lower()=='y':
            playmadlibs()

        if ans.lower()=='n':
            print(mad1,inimad1)
            replace([name1,tic1,inimad1],[name1,tic1,mad1])
            break

def searchname():
    import csv
    f=open("player.csv","r")
    data=csv.reader(f)
    name=input("Enter Name to Search:")
    flag=0
    for player in data:
        if player[0]==name:
            print("Name:",player[0])
            print("TicTacToe Score:",player[1])
            print("Madlib Score:",player[2])
            flag=1
    if flag==0:
        print("Player not found")
    f.close()
    
def viewscoreboard():
    import csv
    f=open("player.csv","r")
    data=csv.reader(f)
    for player in data:
        print("Name:",player[0])
        print("TicTacToe Score:",player[1])
        print("Madlib Score:",player[2])
    f.close()

def deleterecord():
    import csv
    import os
    x=open("player.csv","r")
    y=open("temp.csv","w")
    data=csv.reader(x)
    csv_writer=csv.writer(y)
    name=input("Enter player name to be deleted:")
    p=0
    for line in data:
        if line[0]!=name:
            csv_writer.writerow(line)
        if line[0]==name:
            p=1
            
    if p==0:
        print("Player Not Found")
    else:
        print("Player Deleted")
    x.close()
    y.close()
    os.remove("player.csv")
    os.rename("temp.csv","player.csv")


def main():
    while True:
        try:
            print("What do you want to Do?" )
            print("1.Tic Tac Toe " )
            print("2.Word Guess")
            print("3.Add New Player Name")
            print("4.View A Player Score")
            print("5.View All Player Data")
            print("6.Delete Player Record")
            print("7. Exit")
            a=int(input("Which Number??(1/2/3/4/5/6/7)"))
            if  a==1:
                tictactoe()
            elif a==2:
                madlibs()
            elif a==3:
                scoreboard()
            elif a==4:
                searchname()
            elif a==5:
                viewscoreboard()
            elif a==6:
                deleterecord()
            elif a==7:
                break
            else:
                print('please enter a valid input')
        except ValueError:
                print('please enter a valid input')
        
main()
