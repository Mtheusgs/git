
class Endereco():
    def __init__(self, rua:str, numero:int, cep:str):
        self.rua = rua
        self.numero = numero
        self.cep = cep

class Imovel:
    def __init__(self, endereco:Endereco,tamanho:int,valor:float,status:bool,garagem:bool,comodos:int,mobiliado:bool,descricao = None):
        self.endereco=endereco
        self.tamanho=tamanho
        self.valor=valor
        self.status=status
        self.garagem=garagem
        self.comodos=comodos
        self.mobiliado=mobiliado
        self.descricao=descricao

    def exibir_no_mapa(self):
        print(f"Mostrando link :  {self.endereco}")

    def fotos(self):
        print(f"Mostre fotos do {self.endereco}")

    def __str__(self):
        return f"Imovél em Rua {self.endereco.rua}, Nº{self.endereco.numero}, Tamanho: {self.tamanho} m^2, Preço: {self.valor}"
    
 
