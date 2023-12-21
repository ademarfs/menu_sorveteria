# Estrutura do Cardápio.
print('Seja bem vindo a sorveteria do Ademar Ferreira')
print('-' * 37, 'CARDÁPIO', '-' * 37)
print('| Nº DE BOLAS  | SABOR TRADICIONAL (tr) | SABOR PREMIUM (pr) | SABOR ESPECIAL (es) |')
print('|' + ' ' * 4 + '1' + ' ' * 5 + '|' + ' ' * 6 + 'R$ 6,00' + ' ' * 7 + '|' + ' ' * 5 + 'R$ 7,00' + ' ' * 4 + '|' + ' ' * 5 + 'R$ 8,00' + ' ' * 5 + '|')
print('|' + ' ' * 4 + '2' + ' ' * 5 + '|' + ' ' * 6 + 'R$ 10,00' + ' ' * 6 + '|' + ' ' * 5 + 'R$ 12,00' + ' ' * 3 + '|' + ' ' * 5 + 'R$ 14,00' + ' ' * 4 + '|')
print('|' + ' ' * 4 + '3' + ' ' * 5 + '|' + ' ' * 6 + 'R$ 14,00' + ' ' * 6 + '|' + ' ' * 5 + 'R$ 17,00' + ' ' * 3 + '|' + ' ' * 5 + 'R$ 20,00' + ' ' * 4 + '|')
print('-' * 84)

# Variável para armazenar o valor total dos pedidos.
total_bolas = 0

# Dicionário definido para os sabores.
nome = {
    'tr': "tradicional",
    'pr': "premium",
    'es': "especial"
}
# Dicionário definido para o preço de cada quantidade de bolas.
valor_sabor = {
    'tr': [6, 10, 14],
    'pr': [7, 12, 17],
    'es': [8, 14, 20]
}

# Loop para as condições.
while True:
    # Bloco para questionar o cliente sobre os sabores.
    sabor = input('Selecione o sabor desejado ou finalize o pedido: (tr) Tradicional / (pr) Premium / (es) Especial / (s) Sair:\n').lower()
    if sabor == 's': # Condição para caso o cliente deseje sair.
        break

# Condições caso o cliente digite comandos diferentes dos solicitados em relação aos sabores.
    if sabor not in ['tr', 'pr', 'es']:
        print('Sabor não encontrado. Tente novamente.')
        continue
# Condições caso o cliente digite comandos diferentes dos solicitados em relação a quantidade de bolas.
    qnt_bolas = input('Informe quantas bolas de sorvete você deseja entre 1 a 3: ')
    if qnt_bolas not in ['1', '2', '3']:
        print('Quantidade inválida. Tente novamente.')
        continue
# Bloco para informar as opções selecionadas e valor.
    qnt_bolas = int(qnt_bolas) # Transformando a variável qnt_bolas de str para int.
    valor = valor_sabor[sabor][qnt_bolas - 1] # Armazenando o sabor e quantidade de bolas em Valor atravé dos dicionários criados.
    print('Você escolheu {} bola(s) do sorvete {}: R$ {:.2f}'.format(qnt_bolas, nome[sabor].capitalize(), valor)) 
    total_bolas += valor # Somando os pedidos e armazenando na variável total_bolas
# Bloco para finalização do pedido ou caso queira continuar.
    finalizando_pedido = input('Deseja algo mais? Digite (c) para continuar ou (s) para sair: ').lower() 
    if finalizando_pedido == 's':
        break
    elif finalizando_pedido != 'c':
        print('Comando inválido. Tente novamente.')
        
print('Valor total: R$ {:.2f}'.format(total_bolas)) # Informando o total dos pedidos.
