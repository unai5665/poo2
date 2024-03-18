class Vehiculo:
    def __init__(self, ruedas, color):
        self.ruedas = ruedas
        self.color = color


mi_auto = Vehiculo(ruedas=4, color="rojo")


print("Número de ruedas:", mi_auto.ruedas)
print("Color:", mi_auto.color)



if __name__ == "__main__":
    seat = Vehiculo(4, "blanco")
    seat.ruedas = 4
    seat = Vehiculo(4, "blanco")
        