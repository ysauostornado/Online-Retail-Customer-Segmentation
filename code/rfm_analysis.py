import pandas as pd

# Load data
df = pd.read_csv('data/cleaned_data.csv')

# Calculate Recency, Frequency, and Monetary values
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (pd.Timestamp('2023-12-31') - x.max()).days,
    'InvoiceNo': 'count',
    'TotalPrice': 'sum'
}).rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'TotalPrice': 'Monetary'
})

# Assign RFM Scores
rfm['R_Score'] = pd.qcut(rfm['Recency'], 4, labels=[4, 3, 2, 1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'], 4, labels=[1, 2, 3, 4])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 4, labels=[1, 2, 3, 4])

# Calculate Total RFM Score
rfm['RFM_Score'] = rfm[['R_Score', 'F_Score', 'M_Score']].sum(axis=1)

# Save RFM analysis results
rfm.to_csv('data/rfm_results.csv')
