print("Welcome to PyMoney")
money = 0
print("Initial Money is", money)
continueOrNot = input("If you want to add or take money, key Y, N to exist \n")
while (continueOrNot == "Y"):
    
    a = input("add or take ? key Y or N\n")

    if(a == "Y"):
        add = input("How much you add ( ex lunch 10 )\n")
        # print(int(add.split(" ",1)[1]))
        # print(add)
        money = money + int(add.split(" ",1)[1])
    if(a == "N"):
        take = input("How much you take ( ex lunch -10 or lunch 10 )\n")
        if(take[0] == "-"):
            take = take.split(" ",1)[1]
            take = int(take.split("-",1)[1])
            money = money - int(take.split(" ",1)[1])
        else:
            take = int(take.split(" ",1)[1])
            money = money - int(take)
            
    print("Current Money is", money)
    continueOrNot = input("If you want to continue to add or take money, key Y\n")