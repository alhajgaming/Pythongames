#code by alhajkhan
import random
if __name__ == '__main__':
    #comment for rock paper scrissor game

    userturn = int(input("enter 1 for rock,press 2 for paper, press 3 for scrissor: "))
    computerturn = random.randint(1,3)
    match userturn:
        case 1:
            if(computerturn == 1):
                print("computer chose rock - draw")
            elif(computerturn == 2):
                print("computer chose paper - lose")
            elif(computerturn == 3):
                print("computer chose scrissor - win")
            else:
                print("error 404")
        case 2:
            if(computerturn == 1):
                print("computer chose rock - win")
            elif(computerturn == 2):
                print("computer chose paper - draw")
            elif(computerturn == 3):
                print("computer chose scrissor - lose")
            else:
                print("error 404")
        case 3:
            if(computerturn == 1):
                print("computer chose rock - win")
            elif(computerturn == 2):
                print("computer chose paper - lose")
            elif(computerturn == 3 ):
                print("computer chose scrissor - draw")
            else:
                print("error")
        case _:
            print("enter vaild input betweeen 1 to 3 to proceed")
