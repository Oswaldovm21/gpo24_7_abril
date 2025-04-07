class Cuadrado:
    def __init__(self,lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

lado = int(input("Ingresa el lado: "))
mi_ejemplo = Cuadrado(lado)
r = mi_ejemplo.calcular_area()
print(f'El area es: {r}')