import models.data as d
import dao.funciones as f

data = f.DataDao()

def menu():
    print("""
        1. Agregar Info
        2. Mostrar Info
        6. Salir
        Digite una opción
    """)

def main():
    while(True):
        menu()
        option = input()
        if option == '1':
            nombres = input("Nombres del estudiante: ")
            apellidos = input("Apellidos del estudiante: ")
            carrera = input("Carrera que cursa el estudiante: ")
            año = int(input("Año que cursa el estudiante: "))
            promedio = float(input("Promedio del estudiante: "))
            data = d.Estudiante(nombres, apellidos, carrera, año, promedio)
        elif option == '2':
            print("Información:")
            data.show()
        elif option == '6':
            print("Adios")
            False
            break
        else:
            print("Opción invalidad")