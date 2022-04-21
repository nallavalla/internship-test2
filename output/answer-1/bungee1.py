from pandas import*
grocery = p.read_CSV("main.CSV")
# grocery.head()
# grocery.groupby('product_description')['price'].mean()
grocery["price_new"] = grocery['price'].fillnal(
    grocery.groupby('product_description')['price'].transform("mean")
)
print(grocery[grocery["price"].isna()].head())