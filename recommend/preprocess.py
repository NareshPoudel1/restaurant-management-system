# preprocess.py
import pandas as pd
from shop.models import Product, Order

# Create a dataframe of products and their categories
products = Product.objects.all()
df_products = pd.DataFrame(list(products.values()))

# Create a dataframe of user orders and their items
orders = Order.objects.filter(ordered=True)
df_orders = pd.DataFrame(list(orders.values('user_id', 'items')))

# Merge the two dataframes on 'id' column
df_merged = pd.merge(df_products, df_orders, left_on='id', right_on='items_id')

# Group the merged dataframe by 'user_id' and aggregate the items into a list
df_grouped = df_merged.groupby('user_id')['name'].apply(list)

# Convert the grouped series to a dataframe
df_final = pd.DataFrame(df_grouped)

# Reset index of the final dataframe
df_final = df_final.reset_index()
