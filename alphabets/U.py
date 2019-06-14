for r in range(5):
    print("")
    for c in range(4):
        if((c==0 or c==3) and r!=4):
            print("*",end="")
        elif(r==4 and (c==1 or c==2)):
            print("*",end="")
        else:
            print(" ",end="")
