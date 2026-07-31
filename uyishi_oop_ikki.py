#--------------------------------- HOMEWORK --------------------------------------

#               1-masala.

# class User:
#     def __init__(self, name, email, address):
#         self.name = name
#         self.email = email
#         self.address = address

#     def get_name(self):
#         return self.name

#     def get_email(self):
#         return self.email

#     def get_address(self):
#         return self.address

#     def set_address(self, new_address):
#         self.address = new_address

#     def __str__(self):
#         return f"User: {self.name} <{self.email}>"

# user = User(
#     "Asadbek",
#     "asad@gmail.com",
#     "Qarshi"
# )

# print(user.get_name())
# print(user.get_email())
# print(user.get_address())

# user.set_address("Toshkent")
# print(user.get_address())
# print(user)




#               2-masala.

class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_address(self):
        return self.address

    def set_address(self, new_address):
        self.address = new_address

    def __str__(self):
        return f"User: {self.name} <{self.email}>"


class Customer(User):
    def __init__(self, name, email, address, balance):
        super().__init__(name, email, address)
        self.cart = []
        self.balance = balance

    def add_to_cart(self, product, qty, price):
        self.cart.append((product, qty, price))

    def clear_cart(self):
        self.cart.clear()

    def get_cart_total(self):
        total = 0

        for product, qty, price in self.cart:
            total += qty * price

        return total

    def checkout(self):
        total = self.get_cart_total()

        if self.balance >= total:
            self.balance -= total
            self.clear_cart()
            return True

        return False

    def __str__(self):
        return f"Customer: {self.name} (balance: {self.balance} so'm)"

customer = Customer(
    "Asadbek",
    "asad@gmail.com",
    "Qarshi",
    300000
)

customer.add_to_cart("Olma", 5, 12000)
customer.add_to_cart("Banan", 2, 18000)

print(customer)

print("Jami:", customer.get_cart_total())

if customer.checkout():
    print("Xarid muvaffaqiyatli!")
else:
    print("Pul yetarli emas!")

print(customer)
print(customer.cart)












