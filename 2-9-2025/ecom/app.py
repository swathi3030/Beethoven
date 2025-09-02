from product_manager import create_product, read_all, read_by_id,update, delete_by_id
from product import Product
def menu():
    message = '''
The menu choices are
1- create Product
2- Read all products
3- Read by id
4- Update
5- Delete
6- Exit
Your choice:
'''
    choice =int(input(message))
    if choice == 1:
        name = input('Name:')
        description = input('Description:')
        category = input('category: ')
        tags=input('Tags: ')
        stock=int(input('Stock: '))
        price = int(input('Price: '))
        id = -1
        product=Product(id, name, description, category, tags, stock, price)
        create_product(product)
        print('Product created sucessfully.')
    elif choice == 2:
        produts = read_all()
        print('Products:')
        for product in produts:
            print(product)
    elif choice == 3:
        id = int(input('ID:'))
        product =read_by_id(id)
        if product == None:
            print('Product not found')
        else:
            print(product)
    elif choice == 4:
        id = int(input('ID:'))
        old_product=read_by_id(id)
        if old_product==None:
            print('Product not found')
        else:
            print(old_product)
            name = input('Name:')
            description = input('Description:')
            category = input('category: ')
            tags=input('Tags')
            stock=int(input('Stock: '))
            price = int(input('Price: '))
            new_product = Product(id, name, description, category, tags, stock, price)
            update(new_product) 
            print('Product updated Sucessfully')  
    elif choice == 5:
        id = int(input('ID:'))
        old_product=read_by_id(id)
        if old_product==None:
            print('Product not found')
        else:
            print(old_product)
            if input('Are you sure to delete?')=='y':
                delete_by_id(id)
                print('Product deleeted sucessfully')
    return choice
def menus():
    choice = menu()
    print('Product Management App')
    while choice != 6:
        choice=menu()
    print('Thank you for using App')
menus()