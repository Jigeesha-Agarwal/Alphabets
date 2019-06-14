for r in range (5):
    print("")
    for c in range (4):
        if(r==2):
            print("*",end="")
        elif(c==0 or c==3):
            print("*",end="")
        else:
            print(" ",end="")
