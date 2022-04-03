import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dam2021",
    port="3306",
    database="ecommerce"
)

mycursor = db.cursor()

print('\t\t\033[4m' + "PROGRAMA GESTIÓN DE PRODUCTOS\n" + '\033[0m')
print("\t\t\tMenú de Opciones")
print("\t\t\t================")

def menu():
    print("\n\t\t1) Consulta de un producto")
    print("\t\t2) Consulta de todos los productos")
    print("\t\t3) Inserción de un producto")
    print("\t\t4) Actualización de un producto")
    print("\t\t5) Borrado de un producto")
    print("\t\t6) Salir\n")

def main():
    opcion = 0
    while opcion != 6:
        menu()
        print("\t\t\t\tOpción: ", end="")
        opcion = int(input())
        if opcion == 1:
            Consulta()
        if opcion == 2:
            Consulta2()
        if opcion == 3:
            Insertar()
        if opcion == 4:
            Actualizar()
        if opcion == 5:
            Borrar()

def Consulta():
    print("\n\tIntroduce el id del producto a consultar: ", end="")
    producto = input()
    print("\n\tEncontrado: ")
    mycursor.execute("SELECT * FROM Productos WHERE id=" + producto)

    objeto = mycursor.fetchone()
    print("\tID: ", objeto[0])
    print("\tProducto: ", objeto[1])
    print("\tCódigo de barras:", objeto[2])
    print("\tCantidad: ", objeto[3])
    print("\tPrecio: ", objeto[4])

def Consulta2():
    print("\n\tProductos en base de datos: Producto", end="")
    mycursor.execute("SELECT * FROM Productos")

    print(mycursor.fetchall())

def Insertar():
    salir = True
    i = 0
    while salir == True:
        i = i + 1
        print("\n\tIntroduce el nombre de producto: ", end="")
        nombre = input()
        print("\tIntroduce el código de barras de producto: ", end="")
        cod_barras = input()
        print("\tIntroduce la cantidad de producto: ", end="")
        cantidad = input()
        print("\tIntroduce el precio del producto: ", end="")
        precio = input()
        mycursor.execute("SELECT * FROM Productos")
        last_id = len(mycursor.fetchall())
        last_id = last_id + 1
        elementos = (last_id, nombre, cod_barras, cantidad, precio)
        sql = "INSERT INTO Productos (id, nombre, codigoBarra, cantidad, precio) VALUES (%s, '%s', '%s', %s, %s)"%elementos
        mycursor.execute(sql)
        db.commit()
        print("\n\t¿Quiere introducir otro producto? (S/N) ", end="")
        respuesta = input()
        if respuesta == "N":
            salir = False
    if i == 1:
        print("\n\t1 producto insertado en la base de datos.")
    else:
        print("\n\t", i, "productos insertados en la base de datos.")

def Actualizar():
    salir = True
    i = 0
    while salir == True:
        i = i + 1
        print("\n\tIntroduce el id de producto: ", end="")
        id = input()
        print("\n\tIntroduce el nombre de producto: ", end="")
        nombre = input()
        print("\tIntroduce el código de barras de producto: ", end="")
        cod_barras = input()
        print("\tIntroduce la cantidad de producto: ", end="")
        cantidad = input()
        print("\tIntroduce el precio del producto: ", end="")
        precio = input()
        mycursor.execute(f"UPDATE Productos SET nombre = '{nombre}', codigoBarra = '{cod_barras}', cantidad = '{cantidad}', precio = '{precio}'  WHERE id = '{id}'")
        db.commit()
        print("\n\t¿Quiere modificar otro producto? (S/N) ", end="")
        respuesta = input()
        if respuesta == "N":
            salir = False
    if i == 1:
        print("\n\t1 producto actualizado en la base de datos.")
    else:
        print("\n\t", i, "productos actualizados en la base de datos.")

def Borrar():
    salir = True
    i = 0
    while salir == True:
        i = i + 1
        print("\n\tIntroduce el id de producto: ", end="")
        id = input()
        mycursor.execute("DELETE FROM Productos WHERE id=" + id)
        db.commit()
        print("\n\t¿Quiere borrar otro producto? (S/N) ", end="")
        respuesta = input()
        if respuesta == "N":
            salir = False
    if i == 1:
        print("\n\t1 producto borrado en la base de datos.")
    else:
        print("\n\t", i, "productos borrados en la base de datos.")

main()