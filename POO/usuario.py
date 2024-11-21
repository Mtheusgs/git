from abc import ABC, abstractmethod

class UsuarioInterface(ABC):
    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def login(self):
        pass


class Usuario(UsuarioInterface):
    def __init__(self, nome=None, email=None, senha=None):
        self.nome = nome
        self.email = email
        self.senha = senha

    def register(self):
        print("=== Registro ===")
        self.nome = input("Insira seu nome: ")
        self.email = input("Insira seu e-mail: ")
        self.senha = input("Crie uma senha: ")
        

    def login(self, email:str, senha:str):
        if self.email == email and self.senha == senha:
            print(f"Bem Vindo de Volta, {self.nome}!")
            return True
        else:
            print("Email ou senha invalido(a).")
            return False
