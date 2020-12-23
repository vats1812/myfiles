while (True):

    print("\nChoose Your operation")

    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")

    opr = int(input("\n"))

    if (opr != 1) & (opr != 2) & (opr != 3) & (opr != 4):
        print("\nPlease enter Proper value  !!!")
        continue
    print("\nEnter your first number\n")

    a = int(input())

    print("\nEnter your second number\n")

    b = int(input())

    if opr == 1:
        ans = a+b
        if(a == 56) & (b == 9):
            print("\nYour answer is: 77")
        else:
            print("\nYour answer is:", ans)

    elif opr == 2:
        ans = a-b
        print("\nYour answer is:", ans)

    elif opr == 3:
        ans = a*b
        if(a == 45) & (b == 3):
            print("\nYour answer is: 555")
        else:
            print("\nYour answer is:", ans)

    elif opr == 4:
        ans = a/b
        if(a == 56) & (b == 6):
            print("\nYour answer is: 4")
        else:
            print("\nYour answer is:", ans)
    continue       
