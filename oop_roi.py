class Roi():

    def __init__(self, income, expenses, investments):
        self.income = income
        self.expenses = expenses
        self.investments = investments

    def incomeCalc(self):
        response1 = input('How many units do you have? ')
        sub_response1 =  input('How much do you charge monthly for rent per unit? ')
        self.income.append(((int(response1)) * (int(sub_response1))))
    
    def expensesCalc(self):
        response2 = input("What is your monthly electric bill? ")
        self.expenses.append(int(response2))
        response5 = input("What is your monthly insurance cost? ")
        self.expenses.append(int(response5))
        response6 = input("What is your monthly tax bill? ")
        self.expenses.append(int(response6))
        response7 = input("What is your monthly water bill? ")
        self.expenses.append(int(response7))
        response8 = input("What is your monthly sewer fee? ")
        self.expenses.append(int(response8))
        response9 = input("What is your monthly trash service cost? ")
        self.expenses.append(int(response9))
        response10 = input("What is your monthly gas bill? ")
        self.expenses.append(int(response10))
        response11 = input("What is your monthly HOA fee? ")
        self.expenses.append(int(response11))
        response12 = input("What is your monthly landscaping cost? ")
        self.expenses.append(int(response12))
        response13 = input("What is your monthly vacancy cost? ")
        self.expenses.append(int(response13))
        response14 = input("What is your monthly repairs cost? ")
        self.expenses.append(int(response14))
        response15 = input("What is your monthly capital expenses cost? ")
        self.expenses.append(int(response15))
        response16 = input("What is your monthly mortgage cost? ")
        self.expenses.append(int(response16))
        response17 = input("What is your monthly property management cost? ")
        self.expenses.append(int(response17))
    
    def cashFlow(self):
        cash_flow = sum(self.income) - sum(self.expenses)
        print(f"Your investments cashflow per month is {cash_flow}, yearly is {cash_flow * 12}")
    
    def cashOnCash(self):
        response3 = input("How much was your down payment? ")
        response4 = input("How much have you spent on your property for repairs, renreovations, etc.? ")
        response19 = input("How much was your closing cost?")
        self.investments.append(int(response3) + int(response4) + int(response19))
        cash_on_cash = ((((sum(self.income)) - (sum(self.expenses))) * 12) / sum(self.investments)) * 100
        cash_on_cash = round(cash_on_cash, 2)
        print(f'Your annual cash on cash ROI is {cash_on_cash}%')

    



roi_calc = Roi([],[],[])

def run():
    response = input("Would you like to calculate your ROI for your investments?")
    if response == "yes":
        roi_calc.incomeCalc()
        roi_calc.expensesCalc()
        roi_calc.cashFlow()
        roi_calc.cashOnCash()
    else:
        print("Try buying some properties and come back to try our calculator!")
    
    


run()
