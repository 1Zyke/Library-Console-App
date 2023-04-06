import csv

class Libro:
    def __init__(self, codigo, titulo, autor, estado):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.estado = estado


class Biblioteca:
    def __init__(self):
        self.libros = []

    def cargar_libros(self):
        with open('libros.csv.txt', 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                codigo, titulo, autor, estado = fila
                libro = Libro(codigo, titulo, autor, estado)
                self.libros.append(libro)

    def guardar_libros(self):
        with open('libros.csv', 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            for libro in self.libros:
                fila = [libro.codigo, libro.titulo, libro.autor, libro.estado]
                escritor_csv.writerow(fila)

    def agregar_libro(self, libro):
        self.libros.append(libro)
        self.guardar_libros()

    def buscar_libro_opcion(self):
        codigo = input("Ingrese el código del libro: ")
        libro = self.buscar_libro(codigo)
        if libro:
            if libro.estado == "en sala":
                print("¡Alerta! El libro ha salido de la biblioteca sin haber sido prestado.")
            elif libro.estado == "prestado":
                print("El libro ya ha sido prestado.")
            else:
                print("El libro está disponible para ser prestado.")
        else:
            print("No se encontró ningún libro con ese código.")


    def buscar_libro(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                return libro
        return None

    def modificar_libro(self, codigo, titulo, autor, estado):
        libro = self.buscar_libro(codigo)
        if libro:
            libro.titulo = titulo
            libro.autor = autor
            libro.estado = estado
            self.guardar_libros()

    def eliminar_libro(self, codigo):
        libro = self.buscar_libro(codigo)
        if libro:
            self.libros.remove(libro)
            self.guardar_libros()

    def mostrar_libros(self):
        for libro in self.libros:
            print(f"Código: {libro.codigo}, Título: {libro.titulo}, Autor: {libro.autor}, Estado: {libro.estado}")

    def eliminar_libro(self, codigo):
        libro = self.buscar_libro(codigo)
        if libro:
            self.libros.remove(libro)
            self.guardar_libros()
            print(f"El libro con código {codigo} ha sido eliminado.")
        else:
            print(f"No se encontró ningún libro con el código {codigo}.")

print("Bienvenidos a mi sistema de biblioteca :)")
print(" ")
print("Mi nombre es Lorenzo Hugo Núñez Franco")
print("Matricula 2021-0170")
print("")

biblioteca = Biblioteca()
biblioteca.cargar_libros()

while True:
    print("1- Préstamo de libros")
    print("2- Autoservicio")
    print("3- Salida de libros de biblioteca")
    print("4- Consultar libros")
    print("5- Agregar libros")
    print("6- Eliminar libros")
    print("7- Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        codigo = input("Ingrese el código del libro: ")
        libro = biblioteca.buscar_libro(codigo)
        if libro:
            if libro.estado == "en sala":
                libro.estado = "prestado"
                biblioteca.guardar_libros()
                print("El libro ha sido prestado.")
            else:
                print("El libro ya ha sido prestado.")
        else:
            print("No se encontró ningún libro con ese código.")

    elif opcion == "2":
        codigo = input("Ingrese el código del libro: ")
        libro = biblioteca.buscar_libro(codigo)
        if libro:
            print("1- Préstamo")
            print("2- Renovación")
            print("3- Devolución")
            opcion_autoservicio = input("Ingrese una opción: ")
            if opcion_autoservicio == "1":
                if libro.estado == "en sala":
                    libro.estado = "prestado"
                    biblioteca.guardar_libros()
                    print("El libro ha sido prestado.")
                else:
                    print("El libro ya ha sido prestado.")
            elif opcion_autoservicio == "2":
                if libro.estado == "prestado":
                    libro.estado = "prestado"
                    biblioteca.guardar_libros()
                    print("El libro ha sido renovado.")
                else:
                    print("El libro no puede ser renovado.")
            elif opcion_autoservicio == "3":
                if libro.estado == "prestado":
                    libro.estado = "en sala"
                    biblioteca.guardar_libros()
                    print("El libro ha sido devuelto.")
                else:
                    print("El libro no puede ser devuelto.")
        else:
            print("No se encontró ningún libro con ese código.")

    elif opcion == "3":
        libro = biblioteca.buscar_libro_opcion()
        

    elif opcion == "4":
        biblioteca.mostrar_libros()

    elif opcion == "5":
        print("Agregar nuevo libro")
        titulo = input("Título del libro: ")
        autor = input("Autor del libro: ")
        codigo = input("Código del libro: ")
        estado = "en sala"
        libro = Libro(codigo, titulo, autor, estado)
        biblioteca.agregar_libro(libro)
        print("Libro agregado con éxito.")


    elif opcion == "6":
        codigo = input("Ingrese el codigo del libro que desea eliminar: ")
        biblioteca.eliminar_libro(codigo)

    elif opcion == "7":
        break

    else:
        print("Opción inválida.")



