from Estrella import Estrella
from Galaxia import imprimir_informacion, calcular_y_mostrar_distancias

def main():
    Estrella_A = Estrella("Estrella A", 2, 3, 1)
    Estrella_B = Estrella("Estrella B", 4, 4, 4)
    Estrella_C = Estrella("Estrella C", -3, -1, 0)

    imprimir_informacion(Estrella_A)
    imprimir_informacion(Estrella_B)
    imprimir_informacion(Estrella_C)

    calcular_y_mostrar_distancias(Estrella_A, Estrella_B)
    calcular_y_mostrar_distancias(Estrella_B, Estrella_C)
    calcular_y_mostrar_distancias(Estrella_A, Estrella_C)

    origen = Estrella("Origen")
    Estrellas = [Estrella_A, Estrella_B, Estrella_C]
    Estrella_mas_lejana = max(Estrellas, key=lambda Estrella: Estrella.distancia(origen))
    print(f"La Estrella más lejana del origen es {Estrella_mas_lejana.nombre} con una distancia de {Estrella_mas_lejana.distancia(origen):.2f}")

if __name__ == "__main__":
    main()
