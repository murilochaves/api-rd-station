from RDStation.CRM import APIRDStationCRM  # Abstração da Classe
import sys  # Manipulação do sistema

if __name__ == '__main__':
    '''
    Método principal para execução do script.
    '''

    # Verificando se o token foi passado como argumento
    if len(sys.argv) != 2:

        # Exibindo a mensagem de erro
        print("Erro: Token não fornecido.\nUso correto: python main.py <TOKEN>")

        # Encerrando o script
        sys.exit(1)

    # Obtendo o token
    token = sys.argv[1]

    # Instanciando a Classe
    api = APIRDStationCRM(token)

    # Exibindo o token
    print(api.exibir_token())
