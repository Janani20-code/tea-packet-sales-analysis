import pandas as pd
def clean_data(df_dict):
    """Clean and transform dataset"""
    # Clean date columns
    for table, date_col in [
        ('purchase', 'DateOfPurchase'),
        ('customersale', 'SaleDate'),
        ('shopsale', 'SaleDate'),
        ('financesummary', 'MonthlyProfit')
    ]:
        if table in df_dict and date_col in df_dict[table]:
            df_dict[table][date_col] = pd.to_datetime(
                df_dict[table][date_col],
                format='%d-%m-%Y',
                errors='coerce'
            )

    # Clean numeric columns
    numeric_cols = [
        'StandardPrice', 'PurchaseQuantity', 'PricePerKg',
        'TotalAmount', 'SellingPrice', 'CustomerProfit',
        'ShopProfit', 'CustomerSaleProfit', 'ShopSaleProfit',
        'TotalProfit', 'Investment'
    ]

    for df in df_dict.values():
        for col in df.columns:
            if col in numeric_cols:
                df[col] = pd.to_numeric(df[col], errors='coerce')

    return df_dict