class Estudiante:
    def __init__(self, nombres, apellidos , carrera, año, promedio):
        self.nombres = nombres
        self.apellidos = apellidos
        self.carrera = carrera
        self.año = año
        self.promedio = promedio
    
    def __str__(self):
        return f"Nombre: {self.nombres}\nPrecio: {self.apellidos}\nExistencia: {self.carrera}\nAño: {self.año}\nPromedio: {self.promedio}"