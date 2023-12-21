# --------- Inicio das Variáveis Globais ---------- 
lista_colab = []  # Lista para armazenar os colaboradores
id_global = 0  # Variável global para manter o ID único de cada colaborador
# --------- Fim das Variáveis Globais ---------- 

# --------- Inicio de cadastrar colaboradores ---------- 
def cadastrar_colab(id):
    # Função para cadastrar um novo colaborador
    print('-' * 15,'Cadastro de colaboradores', '-' * 15)
    print('ID do colaborador {}'.format(id_global))
    nome = input('Digite o nome do colaborador: '.capitalize())
    setor = input('Digite o setor do colaborador: '.capitalize())
    pagamento = float(input('Digite o valor do pagamento deste colaborador R$: ').replace(",", "."))
    # Cria um dicionário com os dados do colaborador
    dicionario_cadastro = {
        'id'       : id_global,
        'nome'     : nome,
        'setor'    : setor,
        'pagamento': pagamento
    }
    # Adiciona o dicionário à lista de colaboradores
    lista_colab.append(dicionario_cadastro.copy())
# --------- Fim de cadastrar colaboradores -------------

# --------- Inicio de consultar colaboradores ----------
def consultar_colab():
    # Função para consultar os colaboradores
    print('-' * 15,'Consulta de colaboradores', '-' * 15)
    while True:
        op_consultar = input('Escolha a opção desejada: \n'+
                '1 - Consultar todos colaboradores \n'+
                '2 - Consultar por ID \n'+
                '3 - Consultar por setor \n'+
                '4 - Retornar ao Menu principal \n'+
                '>> '
                )
        if op_consultar == '1':
            # Opção para consultar todos os colaboradores
            print('Você escolheu a opção consultar TODOS os colaboradores.')
            print('-' * 15)
            # Itera sobre a lista de colaboradores e imprime os dados de cada um
            for colab in lista_colab:
                for key, value in colab.items(): # Listar todos os itens do dicionário (key and values)
                    print('{}: {}'.format(key, value))
                print('-' * 15)
        elif op_consultar == '2':
            # Opção para consultar por ID
            print('Você escolheu a opção consultar por ID.')
            print('-' * 15)
            # Solicita o ID do colaborador a ser consultado
            id_desejado = int(input('Informe o ID: '))
            # Procura o colaborador com o ID fornecido e imprime seus dados
            for colab in lista_colab:
                if colab['id'] == id_desejado:
                    for key, value in colab.items():
                        print('{}: {}'.format(key, value))
            print('-' * 15)
        elif op_consultar == '3':
            # Opção para consultar por setor
            print('Você escolheu a opção consultar por SETOR.')
            print('-' * 15)
            # Solicita o setor a ser consultado
            setor_desejado = input('Informe o SETOR: ')
            # Procura os colaboradores do setor fornecido e imprime seus dados
            for colab in lista_colab:
                if colab['setor'] == setor_desejado:
                    for key, value in colab.items():
                        print('{}: {}'.format(key, value))
                    print('-' * 15)
        elif op_consultar == '4':
            return
        else:
            print('Opção inválida. Tente novamente.')
            continue

# --------- Fim de consultar colaboradores -------------

# --------- Inicio de remover colaboradores ------------
def remover_colab():
    # Função para remover um colaborador
    print('-' * 15,'Remover colaboradores', '-' * 15)
    while True:
        # Solicita o ID do colaborador a ser removido
        colab_desejado = int(input('Informe o ID do colaborador: '))
        # Procura o colaborador com o ID fornecido e o remove da lista de colaboradores
        for colab in lista_colab:
            if colab['id'] == colab_desejado:
                lista_colab.remove(colab)
