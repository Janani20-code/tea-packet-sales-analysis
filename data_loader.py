import pandas as pd
def load_data(conn):
    """Load all tables from database into DataFrames"""
    tables = [
        'Vendor', 'Product', 'Purchase', 'Customer',
        'Shop', 'CustomerSale', 'ShopSale', 'FinanceSummary'
    ]

    data_dict = {}
    for table in tables:
        try:
            df = pd.read_sql(f"SELECT * FROM {table}", conn)
            data_dict[table.lower()] = df
            print(f"Loaded {table} with {len(df)} records")
        except Exception as e:
            print(f"Error loading {table}: {str(e)}")

    return data_dict