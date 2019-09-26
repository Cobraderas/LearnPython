# class X:
#
#     def __init__(self, number):
#         self.number = number
#         print("init x")
#
#     def print(self):
#         print("x")
#
#
# class X1(X):
#
#     def __init__(self, number, mstr):
#         X.__init__(self, number)
#         self.string = mstr
#         print("init x1")
#
#     def print(self):
#         print("x1")
#
#
# class X2(X):
#
#     def __init__(self, number):
#         X.__init__(self, number)
#         print("init x2")
#
#     def print(self):
#         print("x2")
#
#
# class DXX(X2, X1):
#     def __init__(self, number, mstr):
#         X2.__init__(self, number)
#         X1.__init__(self, number, mstr)
#         print("init DXX")
#
#     def print(self):
#         print(str(self.number), self.string)
#
#
# dxx = DXX(123, "XX")
# dxx.print()

# ======================================================================================================================

# http://pythontutor.com/visualize.html#mode=display

# ======================================================================================================================


# class Product:
#     def __init__(self, p_name, p_price):
#         self.product_name = p_name
#         self.product_price = p_price
#
#
# class Client:
#     def __init__(self, c_name, c_address):
#         self.client_name = c_name
#         self.client_address = c_address
#
#
# class Order:
#     def __init__(self):
#         self.client = None
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def add_client(self, client):
#         self.client = client
#
#     def print_invoice(self):
#         invoice = []
#         if self.products and self.client:
#             invoice.append(self.client.client_name)
#             invoice.append(self.client.client_address)
#             for product in self.products:
#                 invoice.append(product.product_name + " " + str(product.product_price))
#             else:
#                 print("Please add client and products")
#             for line in invoice:
#                 print(line)
#
#
# order = Order()
# order.add_client(Client("Gigi", "Hunedoara"))
# order.add_product(Product("TV", 5999))
# order.add_product(Product("Sound Bar", 1499))
# order.add_product(Product("Colac WC", 299))
# order.print_invoice()


# ======================================================================================================================

# MIXINS

class MailMixin:
    auth = False

    def get_last_mail(self):
        if self.auth:
            return "mail xxx"
        else:
            return "not authenticated"


class AuthMixin:
    def authenticate(self, username, password):
        if username == "Gigi" and password == "pass":
            self.auth = True


class MailClient(MailMixin, AuthMixin):
    pass


mc = MailClient()
mc.authenticate("Gigil", "pass")
mails = mc.get_last_mail()
print(mails)




class Z:

    nnumber = 0

    def __init__(self, number):
        self.number = number

    def sum(self, new_number):
        return self.number + new_number

    @staticmethod
    def sum2(number_1, number_2):
        return number_1 + number_2

    @classmethod
    def sum3(cls, number):
        cls.nnumber = number


# print(Z.sum2(1, 2))
z1 = Z(1)
z2 = Z(2)
print(z1.nnumber)
print(z2.nnumber)
z1.sum3(3)
print(z2.nnumber)


