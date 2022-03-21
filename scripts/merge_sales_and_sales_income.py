print('hi')
import pandas as pd

sales_by_income_full = pd.read_csv('scripts/data/sales_by_income_feb_22.csv');
sales_full = pd.read_csv('scripts/data/sales_feb_22.csv');

sales_by_income = sales_by_income_full[[
  'Date', 'Txn #', 'Txn Type', 'Patient ID', 'Patient', 'Item', 'Qty', 'Revenue', 'Tax amount'
]]
sales_by_income.rename(columns={'Txn #': 'Txn ID'}, inplace=True)
sales = sales_full[['Txn ID', 'Memo', 'Amount (tax included)', 'Payment method']]

merged_data = sales.merge(sales_by_income, on='Txn ID', how='left')

print(merged_data)

merged_data.to_csv('scripts/output/sales_by_income_sales_merge.csv')
