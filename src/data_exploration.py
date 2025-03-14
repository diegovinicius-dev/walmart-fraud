import matplotlib.pyplot as plt
import pandas as pd

def explore_order_amount(orders_df):
    """Analisa a distribuição da coluna order_amount."""
    print("\nEstatísticas Descritivas de order_amount:")
    print(orders_df['order_amount'].describe())

    # Histograma de 'order_amount' com melhorias
    plt.figure(figsize=(10, 6))  # Aumenta o tamanho da figura
    plt.style.use('ggplot')  # Adiciona um estilo mais moderno
    plt.hist(orders_df['order_amount'], bins=30, color='skyblue', edgecolor='black')  # Ajusta as cores
    plt.xlim(0, 2000)
    plt.title('Distribuição de Valores de Pedido', fontsize=16)  # Título mais descritivo
    plt.xlabel('Valor do Pedido', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    plt.grid(axis='y', alpha=0.75)  # Adiciona grade no eixo Y
    plt.show()

    # Gráfico de Densidade de 'order_amount'
    plt.figure(figsize=(10, 6))
    orders_df['order_amount'].plot.kde(color='salmon')
    plt.title('Densidade de Valores de Pedido', fontsize=16)
    plt.xlabel('Valor do Pedido', fontsize=12)
    plt.ylabel('Densidade', fontsize=12)
    plt.show()

def explore_items_columns(orders_df):
    """Explora as colunas items_delivered e items_missing."""
    # Estatísticas Descritivas
    print("\nEstatísticas Descritivas de items_delivered:")
    print(orders_df['items_delivered'].describe())

    print("\nEstatísticas Descritivas de items_missing:")
    print(orders_df['items_missing'].describe())

    # Histograma de items_delivered
    plt.figure(figsize=(10, 6))
    plt.style.use('ggplot')
    plt.hist(orders_df['items_delivered'], bins=30, color='skyblue', edgecolor='black')
    plt.title('Distribuição de items_delivered', fontsize=16)
    plt.xlabel('Número de Items Entregues', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    plt.grid(axis='y', alpha=0.75)
    plt.show()

    # Gráfico de Densidade de items_delivered
    plt.figure(figsize=(10, 6))
    orders_df['items_delivered'].plot.kde(color='salmon')
    plt.title('Densidade de items_delivered', fontsize=16)
    plt.xlabel('Número de Items Entregues', fontsize=12)
    plt.ylabel('Densidade', fontsize=12)
    plt.show()

    # Histograma de items_missing
    plt.figure(figsize=(10, 6))
    plt.style.use('ggplot')
    plt.hist(orders_df['items_missing'], bins=30, color='skyblue', edgecolor='black')
    plt.title('Distribuição de items_missing', fontsize=16)
    plt.xlabel('Número de Items Faltantes', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    plt.grid(axis='y', alpha=0.75)
    plt.show()

    # Gráfico de Densidade de items_missing
    plt.figure(figsize=(10, 6))
    orders_df['items_missing'].plot.kde(color='salmon')
    plt.title('Densidade de items_missing', fontsize=16)
    plt.xlabel('Número de Items Faltantes', fontsize=12)
    plt.ylabel('Densidade', fontsize=12)
    plt.show()

def explore_categorical_columns(orders_df):
    """Explora colunas categóricas."""
    # Verificar valores únicos em colunas categóricas
    print("\nValores únicos na coluna region:")
    print(orders_df['region'].unique())

    print("\nValores únicos na coluna delivery_hour:")
    print(orders_df['delivery_hour'].unique())


def explore_trips(drivers_df):
    # Estatísticas Descritivas
    print("\nEstatísticas Descritivas de Trips:")
    print(drivers_df['Trips'].describe())

    # Histograma de Trips
    plt.figure(figsize=(10, 6))
    plt.style.use('ggplot')
    plt.hist(drivers_df['Trips'], bins=30, color='skyblue', edgecolor='black')
    plt.title('Distribuição de Trips', fontsize=16)
    plt.xlabel('Número de Viagens', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    plt.grid(axis='y', alpha=0.75)
    plt.show()

    # Gráfico de Densidade de Trips
    plt.figure(figsize=(10, 6))
    drivers_df['Trips'].plot.kde(color='salmon')
    plt.title('Densidade de Trips', fontsize=16)
    plt.xlabel('Número de Viagens', fontsize=12)
    plt.ylabel('Densidade', fontsize=12)
    plt.show()