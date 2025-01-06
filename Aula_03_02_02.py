# Importando a Biblioteca
import pandas as pd

# Criando a Tabela Vendedor
vendedores = [
['Ana','F',28,120],
['Bruno','M',34,150],
['Carlos','M',45,110],
['Diana','F',30,95],
['Eduardo','M',40,130],
['Fernanda','F',29,140],
['Gustavo','M',38,105],
['Helena','F',31,125],
['Igor','M',27,100],
['Juliana','F',33,135],
]
# Criando as Colunas
colunas = ['Nome', 'Sexo', 'Idade','Vendas']

# Criando o DataFrame Vendedor
df_vendedores = pd.DataFrame(vendedores,columns=colunas)

#Realizando os Calculos
soma_vendas = df_vendedores['Vendas'].sum()
media_vendas = df_vendedores['Vendas'].mean()
media_idade = df_vendedores['Idade'].mean()
maior_idade = df_vendedores['Idade'].max()
menor_idade = df_vendedores['Idade'].min()
maior_venda = df_vendedores['Vendas'].max()
menor_venda = df_vendedores['Vendas'].min()
nome_melhor_venda = df_vendedores[df_vendedores['Vendas'] == maior_venda]['Nome']
nome_pior_venda = df_vendedores[df_vendedores['Vendas'] == menor_venda]['Nome']
qtd_feminino = df_vendedores[df_vendedores['Sexo'] == 'F']['Vendas'].sum()
qtd_masculino = df_vendedores[df_vendedores['Sexo'] == 'M']['Vendas'].sum()

#Exibindo o Dataframe

print("\n----Tabela de Vendedores---")
print(df_vendedores)
print("\n----Dados Solicitados---")
print(f"A quantidade total de vendas foi {soma_vendas}")
print(f"A quantidade média de vendas foi {media_vendas}")
print(f"A quantidade média das idades foi {media_idade}")
print(f"A maior idade foi {maior_idade}")
print(f"A menor idade foi {menor_idade}")
print(f"A maior idade foi {maior_idade}")
print(f"A maior idade foi {menor_idade}")
print(f"O (a) Melhor Vendedor(a) é {nome_melhor_venda.values[0]} que vendeu {maior_venda}, sendo o melhor vendedor")
print(f"O (a) Melhor Vendedor(a) é {nome_pior_venda.values[0]} que vendeu {menor_venda}, sendo a pior vendedor")
print(f"A quantidade total de vendas das Vendedoras foi {qtd_feminino}")
print(f"A quantidade total de vendas dos Vendedores foi {qtd_masculino}")