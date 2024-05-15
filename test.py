''' En este algoritmo se administra el stock de una tienda '''
import os

productos={'escoba':5, 'huevos':25,'leche':9}
menup=['Ver stock de productos','Añadir nuevo producto','Ajustar stock','Eliminar producto','Salir']

while True:
    print('***************************************\n********Administracion de stock********\n***************************************')
    for ind, opt in enumerate(menup):
        print(f'{ind+1}.{opt}')
    ans = input('¿Que quieres hacer?\n')
    if ans =='1':
        os.system('cls')
        for llave, valor in productos.items():
            print(f'{llave} {valor}')
    elif ans =='2':
        while True:
            os.system('cls')
            nom = input(str('Ingresa el nombre del nuevo producto:\n'))
            if nom.replace(' ','').isalpha():
                break
        if nom.lower() in productos:
            print('Error el producto ya existe')
        else:
            productos[nom.lower()] = 0
            print('Producto agregado exitosamente')
    elif ans =='3':
        while True:
            os.system('cls')
            nom = input(str('Ingresa el nombre del producto a ajustar stock:\n'))
            if nom.replace(' ','').isalpha():
                break
        if nom.lower() in productos:
            os.system('cls')
            num = input('Ingresa el nuevo valor de stock:\n')
            productos.update({nom:num})
            print('Stock cambiado exitosamente')
        else:
            os.system('cls')
            print('Error el producto no existe')
    elif ans =='4':
        while True:
            os.system('cls')
            nom = input(str('Ingresa el nombre del producto a eliminar:\n'))
            if nom.replace(' ','').isalpha():
                break
        if nom.lower() in productos:
            del productos[nom.lower()]
            print('Producto eliminado exitosamente')
        else:
            os.system('cls')
            print('Error el producto no existe')
    elif ans =='5':
        os.system('cls')
        exit('Adios, nos vemos!')
    else:
        os.system('cls')
        print('Error: ingresa una opcion valida')
