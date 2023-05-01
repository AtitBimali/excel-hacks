import pandas as pd

# Load the excel file into a pandas dataframe
df = pd.read_excel('file1.xlsx', header=0)

# Group the dataframe by product name and calculate the mean rate for each group
df_grouped = df.groupby('prodname')['rate'].mean().reset_index()

# Calculate the 10% lower and higher rate for each product
df_grouped['lower_rate'] = df_grouped['rate'] * 0.9
df_grouped['higher_rate'] = df_grouped['rate'] * 1.1

# Merge the grouped dataframe with the original dataframe to get the lower and higher rates for each row
df_merged = pd.merge(df, df_grouped, on='prodname', how='left')
# Filter the rows where the rate is 10% lower or higher than the average rate for the product
df_filtered = df_merged[(df_merged['rate_x'] < df_merged['lower_rate']) | (df_merged['rate_x'] > df_merged['higher_rate'])]

# Print the filtered dataframe
print(df_filtered)
df_filtered.to_excel('filtered_file.xlsx', index=False)


