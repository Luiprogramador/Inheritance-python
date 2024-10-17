from Classes import *
if __name__ == '__main__':
    veiculo1 = Veiculo("kawasaki", "ninja ZX-4R", 2024)

    # mostrando os dados do veiculo
    print("Dados do Veículo:")
    veiculo1.mostra_dados()

    # usando os metodos setters para trocar os dados do veículo
    print("\nAlterando dados do Veículo...")
    veiculo1.set_marca("BMW")
    veiculo1.set_modelo("Gs 1200")
    veiculo1.set_ano(2008)
    veiculo1.set_quilometragem(17446)

    # Mostrando dados atualizados
    print("\nDados do Veículo Atualizados:")
    veiculo1.mostra_dados()

    carro1 = Carro("Honda", "Civic", 2017, 0, 4, "vermelho", 18)

    # Exibindo os dados do carro 1
    print("\nDados do Carro 1:")
    carro1.mostra_dados()

    # Usando os métodos setters do carro 1
    print("\nAlterando dados do Carro 1...")
    carro1.set_marca("Chevrolet")
    carro1.set_modelo("Camaro")
    carro1.set_ano(2021)
    carro1.set_quilometragem(15000)
    carro1.set_portas(2)
    carro1.set_cor("amarelo")
    carro1.set_aro(19)

    # Exibindo os dados atualizados do carro 1
    print("\nDados do Carro 1 Atualizados:")
    carro1.mostra_dados()

    carro2 = Carro("Bugatti", "Chiron", 2016, 0, 2, "azul", 19)

    # Exibindo os dados do carro 2
    print("\nDados do Carro 2:")
    carro2.mostra_dados()

    # Usando os métodos setters do carro 2
    print("\nAlterando dados do Carro 2...")
    carro2.set_marca("lamborghini")
    carro2.set_modelo("aventador")
    carro2.set_ano(2014)
    carro2.set_quilometragem(14200)
    carro2.set_portas(2)
    carro2.set_cor("Cinza")
    carro2.set_aro(17)

    # Exibindo os dados atualizados do carro 2
    print("\nDados do Carro 2 Atualizados:")
    carro2.mostra_dados()
