for r in range(4):
    print("")
    for c in range(7):
        if (c==4 or c==0):
            print("*",end="")
        elif(r==1 and (c==1 or c==3)):
            print("*",end="")
        elif(r==2 and c==2):
            print("*",end="")
        else:
            print(" ",end="")
