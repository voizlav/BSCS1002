class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if enough_funds := self.balance >= abs(amount):
            self.balance -= abs(amount)
        return enough_funds


class PaymentTerminal:
    def __init__(self):
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        lunch_cost = 2.50
        if payment >= lunch_cost:
            self.funds += lunch_cost
            self.lunches += 1
            payment -= lunch_cost
        return payment

    def eat_special(self, payment: float):
        special_cost = 4.30
        if payment >= special_cost:
            self.funds += special_cost
            self.specials += 1
            payment -= special_cost
        return payment

    def eat_lunch_lunchcard(self, card: LunchCard):
        lunch_cost = 2.50
        if subtract_allowed := card.subtract_from_balance(lunch_cost):
            self.lunches += 1
        return subtract_allowed

    def eat_special_lunchcard(self, card: LunchCard):
        special_cost = 4.30
        if subtract_allowed := card.subtract_from_balance(special_cost):
            self.specials += 1
        return subtract_allowed

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        self.funds += abs(amount)
        card.deposit_money(abs(amount))


if __name__ == "__main__":
    exactum = PaymentTerminal()

    change = exactum.eat_lunch(10)
    print("The change returned was", change)

    change = exactum.eat_lunch(5)
    print("The change returned was", change)

    change = exactum.eat_special(4.3)
    print("The change returned was", change)

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)

    change = exactum.eat_lunch(10)
    print("The change returned was", change)

    card = LunchCard(7)

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_lunch_lunchcard(card)
    print("Payment successful:", result)

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)
