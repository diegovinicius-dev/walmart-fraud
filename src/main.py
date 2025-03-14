import os
from data_loading import load_data
from data_cleaning import clean_order_amount, clean_price
from data_exploration import explore_order_amount, explore_categorical_columns, explore_items_columns, explore_trips

# Obter o diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Carregar os dados
orders_df, missing_items_df, drivers_df, products_df, customers_df = load_data(script_dir)

# Mostrar as primeiras 5 linhas de cada tabela
print("Orders Table:")
print(orders_df.head())
print("\nMissing Items Table:")
print(missing_items_df.head())
print("\nDrivers Table:")
print(drivers_df.head())
print("\nProducts Table:")
print(products_df.head())
print("\nCustomers Table:")
print(customers_df.head())

# Mostrar informações sobre as colunas e tipos de dados de cada tabela
print("\nOrders Info:")
print(orders_df.info())
print("\nMissing Items Info:")
print(missing_items_df.info())
print("\nProducts Info:")
print(products_df.info())
print("\nCustomers Info:")
print(customers_df.info())

# Limpar os dados
orders_df = clean_order_amount(orders_df)
products_df = clean_price(products_df)

# Verificar a conversão
print("\nOrders Info (Após conversão):")
print(orders_df.info())
print("\nProducts Info (Após conversão):")
print(products_df.info())

# Explorar os dados
explore_order_amount(orders_df)
explore_items_columns(orders_df)
explore_trips(drivers_df)
explore_categorical_columns(orders_df)


