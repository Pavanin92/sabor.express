from models.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('John', 4)
restaurante_praca.receber_avaliacao('Lays', 3)
restaurante_praca.receber_avaliacao('Eva', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()