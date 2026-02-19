import pandas as pd
df=pd.read_csv("customer_shopping_behavior.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.describe(include="all"))
print(df.isnull().sum())
avg_rating = df["Review Rating"].median()
df["Review Rating"] = df["Review Rating"].fillna(avg_rating)
print(df.isnull().sum())
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(" ","_")
df=df.rename(columns={"purchase_amount_(usd)" : "purchase_amount"})
print(df.columns)
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)
print(df[["age",'age_group']])
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
print(df['purchase_frequency_days'])
print(df[["discount_applied","promo_code_used"]])
print((df["discount_applied"]==df["promo_code_used"]).all())
df.drop("promo_code_used",axis=1)
print(df.info())
# install required libraries


from sqlalchemy import create_engine
import pandas as pd

# MySQL connection details
username = "root"
password = "mrahmad702"
host = "localhost"
port = "3306"
database = "Customer_behavior"

# Create engine
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# Write DataFrame to MySQL
table_name = "Customer_behavior_table"   # choose any table name
df.to_sql(table_name, engine, if_exists="replace", index=False)

# Read back sample
pd.read_sql(f"SELECT * FROM {table_name} LIMIT 5;", engine)
