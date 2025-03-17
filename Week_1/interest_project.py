print("INTEREST CALCULATOR \nChoose the number you wish to calculate \n1. Simple Interest \n2. Compound Interest \n3. Annuity")
choice = int(input( ))

if (choice == 1) :
    print("You chose Simple Interest")
    p = int(input( "Enter the Principal (in Naira):   "))
    t = int(input( "Enter the Time (in years):   "))
    r = int(input( "Enter the Rate (in percentage):   "))
    a = p * (1 + ((r/100)*t))
    print("The Amount of Simple Interest:   ", a)

elif (choice == 2) :
    print("You chose Compound Interest")
    p = int(input( "Enter the Principal (in Naira):   "))
    t = int(input( "Enter the Time (in years):   "))
    r = int(input( "Enter the Rate (in percentage):   "))
    n = int(input( "Enter the number of times interest is compounded per year:   "))
    a = p * (1 + ((r/100)/n)) ** (n * t)
    print("The Amount of Compound Interest:   ", a)

elif (choice == 3) :
    print("You chose Annuity")
    p = int( input("Enter your Periodic payment (in Naira):   "))
    t = int(input( "Enter the Time (in years):   "))
    r = int(input( "Enter the Rate (in percentage):   "))
    n = int(input( "Enter the number of times interest is compounded per year:   "))
    a = p * ( (((1 + ((r/100)/n)) ** (n * t)) - 1) / ((r/100)/n))
    print("The Amount of Annuity:   ", a)

else :
    print("Invalid input. Please choose either [1], [2], and [3]")

print("Thank you for using the Interest Calculator")
    