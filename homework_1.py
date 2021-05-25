# 1. Создайте пользовательский класс для описания товара (предположим, это задел для интернет-магазина). В качестве
# полей товара можете использовать значение цены, описание, габариты товара. Создайте пару экземпляров вашего класса
# и протестируйте их работу. 2. Создайте класс «Покупатель». В качестве полей можете использовать фамилию, имя,
# отчество, мобильный телефон и т. д. 3. Создайте класс «Заказ». Заказ может содержать несколько товаров. Заказ
# должен содержать данные о пользователе, который его осуществил. Реализуйте метод вычисления суммарной стоимости
# заказа. Определите метод __str__() для корректного вывода информации о этом заказе.
from typing import List
# from collections import namedtuple


# Product = namedtuple('Product', ['price', 'description', 'dimensions'])

class Product:
    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f'price: {self.price}, description: {self.description}, dimensions: {self.dimensions}'


class Customer:
    orders = []

    def __init__(self, customer_name, customer_last_name, customer_phone):
        self.customer_name = customer_name
        self.customer_last_name = customer_last_name
        self.customer_phone = customer_phone
        self._id = ' '.join([self.customer_name, self.customer_last_name, self.customer_phone])

    def create_order(self, products: List[Product]):
        order = Order(self)
        for product in products:
            order.add_product(product)
        self.orders.append(order)
        return order

    def __str__(self):
        return f'{self.customer_name} {self.customer_last_name}, phone: {self.customer_phone}'


class Order:
    products = []

    def __init__(self, customer: Customer):
        self._customer = customer

    def add_product(self, product: Product):
        self.products.append(product)

    @property
    def order_sum(self):
        return sum([product.price for product in self.products])

    def __str__(self):
        return f'Customer: {self._customer} ordered: {list(map(str, selected_products))} the whole value is: {self.order_sum}'


first_customer = Customer('Leva', 'Rossum', '0991488099')

selected_products = [Product(1, 'first_product', '20*20*20'), Product(2, 'second_product', '40*40*40')]
selected_order = first_customer.create_order(selected_products)

print(selected_order)
