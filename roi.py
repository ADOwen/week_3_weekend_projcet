class roiCalculator():

    def __init__(self, total_income=0, total_expenses=0, investment_total=0):
        self.income = {}
        self.expenses = {}
        self.investments = {}
        self.total_income = total_income
        self.total_expenses = total_expenses
        self.investment_total = investment_total

    def getIncome(self):
        source_income = input("\nPlease enter a source of income: ")
        monthly_income = int(
            input("\nHow much will you recieve from this per month? : "))
        self.income[source_income.title().strip()] = monthly_income
        add_more = input(
            "\nWould you like to add another source of income? 'yes' or 'no' ")
        if add_more.lower().strip() == 'yes':
            self.getIncome()
        elif add_more.lower().strip() == 'no':
            if self.income:
                self.values = self.income.values()
                self.total_income = sum(self.values)
                print(f"\nYour total monthly income is ${self.total_income} ")
            else:
                pass
        else:
            print("Not a valid response please re-enter")

    def getExpenses(self):
        source_expense = input("\nPlease enter an expense: ")
        monthly_expense = int(
            input("\nHow much will this cost you per month? : "))
        self.expenses[source_expense.title().strip()] = monthly_expense
        add_more = input(
            "\nWould you like to add another expense? 'yes' or 'no' ")
        if add_more.lower().strip() == 'yes':
            self.getExpenses()
        elif add_more.lower().strip() == 'no':
            if self.expenses:
                self.expense_values = self.expenses.values()
                self.total_expenses = sum(self.expense_values)
                print(
                    f"\nYour total monthly expense are ${self.total_expenses} ")
            else:
                pass

    def getInvestment(self):
        source_investment = input(
            "\nPlease enter source of investment(eg. your down payment or rennovation): ")
        cost = int(input("\nHow much did this cost you? "))
        self.investments[source_investment.strip().title()] = cost
        add_more = input(
            "\nWould you like to add another investment? 'yes' or 'no' ")
        if add_more.lower().strip() == 'yes':
            self.getInvestment()
        elif add_more.lower().strip() == 'no':
            self.investment_values = self.investments.values()
            self.investment_total = sum(self.investment_values)
            print(
                f"\nYour total investment is ${self.investment_total}")

    def getRoi(self):
        if self.investments:
            self.cashflow = self.total_income - self.total_expenses
            self.roi = ((self.cashflow * 12) / self.investment_total)*100
            print(f"\nYour total Return on Investment is {float(self.roi)}%")

    def runCalc(self):
        self.active = True
        while self.active:
            main_prompt = input(
                """\nWelcome to RoI Calcutor
======================================================================================
"Please enter 'Income', 'Expenses', or 'Investments' to fill them out respectively
======================================================================================
Once you have each of those sections filled out enter 'Calculate' to recieve your RoI
======================================================================================
You can enter 'Display' or 'Clear' to show or clear your info or 'Quit' to exit:\n """)
            main_prompt = main_prompt.lower().strip()

            if main_prompt == 'income':
                self.getIncome()

            if main_prompt == 'expenses':
                self.getExpenses()

            if main_prompt == 'investments':
                self.getInvestment()

            if main_prompt == 'calculate':
                self.getRoi()

            if main_prompt == 'display':
                print(
                    f"\nIncome: {self.income} \nTotal: {self.total_income} ")
                print(
                    f"\nExpenses: {self.expenses} \nTotal: {self.total_expenses} ")
                print(
                    f"\nInvestments: {self.investments} \nTotal: {self.investment_total} ")

            if main_prompt == 'clear':
                clear = input(
                    "Which would you like to clear? 'Income' , 'Expenses' , or 'Investments'? ")
                clear = clear.lower().strip()
                if clear == 'income':
                    self.income.clear()
                    print("Your Monthly Income has been cleared")
                elif clear == 'expenses':
                    self.expenses.clear()
                    print("\nYour Expenses have been cleared.")
                elif clear == 'investments':
                    self.investments.clear()
                    print("Your Investments have been cleared.")
                else:
                    pass

            if main_prompt == 'quit':
                self.active = False


calculation1 = roiCalculator()

calculation1.runCalc()
