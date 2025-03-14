import pandas as pd

def clean_order_amount(orders_df):
    """Limpa e converte a coluna order_amount."""
    # Verificar valores não numéricos
    non_numeric_values_order_amount = orders_df[pd.to_numeric(orders_df['order_amount'], errors='coerce').isna()]['order_amount'].unique()
    if (len(non_numeric_values_order_amount) > 0):
        print("Valores não numéricos encontrados na coluna 'order_amount': ", non_numeric_values_order_amount)
    else:
        print("Não foram encontrados valores não numéricos na coluna 'order_amount'")

    # Remover caracteres não numéricos
    orders_df['order_amount'] = orders_df['order_amount'].astype(str).str.replace(r'[$,]', '', regex=True)

    # Converter a coluna para numérico
    orders_df['order_amount'] = pd.to_numeric(orders_df['order_amount'], errors='coerce')
    return orders_df

def clean_price(products_df):
    """Limpa e converte a coluna price."""
    # Verificar valores não numéricos
    non_numeric_values_price = products_df[pd.to_numeric(products_df['price'], errors='coerce').isna()]['price'].unique()
    if (len(non_numeric_values_price) > 0):
        print("Valores não numéricos encontrados na coluna 'price': ", non_numeric_values_price)
    else:
        print("Não foram encontrados valores não numéricos na coluna 'price'")

    # Remover caracteres não numéricos
    products_df['price'] = products_df['price'].astype(str).str.replace(r'[$,]', '', regex=True)

    # Converter a coluna para numérico
    products_df['price'] = pd.to_numeric(products_df['price'], errors='coerce')

    # Remover coluna extra 'order_amount'
    if 'order_amount' in products_df.columns:
        products_df = products_df.drop(columns=['order_amount'])
    return products_df