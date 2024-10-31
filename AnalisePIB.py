import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'AnalisePIB.xlsx'
xls = pd.ExcelFile(file_path)
df_valores_correntes = pd.read_excel(xls, sheet_name='Valores Correntes', skiprows=3)

print("Primeiras linhas do DataFrame:")
print(df_valores_correntes.head())

print("\nInformações sobre o DataFrame:")
df_valores_correntes.info()

print("\nEstatísticas Descritivas:")
print(df_valores_correntes.describe())


missing_values = df_valores_correntes.isnull().sum()
print("\nValores Ausentes por Coluna:")
print(missing_values[missing_values > 0])

import matplotlib.pyplot as plt


periodos = df_valores_correntes['Período']
agropecuaria = df_valores_correntes['AGROPECUÁRIA']

# Plotar o gráfico com os períodos como strings no eixo x
plt.plot(range(len(periodos)), agropecuaria, marker='o')
plt.title('Variação da Agropecuária ao Longo do Tempo')
plt.xlabel('Período')
plt.ylabel('Agropecuária (1.000.000 R$)')

# Configurando os valores do eixo x como strings e rotacionando
plt.xticks(ticks=range(len(periodos)), labels=periodos, rotation=45, ha='right') 
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(nbins=10))
plt.tight_layout()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

# Selecionar dados específicos para "Total" e "Total.1"
Industria = df_valores_correntes['Total']
Serviços = df_valores_correntes['Total.1']

periodos = df_valores_correntes['Período']

# Plotar o gráfico com os períodos como strings no eixo x
plt.plot(range(len(periodos)), Industria, marker='o')
plt.title('Variação da Taxa acumulada na Industria ao Longo do Tempo')
plt.xlabel('Período')
plt.ylabel('Industria (1.000.000 R$)')


plt.xticks(ticks=range(len(periodos)), labels=periodos, rotation=45, ha='right') 
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(nbins=10))
plt.tight_layout()
plt.grid(True)
plt.show()

Servicos = df_valores_correntes['Total.1']

periodos = df_valores_correntes['Período']


plt.plot(range(len(periodos)), Servicos, marker='o')
plt.title('Variação da Taxa acumulada na Serviços ao Longo do Tempo')
plt.xlabel('Período')
plt.ylabel('Industria (1.000.000 R$)')

plt.xticks(ticks=range(len(periodos)), labels=periodos, rotation=45, ha='right') 
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(nbins=10))
plt.tight_layout()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_valores_correntes_renomeado = df_valores_correntes.rename(columns={
    
    'Total': 'Serviços',
    'Total.1': 'Indústria'
})

numerical_df = df_valores_correntes_renomeado.select_dtypes(include=[float, int])

# Calcular a matriz de correlação
correlation_matrix = numerical_df.corr()
print("\nMatriz de Correlação:")
print(correlation_matrix)

# Plotar o heatmap da matriz de correlação
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Mapa de Calor da Correlação entre Variáveis')
plt.show()

# Selecionar variáveis para o histograma
variaveis = ['AGROPECUÁRIA', 'Serviços', 'Indústria', 'Imposto']

# Plotar histograma das variáveis selecionadas
df_valores_correntes_renomeado[variaveis].hist(bins=15, figsize=(10, 8), layout=(2, 2), edgecolor='black')
plt.suptitle('Distribuição de Variáveis Selecionadas')
plt.show()
