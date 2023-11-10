print("Welcome to PyMoney ! How much money do you have?")
money = input()
print("Initial Money is", money)
continueOrNot = input("If you want to add or take money, key Y, N to exist \n")
while (continueOrNot == "Y"):
    
    a = input("add or take ? key Y or N\n")
    record = []
    if(a == "Y"):
        add = input("How much you add ( ex lunch 10 )\n")
        item = add.split(" ",1)[0]
        itemPrice = int(add.split(" ",1)[1])
        money = money + itemPrice
    if(a == "N"):
        take = input("How much you take ( ex lunch -10 or lunch 10 )\n")
        item = take.split(" ",1)[0]
        take = take.split(" ",1)[1]
        if(take[0] == "-"):
            take = take.split("-",1)[1]
            money = money - int(take)
        else:
            money = money - int(take)
        item = take.split(" ",1)[0]
        itemPrice = int(take.split(" ",1)[1])

    print("Current Money is", money)
    continueOrNot = input("If you want to continue to add or take money, key Y\n")
