#Zayd Alashini
#888471
##Homework 5 Program Set 1
##This program calculates monthly payment of the loan and the total payment of the loan
##You can also change the loan ammount when prompt


class Loan:
    def __init__(self,_annualRate,_numYears,_ammount,_name):
        self.annualRate = _annualRate
        self.numYears = _numYears
        self.ammount = _ammount
        self.name = _name

    def getInterestRate(self):
        return self.annualRate
    def getYears(self):
        return self.numYears
    def getAmmount(self):
        return self.ammount
    def getName(self):
        return self.name

    def setInterestRate(self, _rate):
        self.nnualrate = _rate
    def setYear(self, _years):
        self.numYears = _years
    def setAmmount(self, _ammount):
        self.ammount = _ammount;
    def setName(self, _name):
        self.name = _name

    def getMonthlyPayment(self):
        monthlyRate = self.annualRate / 1200
        monthlyPayment = self.ammount * monthlyRate /( 1 -( 1 / (1 + monthlyRate)**(self.numYears * 12)))
        return monthlyPayment

    def getTotalPayment(self):
        return self.getMonthlyPayment() * self.numYears * 12

    
        
def main() :
    rate = float(input("Enter annual interest rate: "))
    years = int(input("Enter number of years as an integer: "))
    ammount = float(input("Enter loan ammount: "))
    name = input("Enter a borrower's name: ")

    loan = Loan(rate, years, ammount, name)

    print("The loan is for ", loan.name)

    monthlyPayment = loan.getMonthlyPayment()
    totalPayment = loan.getTotalPayment()
    monthlyPayment = format(monthlyPayment , ",.2f")
    totalPayment = format(totalPayment , ",.2f")
    
    print("The monthly payment is " , monthlyPayment)
    print("The total payment is " , totalPayment)

    newLoan = input("\nDo you want to change loan ammount? y for yes or enter to quit")

    while newLoan == "Y" or newLoan == "y":
        newAmmount = int(input("Enter the new loan amount "))
        loan.setAmmount(newAmmount)

        print("The loan is for ", loan.name)

        monthlyPayment = loan.getMonthlyPayment()
        totalPayment = loan.getTotalPayment()
        monthlyPayment = format(monthlyPayment , ",.2f")
        totalPayment = format(totalPayment , ",.2f")
    
        print("The monthly payment is " , monthlyPayment)
        print("The total payment is " , totalPayment)

        newLoan = input("\nDo you want to change loan ammount? y for yes or enter to quit")


        
                       
if __name__ == "__main__" : 
    main()



##OutPut
##Trest Run 1
##Enter annual interest rate: 2.5
##Enter number of years as an integer: 5
##Enter loan ammount: 1000.00
##Enter a borrower's name: John Jones
##The loan is for  John Jones
##The monthly payment is  17.75
##The total payment is  1,064.84
##
##Do you want to change loan ammount? y for yes or enter to quity
##Enter the new loan amount 5000
##The loan is for  John Jones
##The monthly payment is  88.74
##The total payment is  5,324.21
##
##Do you want to change loan ammount? y for yes or enter to quit
##>>>


##Test Rune 2
##Enter annual interest rate: 6
##Enter number of years as an integer: 6
##Enter loan ammount: 6666
##Enter a borrower's name: Bobby Marks
##The loan is for  Bobby Marks
##The monthly payment is  110.47
##The total payment is  7,954.19
##
##Do you want to change loan ammount? y for yes or enter to quit
##>>> 


##Test Run 3
##Enter annual interest rate: 7
##Enter number of years as an integer: 1
##Enter loan ammount: 10000
##Enter a borrower's name: Kobe Bryant
##The loan is for  Kobe Bryant
##The monthly payment is  865.27
##The total payment is  10,383.21
##
##Do you want to change loan ammount? y for yes or enter to quity
##Enter the new loan amount 1000000
##The loan is for  Kobe Bryant
##The monthly payment is  86,526.75
##The total payment is  1,038,320.95
##
##Do you want to change loan ammount? y for yes or enter to quity
##Enter the new loan amount 5000000
##The loan is for  Kobe Bryant
##The monthly payment is  432,633.73
##The total payment is  5,191,604.77
##
##Do you want to change loan ammount? y for yes or enter to quit    


##Test Run 4
##Enter annual interest rate: 3
##Enter number of years as an integer: 10
##Enter loan ammount: 100
##Enter a borrower's name: Zayd Alashini
##The loan is for  Zayd Alashini
##The monthly payment is  0.97
##The total payment is  115.87
##
##Do you want to change loan ammount? y for yes or enter to quity
##Enter the new loan amount 50
##The loan is for  Zayd Alashini
##The monthly payment is  0.48
##The total payment is  57.94
##
##Do you want to change loan ammount? y for yes or enter to quity
##Enter the new loan amount 600
##The loan is for  Zayd Alashini
##The monthly payment is  5.79
##The total payment is  695.24
##
##Do you want to change loan ammount? y for yes or enter to quity
##Enter the new loan amount 1000000000
##The loan is for  Zayd Alashini
##The monthly payment is  9,656,074.47
##The total payment is  1,158,728,936.38
##
##Do you want to change loan ammount? y for yes or enter to quit
##>>>


##Test Run 5
##Enter annual interest rate: 1000
##Enter number of years as an integer: 1
##Enter loan ammount: 1000
##Enter a borrower's name: Lucky Manchester
##The loan is for  Lucky Manchester
##The monthly payment is  833.91
##The total payment is  10,006.94
##
##Do you want to change loan ammount? y for yes or enter to quit
##>>> 
