import math#maths calculator 

calculation_type =str (input("Choose either 'Investment' or 'bond' to proceed :"))#prompting user to chose eith the bond option or investment


if calculation_type == "Investment":#if the user choses the investment option 
    Amount = float (input ("Enter desired amount to invest :R"))#the first requested information is the amount
    Intrest_rate = float (input("Enter intrest rate to calculate "))#the second requested information is the intrest rate 
    Number_of_years = int (input("Enter numbers of years for loan :"))#the third requested information is number of years user is going to pay 
    type_of_investment = input("Enter weather you want simple or compound intrest :")#last question is the compond or simple intrest option where the user can chose either 

    if type_of_investment == 'simple':#calculation of the simple intrest fomular
        r = Intrest_rate / 100#intrest rate is divided by 100
        A = Amount * (1 + r *  Number_of_years)#Amount is multiplied by 1 plus the rate and multiplied again by the number of years
        print(f'Total amount for the simple interest calculation is R{A}')#output of the calculation for simple intrest
    
    elif type_of_investment == 'compound':#calculation of the compound intrest fomular
        r = Intrest_rate/ 100#variable r initialized to intrest rate thats is divided by 100
        B = Amount * math.pow ((1 + r ),Number_of_years)#amount multiplied by 1 plus rate to the power of the number of years 
        print(f'the amount for the compound in interest calculation is R{B}')#output of the fomular for compound intrest 


elif calculation_type== 'bond':#If the user selects the bond option
    Amount = float (input ("Input the current value of the house :R"))#Requesting the user to input the amount 
    Intrest_rate = int (input ("Enter desired intrest rate :"))#requesting the user to input the intrest rate 
    Months = int (input ("Enter number of months planned for repayment :"))#requesting the user to imput the months of the bond
    r = (Intrest_rate / 100) / 12#rate inputed by the user divided by 12 since we calculating months 
    n = Months#variable n initialized to months
    x = (r * Amount)/(1 - math.pow((1+r),(-n)))#the variable x initializd to the bond calculation fomular
    x = round(x,2)#answer rounded of to two decimals 
    print (f'The bond calculation is R{x}')#output for the bond calculation

    

