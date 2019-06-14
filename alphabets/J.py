for r in range(6):
    print("")
    for c in range(7):
        if(r==0 or (r==5 and (c==1 or c==2)) ):
            print("*",end="")
        elif(c==3 and (r==1 or r==2)):
            print("*",end="")
        elif((r==3 or r==4) and (c==0 or c==3)):
            print("*",end="")
        else:
            print(" ",end="")
