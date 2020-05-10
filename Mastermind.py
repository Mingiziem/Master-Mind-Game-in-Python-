# Mastermind game Computer Vs Player


# Import random libraries
import random
''' Set variables for Computer Choice, Player Choice, and Number of Round Respectively
    and define Colors''' 
Computer_Choice = []
Player_Choice = ["", "", "",""]
Number_Round = 10
Color_Available= ["Blue","Green","Orange","Pink","Red","Yellow"]


#Define the functions colorRandom which generate the computer choice of color and its position
 #Which is fixed once it is generated because it is tuple
def colorRandom():
    Comp_Colors = [
        random.choice(Color_Available)
        for i in range(4)]
    return(Comp_Colors)

""" ***Define a function to get round result: 
  *****Black means the right colour in the right position
*******White means this colour is present in the computer choice but in the wrong position"""
def getResult():
    Result = ["Not Match", "Not Match", "Not Match", "Not Match"]
    Computer_Choice = list(Comp_tuple)
    Computer_Blst = Computer_Choice
    for i in range(len(Player_Choice)):
    # If there are any Blacks in the results and add it to the list 
        if Player_Choice[i] == Computer_Choice[i]:
            Result[i] = "black"
            Computer_Blst[i] = "taken"
    for i in range(len(Player_Choice)):
    # If there are any Whites in the results and add it to the list 
    #White means you get the answer but the position is not correct
    #Black means you get the answer
        for j in range(len(Computer_Choice)):
            if Player_Choice[i] == Computer_Blst[j]:
                Result[i] = "white"
                Computer_Blst[j] = "taken"
                break
    print(f"\nThe result is {Result}\n")
    return Result 

"""
*****Define computer color choice
*******The result of random color list
*********Tuple of omputer which is unchangable as a reference to use for the initial computer choice of colors 
************Remember: We can modifiy the computer _choice variable during the function getResult 
**************Functionsare mutuable """

Comp_tuple = tuple(colorRandom())

"""
***********Time to get input from Player his choice of colors which is four color from the available colors *****
***********Available Colors Blue, Green , Orange, Pink , Red, Yellow***********
""" 
def requestPlayer():
    print("************ Your Color Blue,Green, Orange, Pink, Red, or Yellow ************************************")
    for i in range(len(Computer_Choice)):
       # print("************ Your Color Blue,Green, Orange, Pink, Red, or Yellow ************************************")
        Player_Choice[i] = input(f"**** Enter for Position {i+1}: ---->")
        while Player_Choice[i] not in Color_Available:         
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Wrong. Please enter **no space, or *** First Capital letters!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            Player_Choice[i] = input(f"*******ENTER AGAIN FOR POSITION NUMBER {i+1}:----->")

            
#Define Computer choice
Computer_Choice = colorRandom()

print("Game : Computer Vs Player")
# Play the game. The game is composed of a maximum of 10 rounds. if after 10 rounds the user has not found the 
# computer's choice then the computer wins
for i in range(10):
    print(f"This is round number {i+1}")
    requestPlayer()
    result2 = getResult()
    if result2 == ["black", "black", "black", "black"]:
        print("Congratulations! You won!!")

if result2 != ["black", "black", "black", "black"]:
    print(f"Sorry but you lost. The answer was {Comp_tuple}")