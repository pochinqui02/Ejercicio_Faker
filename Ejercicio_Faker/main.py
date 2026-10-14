import random
from faker import Faker

NUM_USUARIOS = 15

#Devuelve un dicionario {codigo: datos} con usuarios ficticios.
def crear_usuarios(fake, cantidad=NUM_USUARIOS):
    usuarios = {}
    for codigo in range(1, cantidad + 1):
        usuarios[codigo] = {
            "nome": fake.name(),
            "direccion": fake.address().replace("\n", ", "),
            "correo": fake.email(),
            "telefono": fake.phone_number(),
        }
    return usuarios

#Muestra por pantalla los datos de todos los usuarios.
def mostrar_usuarios(usuarios):
    for codigo, datos in usuarios.items():
        print(f"Usuario {codigo}")
        print(f"  Nome:      {datos['nome']}")
        print(f"  Dirección: {datos['direccion']}")
        print(f"  Correo:    {datos['correo']}")
        print(f"  Teléfono:  {datos['telefono']}")
        print()

def main():
    fake = Faker("es_ES")
    usuarios = crear_usuarios(fake)
    mostrar_usuarios(usuarios)

    codigo_afortunado = random.choice(list(usuarios))
    nome = usuarios[codigo_afortunado]["nome"]
    print(f"O usuario chamado {nome} foi o afortunado!")

if __name__ == "__main__":
    main()
