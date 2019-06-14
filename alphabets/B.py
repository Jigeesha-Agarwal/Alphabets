for r in range(8):
    print("")
    for c in range(4):
        if((r==1 or r==4 or r==7) and c!=3):
            print("*",end="")
        elif((r==2 or r==3 or r== 5 or r==6 ) and c!=1 and c!=2):
            print("*",end="")
        else:
            print(" ",end="")
            
