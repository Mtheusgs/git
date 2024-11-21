from usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nome=None, email=None, senha=None):
        super().__init__(nome, email, senha)

    def entrar_em_contato(self):
        print(f"O e-mail para contato do usuário é {self.email}")

    def cliente_interface(self, catalogo, users):
        while True:
            print("\n=== Cliente Menu ===")
            print("1. Ver Imóveis Disponíveis")
            print("2. Suporte")
            print("3. Sair")
            choice = input("Escolha uma opção: ")

            if choice == "1":
                print("\nImóveis disponíveis:")
                catalogo.exibir_imoveis()

            elif choice == "2":
                print("Corretores: \n")
                for user in users:
                    if type(user).__name__ == "Corretor":
                        print(f"Nome: {user.nome}, E-mail: {user.email}, CRECI: {user.creci_num}.\n")

            elif choice == "3":
                print("Saindo da interface Cliente.")
                break

            else:
                print("Opção inválida. Tente novamente.")