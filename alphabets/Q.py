for r in range(5):
    print("")
    for c in range(5):
        if (r==0 and (c==1 or c==2)):
            print("*",end="")
        elif(r==1 and(c==0 or c==3)):
            print("*",end="")
        elif(r==2 and(c==0 or c==3 or c==2)):
            print("*",end="")
        elif(r==3 and(c==1 or c==3 or c==2)):
            print("*",end="")
        elif(c==4 and r==4):
            print("*",end="")
        else:
            print(" ",end="")
