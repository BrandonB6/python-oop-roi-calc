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
        response2 = input("How much are your monthly expenses? ")
        self.expenses.append(int(response2))
    
    def cashFlow(self):
        cash_flow = sum(self.income) - sum(self.expenses)
        print(f"Your investments cashflow per month is {cash_flow}, yearly is {cash_flow * 12}")
    
    def cashOnCash(self):
        response3 = input("How much was your down payment? ")
        response4 = input("How much have you spent on your property for repairs, renovations, etc.? ")
        self.investments.append(int(response3) + int(response4))
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
