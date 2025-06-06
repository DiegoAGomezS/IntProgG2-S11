#Calcular el area de un círculo
"""Formula del área = PI * (r * r)"""
PI = 3.14

def cal_area_circulo(r):
    return PI * (r ** 2)

def main():
    radio = float(input("Ingrese el radio de la circunferencia: "))
    area = cal_area_circulo(radio)
    print(f"El circulo con radio {radio} tiene un área de: {area}")

main()