import os
import pandas as pd

def load_data(src_dir):
    """Carrega os dados dos arquivos CSV."""
    data_dir = os.path.join(src_dir, "data")
    orders_path = os.path.join(data_dir, "5qPZ8EyPSau2UNVvdRak_orders.csv")
    missing_items_path = os.path.join(data_dir, "LKyEGqe9QsWdRFCujqRc_missing_items_data.csv")
    drivers_path = os.path.join(data_dir, "DASNKm5LTPy2hXX0dM0D_drivers_data.csv")
    products_path = os.path.join(data_dir, "PGqj7HULTByfy23R8vxN_products_data.csv")
    customers_path = os.path.join(data_dir, "i7WiftZQm2ToVfzHFBBW_customers_data.csv")

    orders_df = pd.read_csv(orders_path)
    missing_items_df = pd.read_csv(missing_items_path)
    drivers_df = pd.read_csv(drivers_path)
    products_df = pd.read_csv(products_path)
    customers_df = pd.read_csv(customers_path)

    return orders_df, missing_items_df, drivers_df, products_df, customers_df