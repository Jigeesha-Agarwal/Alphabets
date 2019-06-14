for r in range(6):
    print("")
    for c in range(4):
        if (c==0 or ((r==0 or r==3) and(c==1 or c==2))):
            print("*",end="")
        elif((r==1 or r==2 )and (c==0 or c==3)):
            print("*",end="")
        else:
            print(" ",end="")
