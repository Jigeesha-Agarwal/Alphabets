for r in range(6):
    print("")
    for c in range(4):
        if((r==0 or r==5) and c==3):
            print("*",end="")
        elif((r==1 or r==4)and c==2):
            print("*",end="")
        elif((r==2 or r==3)and c==1):
            print("*",end="")
        elif( c==0):
            print("*",end="")
        else:
            print(" ",end="")
