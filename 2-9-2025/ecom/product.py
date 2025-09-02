#id,name, description, category, tags, stock, price
class Product:
    def __init__(self, id, name, description, category, tags, stock, price):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.tags = tags
        self.stock = stock
        self.price = price
    def __str__(self):
        return f'[id = {self.id}, name = {self.name}, description = {self.description}, category = {self.category}, tags = {self.tags}, stock = {self.stock}, price = {self.price}]'
    def __repr__(self):
        return self.__str__()
'''    
mobile_vivo = Product(1001, 'Vivo Y21', 'Good camera quality. Bad call quality', 'mobile', 'moblile, electronics, smart phone, android phone', 10, 23000)
print(mobile_vivo)

mobile_samsang = Product(id= 1002, description='good good camera. bad service', name='samsang s24 Ultra', category='mobile',tags='electronics,smart phone,android phone', stock=20, price=130000)
print(mobile_samsang)

'''