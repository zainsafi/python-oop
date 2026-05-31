class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def deposit(self,amount,description = ''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def get_balance(self):
        total_balance = 0
        for item in self.ledger:
            total_balance += item['amount']
        return total_balance
    
    def check_funds(self,amount):
        return self.get_balance() >= amount

    def withdraw(self,amount,description = ''):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
            return True
        return False


    
    def transfer(self,amount,other_category):
        if self.check_funds(amount):

            # withdraw from current category
            self.ledger.append({
                'amount': -amount,
                'description': f"Transfer to {other_category.name}"
            })

            # deposit into other category
            other_category.ledger.append({
                'amount': amount,
                'description': f"Transfer from {self.name}"
            })

            return True
        return False
    
    def __str__(self):
        result = (f"{self.name:*^30}\n")
        for item in self.ledger:
            description = item['description'][:23]
            amount = item['amount']
            result += (
                f"{description:<23}"
                f"{amount:>7.2f}\n"
            )
        result += f"Total: {self.get_balance()}"
        return result
    


def create_spend_chart(categories):
    bar_chart = f'Percentage spent by category\n'

    spending = []
    total_spent = 0

    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += -item['amount']
        spending.append(spent)
        total_spent += spent
    
    percentages = []

    for spent in spending:
        percentage = int((spent/total_spent) * 100)
        percentages.append((percentage // 10) * 10)

    for percent in range(100,-1,-10):
        bar_chart += f"{percent:>3}|"
    
        for p in percentages:
            
            if p >= percent:
                bar_chart += ' o '
            else:
                bar_chart += '   '
        bar_chart += ' \n'
    bar_chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [category.name for category in categories]
    max_length = max(len(name) for name in names)
    
    for i in range(max_length):
        bar_chart += "     "
        for name in names:
            if i < len(name):
                bar_chart += name[i] + '  '
            else: 
                bar_chart += '   '
        bar_chart += '\n'

    return bar_chart.rstrip('\n')




food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

auto = Category("Auto")
auto.deposit(1000)
auto.withdraw(200)

print(food)
print()
print(create_spend_chart([food, clothing, auto]))
