import pandas as pd
import sqlite3

train_df = pd.read_csv('data/fraudTrain.csv')
test_df = pd.read_csv('data/fraudTest.csv')

# Combine the datasets
df = pd.concat([train_df, test_df], ignore_index= True) #Read about ignore index

# drop any nulls (safety step)
df.dropna(inplace = True)

# Convert transaction time to datetime format
df['trans_date_trans_time'] = pd.to_datetime(df['trans_date_trans_time'])

# Save the cleaned CSV
df.to_csv('data/cleaned.csv', index=False)
print("Cleaned data saved to data/cleaned.csv")

# Push to SQLite for SQL access
conn = sqlite3.connect('data/transactions.db')
df.to_sql('transactions', conn, if_exists='replace', index=False)
print("Data pushed to SQLite database at data/transactions.db")
