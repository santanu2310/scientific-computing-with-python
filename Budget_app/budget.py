class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
    
    def __str__(self):
        string = self.category.center(30,"*") + "\n"
        for item in self.ledger:
            string += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
        string += f"Total: {self.get_balance():.2f}"
        return string
    
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": float(amount), "description": description})
    
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({"amount": float(-amount), "description": description})
            return True
        else:
            return False
    
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]

        return balance

    def transfer(self, amount, budget_cat):
        if self.check_funds(amount):
            self.withdraw(float(amount),f"Transfer to {budget_cat.category}")
            budget_cat.deposit(float(amount),f"Transfer from {self.category}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True


def create_spend_chart(categories):
    budget_list = []
    total_amount = 0
    for categori in categories:
        amount_spend = 0
        for amount in categori.ledger:
            if amount["amount"]<0:
                amount_spend += -amount["amount"]
        budget_list.append({'category':categori.category, 'amount':round(amount_spend,2)})
        total_amount += amount_spend
    
    #converting to percentage
    for item in budget_list:
        item['spent_percent'] = item['amount']*100/total_amount
        
    print(budget_list)
    #converting to string
    bar_graph = "Percentage spent by category\n"
    y_axis = 10

    while y_axis>-1:
        bar_graph += f"{10*y_axis:>3}|"
        for item in budget_list:
            if item["spent_percent"]>10*y_axis:
                bar_graph +=" o "
            else:
                bar_graph +="   "
        bar_graph +=" "
        bar_graph += '\n'

        y_axis -=1
    
    bar_graph += " "*4 + "-"*len(budget_list)*3 + "-"
    
    max_cat_len = 0
    for item in budget_list:
        if len(item['category']) > max_cat_len:
            max_cat_len = len(item['category'])

    for i in range(max_cat_len):
        bar_graph += "\n    "
        for item in budget_list:
            try:
                paduri = item['category'][i]
            except:
                paduri = " "

            bar_graph += " "+paduri+" "
        bar_graph += " "*1

    return bar_graph