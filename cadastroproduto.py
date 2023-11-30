# Cadastro de Produtos

# Estrutura

Produto = {'Descrição': '','Preço':0.0, 'Quantidade': '', 'Ativo': False, 'Valor total':0.0 }

# Entradas

print('\n\t\t\t -- Cadastro de Produtos -- \n')
Produto['Descrição'] = input('Informe o produto: ')
Produto['Preço'] = float(input('Informe o preço: '))
Produto['Quantidade'] = int(input('Informe a quantodade: '))
if (Produto['Quantidade'] > 0):
    Produto['Ativo'] = True
# Produto['Valor total'] = input('Valor total R$')


# Processamento

# Produto['Valor total R$ ''] = Produto['Preço unitário'] * Produto['Quantidade']

# Saída

print(f'\n\n Descrição ........{Produto["Descrição"]}')
print(f'Preço unitário .......{Produto["Preço"]}')
print("*** Produto disponível ***") if Produto['Ativo'] else print("*** Produto não disponível ***")
print('Valor total .......... R${:.2f}'.format(Produto['Preço'] * Produto['Quantidade']))