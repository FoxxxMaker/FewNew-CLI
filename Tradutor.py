from translate import Translator
import Request as RQ

# configura do inglês para o portugês
Tradutor = Translator(from_lang="en", to_lang="pt")

# Armazena em uma variável
tradu = Tradutor.translate(RQ.Atividade)

print(tradu)