import pandas as pd
import numpy as np

# Load the dataset
file_path = 'C:/Users/ABU HURAIRAH & SONS/Downloads/BizMetrics Data Set.xlsx'
df = pd.read_excel(file_path)

# Summary statistics for 'Annual Revenue'
summary_stats = df['Annual Revenue'].describe()
std_error = df['Annual Revenue'].sem()  # Standard Error
mode = df['Annual Revenue'].mode()[0] if not df['Annual Revenue'].mode().empty else 'No Mode'
skewness = df['Annual Revenue'].skew()  # Skewness
kurtosis = df['Annual Revenue'].kurtosis()  # Kurtosis

# Additional statistics (Range, Sum)
range_value = df['Annual Revenue'].max() - df['Annual Revenue'].min()
sum_value = df['Annual Revenue'].sum()

# Creating a dictionary of summary statistics
summary_dict = {
    'Mean': summary_stats['mean'],
    'Standard Error': std_error,
    'Median': summary_stats['50%'],
    'Mode': mode,
    'Standard Deviation': summary_stats['std'],
    'Sample Variance': summary_stats['std'] ** 2,
    'Kurtosis': kurtosis,
    'Skewness': skewness,
    'Range': range_value,
    'Minimum': summary_stats['min'],
    'Maximum': summary_stats['max'],
    'Sum': sum_value,
    'Count': summary_stats['count']
}

# Convert dictionary to DataFrame
summary_df = pd.DataFrame([summary_dict])

# Calculating Percentiles for 'Profit Margin'
percentiles = np.percentile(df['Profit Margin'], [25, 50, 75])
percentile_df = pd.DataFrame({
    'Percentile': ['25th', '50th (Median)', '75th'],
    'Profit Margin': percentiles
})

# Save the results to an Excel file
output_file = 'BizMetrics_Analysis.xlsx'
with pd.ExcelWriter(output_file) as writer:
    summary_df.to_excel(writer, sheet_name='Annual Revenue Summary', index=False)
    percentile_df.to_excel(writer, sheet_name='Profit Margin Percentiles', index=False)

print(f"Analysis complete. Results saved to {output_file}.")
