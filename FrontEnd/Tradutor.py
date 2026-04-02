from translate import Translator
import Request as RQ

def Traduzir_texto(texto):
    # configura do inglês para o portugês
    Tradutor = Translator(from_lang="en", to_lang="pt")
    return Tradutor.translate(texto)