class MagiaNumerica:
    def __init__(self, lista_numeros):
        self.lista_numeros = lista_numeros

    def eliminar_duplicados(self):
        lista_sin_duplicados = list(set(self.lista_numeros))
        return lista_sin_duplicados

    def ordenar_descendente(self, lista):
        lista_ordenada = sorted(lista, reverse=True)
        return lista_ordenada

    def eliminar_impares(self, lista):
        lista_sin_impares = [num for num in lista if num % 2 == 0]
        return lista_sin_impares

    def sumar_numeros(self, lista):
        suma = sum(lista)
        return suma

    def realizar_magia_numerica(self):
        lista_sin_duplicados = self.eliminar_duplicados()
        lista_ordenada = self.ordenar_descendente(lista_sin_duplicados)
        lista_sin_impares = self.eliminar_impares(lista_ordenada)
        suma = self.sumar_numeros(lista_sin_impares)
        lista_final = [suma] + lista_sin_impares
        return lista_final

    def verificar_suma(self, lista):
        return lista[0] == sum(lista[1:])

    def imprimir_lista(self, lista):
        print(lista)

def main():
    lista_numeros = [11, 322, 34, 24, 154, 62, 703, 14, 9312, 20]
    magia = MagiaNumerica(lista_numeros)
    resultado = magia.realizar_magia_numerica()
    magia.imprimir_lista(resultado)
    verificacion = magia.verificar_suma(resultado)
    print(verificacion)

if __name__ == "__main__":
    main()
