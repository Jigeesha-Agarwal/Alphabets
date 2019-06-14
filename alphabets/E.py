for r in range(5):
    print("")
    for c in range(4):
        if(r==0 or r==2 or r==4):
            print("*",end="")
        elif((r==1 or r==3)and c==0 ):
            print("*",end="")
        else:
            print(" ",end="")
