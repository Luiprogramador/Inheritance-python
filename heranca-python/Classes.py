class Veiculo(object):
    def __init__(self, marca, modelo, ano, quilometragem=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem

    def get_marca(self):
        return self.marca

    def set_marca(self, nova_marca):
        self.marca = nova_marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, novo_modelo:str):
        if not isinstance(novo_modelo, str):
            raise ValueError("O modelo do carro deve ser uma string.")
        if not novo_modelo.strip():
            raise ValueError("O modelo do carro não pode ser vazio.")
        self.modelo = novo_modelo

    def get_ano(self):
        return self.ano

    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def get_quilometragem(self):
        return self.quilometragem

    def set_quilometragem(self, nova_quilometragem):
        self.quilometragem = nova_quilometragem

    def mostra_dados(self):
        dados = self.retorna_dados()
        for chave, valor in dados.items():
            print(f'{chave.title()}: {valor}')

    def retorna_dados(self):
        return { 'marca': self.marca, 'modelo': self.modelo, 'ano': self.ano, 'quilimetragem': self.quilometragem}


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, quilometragem, portas, cor, aro=17):
        super().__init__(marca, modelo, ano, quilometragem)
        self.portas = portas
        self.cor = cor
        self. aro = aro

    def get_portas(self):
        return self.portas

    def set_portas(self,novas_portas):
        self.portas = novas_portas

    def get_cor(self):
        return self.cor

    def set_cor(self, nova_cor):
        self.cor = nova_cor

    def get_aro(self):
        return self.aro

    def set_aro(self,novo_aro):
        if novo_aro not in [17,18,19,22]:
            print('O aro deve ser entre 17,18,19,22')
        else:
            self.aro = novo_aro

    def mostra_dados(self):
        dados = self.retorna_dados()
        for chave, valor in dados.items():
            print(f'{chave.title()}: {valor}')

    def retorna_dados(self):
        return { 'marca': self.marca, 'modelo': self.modelo, 'ano': self.ano, 'quilimetragem': self.quilometragem, 'portas': self.portas, 'cor': self.cor, 'aro': self.aro}






