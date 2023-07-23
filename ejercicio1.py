### Primer ejercicio ###

# primera parte

def suma(num1, num2, num3):
    resultado = num1 + num2 + num3
    print(resultado)

suma(1, 2, 3)


# segunda parte

class coche:
    def __init__(self, puertas):
        self.puertas = puertas

def inc_puertas(nuevaPuerta):
    miCoche.puertas = miCoche.puertas + nuevaPuerta

miCoche = coche(2)

inc_puertas(0)

print(miCoche.puertas)