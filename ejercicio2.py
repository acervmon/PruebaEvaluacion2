class Dialogo:
    def __init__(self, texto_original):
        self.texto_original = texto_original

    def dividir_frases(self):
        frases = self.texto_original.split("#")
        return frases

    def formatear_frases(self, frases):
        frases_formateadas = [frase.capitalize() + "." for frase in frases]
        frases_formateadas[0] = frases_formateadas[0].replace(".", "...")
        return frases_formateadas

    def unir_dialogo(self, frases_formateadas):
        dialogo_formateado = "\n\n".join(frases_formateadas)
        return dialogo_formateado

    def imprimir_dialogo(self):
        frases = self.dividir_frases()
        frases_formateadas = self.formatear_frases(frases)
        dialogo_formateado = self.unir_dialogo(frases_formateadas)
        print(dialogo_formateado)

def main():
    texto_original = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

    dialogo = Dialogo(texto_original)
    dialogo.imprimir_dialogo()

if __name__ == "__main__":
    main()
