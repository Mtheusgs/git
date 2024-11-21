import csv
from cliente import Cliente
from corretor import Corretor
from imovel import Imovel, Endereco

class UserPersistence:
    @staticmethod
    def save_to_csv(users, properties, file_path):
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["type", "nome", "email", "senha", "creci_num", 
                             "rua", "numero", "cep", "tamanho", "valor", 
                             "status", "garagem", "comodos", "mobiliado", "descricao"])
            
            for user in users:
                if isinstance(user, Cliente):
                    writer.writerow(["Cliente", user.nome, user.email, user.senha, "", 
                                     "", "", "", "", "", "", "", "", "", ""])
                elif isinstance(user, Corretor):
                    writer.writerow(["Corretor", user.nome, user.email, user.senha, user.creci_num, 
                                     "", "", "", "", "", "", "", "", "", ""])
            for prop in properties:
                writer.writerow(["Imovel", "", "", "", "", 
                                 prop.endereco.rua, prop.endereco.numero, prop.endereco.cep, 
                                 prop.tamanho, prop.valor, prop.status, prop.garagem, 
                                 prop.comodos, prop.mobiliado, prop.descricao])

    @staticmethod
    def load_from_csv(file_path):
        users = []
        properties = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["type"] == "Cliente":
                        user = Cliente(row["nome"], row["email"], row["senha"])
                        users.append(user)
                    elif row["type"] == "Corretor":
                        user = Corretor(row["nome"], row["email"], row["senha"], row["creci_num"])
                        users.append(user)
                    elif row["type"] == "Imovel":
                        endereco = Endereco(row["rua"], int(row["numero"]), row["cep"])
                        prop = Imovel(endereco, int(row["tamanho"]), float(row["valor"]), 
                                      row["status"] == "True", row["garagem"] == "True", 
                                      int(row["comodos"]), row["mobiliado"] == "True", row["descricao"])
                        properties.append(prop)
        except FileNotFoundError:
            print(f"Não existe nenhuma informação em {file_path}. Começando do zero.")
        return users, properties
