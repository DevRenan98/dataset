import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('USD_BRL_hist.csv')

df['Data'] = pd.to_datetime(df['Data'], format='%d.%m.%Y')

df = df.sort_values('Data')

print(df.head())

plt.figure(figsize=(10,6))
sns.lineplot(x='Data', y='USD_BRL', data=df)
plt.title('Cotação USD/BRL ao longo do tempo')
plt.xlabel('Data')
plt.ylabel('Cotação USD/BRL')
plt.savefig('grafico_linha.png')
plt.close()

plt.figure(figsize=(8,6))
sns.histplot(df['USD_BRL'], bins=20, kde=True)
plt.title('Distribuição das cotações USD/BRL')
plt.xlabel('Cotação USD/BRL')
plt.ylabel('Frequência')
plt.savefig('histograma.png')
plt.close()

df['Ano'] = df['Data'].dt.year
media_anual = df.groupby('Ano')['USD_BRL'].mean().reset_index()

plt.figure(figsize=(8,6))
sns.barplot(x='Ano', y='USD_BRL', data=media_anual)
plt.title('Média anual da cotação USD/BRL')
plt.xlabel('Ano')
plt.ylabel('Cotação média USD/BRL')
plt.savefig('grafico_barras.png')
plt.close()

print("Gráficos salvos com sucesso!")
