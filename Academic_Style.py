import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 1. Set the Academic Standard Style
plt.style.use('ggplot')

# 2. Data Loading
file_name = 'wb_data.xlsx'
df = pd.read_excel(file_name)
df = df.dropna(subset=['Country Name'])
df.set_index('Country Name', inplace=True)

# 3. Year Processing
year_columns = [col for col in df.columns if '[' in col]
df_clean = df[year_columns].copy()
df_clean.columns = [int(col.split(' ')[0]) for col in df_clean.columns]

# 4. Cleaning & Conversion
df_clean = df_clean.replace('..', pd.NA)
plot_data = df_clean.T.apply(pd.to_numeric)

# 5. Filter for target countries
target_countries = ['Iraq', 'Egypt', 'Morocco', 'Oman']
plot_data = plot_data[target_countries]

# 6. Initialize Plot (White background for paper-ready look)
fig, ax = plt.subplots(figsize=(15, 10), facecolor='white')

# 7. Professional Plotting
# Clean lines with markers for precise data point identification
plot_data.plot(ax=ax, marker='o', linewidth=2.5, markersize=6, alpha=0.8)

# 8. Smart Y-Axis Formatter (T/B)
def format_gdp(x, pos):
    if x >= 1e12: return f'{x/1e12:g}T'
    elif x >= 1e9: return f'{x/1e9:g}B'
    return f'{x:g}'

ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_gdp))
ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# 9. Academic Chart Formatting
plt.title('GDP Comparison: Regional Economic Analysis', 
          fontsize=22, fontweight='bold', color='#2c3e50', pad=30)
plt.xlabel('Year', fontsize=14, color='#2c3e50')
plt.ylabel('GDP (Current USD)', fontsize=14, color='#2c3e50')

# Grid and Ticks
ax.tick_params(axis='both', which='major', labelsize=11, labelcolor='#2c3e50')
ax.grid(True, linestyle='--', alpha=0.7)

# 10. The Professional Square Legend
plt.legend(
    title='Countries',
    loc='upper left', 
    bbox_to_anchor=(0.02, 0.98), 
    prop={'size': 13}, 
    title_fontsize=14,
    frameon=True,      
    fancybox=False,    # Mandatory square corners for academic look
    edgecolor='#bdc3c7', 
    facecolor='white',
    framealpha=1
)

# 11. Save as the Arsenal filename
plt.tight_layout()
plt.savefig('Figure_Academic.png', dpi=300, bbox_inches='tight')

plt.show()
