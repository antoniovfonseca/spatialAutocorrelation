# Load the newly uploaded Excel file
new_file_path = "C:/Users/AntFonseca/spatialAutocorrelation/heatmap19902020.xlsx"
xls_new = pd.ExcelFile(new_file_path)

# Check sheet names
xls_new.sheet_names

# Load the data from 'Sheet1'
df_new = pd.read_excel(xls_new, sheet_name="Sheet1", index_col=0)

# Clean: drop unnecessary columns if present
df_new = df_new.drop(columns=["(blank)", "Grand Total"], errors='ignore')
df_new = df_new.drop(index="Grand Total", errors='ignore')

# Replace NaNs with 0
df_new = df_new.fillna(0)

# Rename any NaN or blank index to "NS"
df_new.index = df_new.index.to_series().replace({np.nan: "NS", "": "NS"})
df_new.columns = df_new.columns.to_series().replace({np.nan: "NS", "": "NS"})

# Plot the updated heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    df_new,
    annot=True,
    fmt=".0f",
    cmap="YlOrRd",
    linewidths=.5,
    cbar_kws={'label': 'Number of transitions'}
)
plt.title("LISA Transition Heatmap (1990 → 2020)")
plt.xlabel("Cluster in 2020")
plt.ylabel("Cluster in 1990")
plt.tight_layout()
plt.show()

