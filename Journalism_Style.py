import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 1. Set the Data Journalism Style
plt.style.use('fivethirtyeight')

# 2. Data Loading
file_name = 'wb_data.xlsx'
df = pd.read_excel(file_name)
df = df.dropna(subset=['Country Name'])
df.set_index('Country Name', inplace=True)

# 3. Year Processing
year_columns = [col for col in df.columns if '[' in col]
df_clean = df[year_columns].copy()
df_clean.columns = [int(col.split(' ')[0]) for col in df_clean.columns]

# 4. Cleaning
df_clean = df_clean.replace('..', pd.NA)
plot_data = df_clean.T.apply(pd.to_numeric)

# 5. Filter
target_countries = ['Iraq', 'Egypt', 'Morocco', 'Oman']
plot_data = plot_data[target_countries]

# 6. Initialize Plot (Signature light-grey background)
fig, ax = plt.subplots(figsize=(15, 10), facecolor='#f0f0f0')
ax.set_facecolor('#f0f0f0')

# 7. Bold Plotting (Thick lines for editorial impact)
plot_data.plot(ax=ax, linewidth=4, alpha=0.85) 

# 8. Smart Y-Axis Formatter (T/B)
def format_gdp(x, pos):
    if x >= 1e12: return f'{x/1e12:g}T'
    elif x >= 1e9: return f'{x/1e9:g}B'
    return f'{x:g}'

ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_gdp))

# 9. Journalism Formatting (Left-aligned bold title)
plt.title('GDP Trends: Regional Analysis', 
          fontsize=26, fontweight='bold', color='#333333', loc='left', pad=30)
plt.ylabel('GDP (Current USD)', fontsize=14, fontweight='bold')

# Horizontal grid focus
ax.grid(True, axis='y', linestyle='-', alpha=0.5)
ax.grid(False, axis='x') 

# 10. Clean Legend
plt.legend(
    loc='upper left', 
    bbox_to_anchor=(0.01, 0.99), 
    prop={'size': 14, 'weight': 'bold'}, 
    frameon=True,
    fancybox=False,
    edgecolor='white',
    facecolor='#f0f0f0'
)

# 11. Save as the Arsenal filename
plt.tight_layout()
plt.savefig('Figure_Journalism.png', dpi=300, facecolor=fig.get_facecolor())

plt.show()
