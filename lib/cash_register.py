#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0, total=0, items=[], last_item=0):
        self.discount = discount
        self.total = total
        self.items = []
        self.last_item = last_item

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.quantity = quantity
        while quantity > 0:
            self.items.append(title)
            quantity -= 1
        self.last_item = price * self.quantity

    def apply_discount(self, discount=20):
        if self.discount > 0:
            self.total *= 1 - (discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_item
        self.items.pop()
