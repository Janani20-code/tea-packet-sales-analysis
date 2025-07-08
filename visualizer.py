import matplotlib.pyplot as plt
import pandas as pd


def plot_monthly_profit(finance_df):
    """Visualize monthly profit trend"""
    plt.figure(figsize=(12, 6))
    ax = finance_df.set_index('MonthlyProfit')['TotalProfit'].plot(
        marker='o',
        color='#2c7bb6',
        linewidth=2.5
    )
    plt.title('Monthly Profit Trend', fontsize=14)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Profit (₹)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Add value labels
    for x, y in zip(finance_df['MonthlyProfit'], finance_df['TotalProfit']):
        plt.text(x, y, f'₹{y:,.0f}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig('monthly_profit_trend.png')
    print("Saved monthly_profit_trend.png")


def plot_product_performance(product_df, cust_sale_df, shop_sale_df):
    """Visualize product sales performance"""
    try:
        # Prepare data
        customer_sales = cust_sale_df.groupby('ProductID')['Quantity_500g'].sum().reset_index()
        shop_sales = shop_sale_df.groupby('ProductID')['Quantity'].sum().reset_index()

        # Merge data
        product_sales = pd.merge(customer_sales, shop_sales, on='ProductID', how='outer')
        product_sales = pd.merge(product_sales, product_df[['ProductID', 'BrandName']], on='ProductID', how='left')

        # Fill NaN values with 0
        product_sales.fillna(0, inplace=True)

        # Plot
        plt.figure(figsize=(10, 6))
        ax = product_sales.set_index('BrandName')[['Quantity_500g', 'Quantity']].plot(
            kind='bar',
            color=['#fdae61', '#d7191c'],
            edgecolor='black'
        )
        plt.title('Product Sales Performance', fontsize=14)
        plt.xlabel('Product', fontsize=12)
        plt.ylabel('Quantity Sold', fontsize=12)
        plt.xticks(rotation=0)
        plt.legend(['Customer Sales (500g units)', 'Shop Sales (units)'])

        # Add value labels
        for container in ax.containers:
            ax.bar_label(container, fmt='%.0f', label_type='edge', padding=3)

        plt.tight_layout()
        plt.savefig('product_performance.png')
        print("Saved product_performance.png")

    except Exception as e:
        print(f"Error in product performance visualization: {str(e)}")


def plot_top_customers(customer_df, cust_sale_df):
    """Visualize top customers by profit"""
    try:
        # Prepare data
        customer_profit = cust_sale_df.groupby('CustomerID')['CustomerProfit'].sum()
        top_customers = customer_profit.nlargest(5).reset_index()
        top_customers = pd.merge(
            top_customers,
            customer_df[['CustomerID', 'CustomerName']],
            on='CustomerID',
            how='left'
        )

        # Plot
        plt.figure(figsize=(10, 6))
        plt.barh(
            top_customers['CustomerName'],
            top_customers['CustomerProfit'],
            color='#2ca25f',
            edgecolor='black'
        )
        plt.title('Top 5 Customers by Profit', fontsize=14)
        plt.xlabel('Total Profit (₹)', fontsize=12)
        plt.ylabel('Customer', fontsize=12)

        # Add value labels
        for i, v in enumerate(top_customers['CustomerProfit']):
            plt.text(v + 5, i, f'₹{v:,.0f}', ha='left', va='center')

        plt.gca().invert_yaxis()  # Highest profit at top
        plt.tight_layout()
        plt.savefig('top_customers.png')
        print("Saved top_customers.png")

    except Exception as e:
        print(f"Error in top customers visualization: {str(e)}")
def plot_top_shops(shop_df, shop_sale_df):
    """Visualize top shops by profit"""
    try:
        shop_profit = shop_sale_df.groupby('ShopID')['ShopProfit'].sum()
        top_shops = shop_profit.nlargest(5).reset_index()
        top_shops = pd.merge(
            top_shops,
            shop_df[['ShopID', 'ShopName']],
            on='ShopID',
            how='left'
        )

        plt.figure(figsize=(10, 6))
        plt.barh(
            top_shops['ShopName'],
            top_shops['ShopProfit'],
            color='#3182bd', edgecolor='black'
        )
        plt.title('Top 5 Shops by Profit', fontsize=14)
        plt.xlabel('Total Profit (₹)', fontsize=12)
        plt.ylabel('Shop', fontsize=12)

        for i, v in enumerate(top_shops['ShopProfit']):
            plt.text(v + 5, i, f'₹{v:,.0f}', ha='left', va='center')

        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.savefig('top_shops.png')
        print("Saved top_shops.png")

    except Exception as e:
        print(f"Error in top shops visualization: {str(e)}")



def analyze_and_visualize(df_dict):
    """Orchestrate analysis and visualization"""
    plt.style.use('seaborn-v0_8-whitegrid')

    try:
        # Monthly Profit Trend
        if 'financesummary' in df_dict and not df_dict['financesummary'].empty:
            plot_monthly_profit(df_dict['financesummary'])
        else:
            print("Skipping monthly profit: No finance data")

        # Product Performance
        if all(key in df_dict for key in ['product', 'customersale', 'shopsale']):
            plot_product_performance(
                df_dict['product'],
                df_dict['customersale'],
                df_dict['shopsale']
            )
        else:
            print("Skipping product performance: Missing required data")

        # Top Customers
        if all(key in df_dict for key in ['customer', 'customersale']):
            plot_top_customers(
                df_dict['customer'],
                df_dict['customersale']
            )
        else:
            print("Skipping top customers: Missing required data")

        # Top Shops
        if all(key in df_dict for key in ['shop', 'shopsale']):
            plot_top_shops(
                df_dict['shop'],
                df_dict['shopsale']
            )
        else:
            print("Skipping top shops: Missing required data")


    except Exception as e:
        print(f"Visualization error: {str(e)}")