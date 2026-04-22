import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 1. Set Marvellous Modern Theme
plt.style.use("seaborn-v0_8-darkgrid")
# Custom colors for a premium look
background_color = "#1e1e2f"  # Deep Midnight Blue
grid_color = "#3e3e5e"

# 2. Data Loading
file_name = "wb_data.xlsx"
df = pd.read_excel(file_name)
df = df.dropna(subset=["Country Name"])
df.set_index("Country Name", inplace=True)

# 3. Year Processing
year_columns = [col for col in df.columns if "[" in col]
df_clean = df[year_columns].copy()
df_clean.columns = [int(col.split(" ")[0]) for col in df_clean.columns]

# 4. Cleaning
df_clean = df_clean.replace("..", pd.NA)
plot_data = df_clean.T.apply(pd.to_numeric)

# 5. Filter
target_countries = ["Iraq", "Egypt", "Morocco", "Oman"]
plot_data = plot_data[target_countries]

# 6. Initialize Plot with Custom Colors
fig, ax = plt.subplots(figsize=(15, 10))
fig.patch.set_facecolor(background_color)
ax.set_facecolor(background_color)

# Plot with thicker lines
plot_data.plot(ax=ax, marker="o", linewidth=3.5, markersize=7)


# 7. Formatter
def format_gdp(x, pos):
    if x >= 1e12:
        return f"{x / 1e12:g}T"
    elif x >= 1e9:
        return f"{x / 1e9:g}B"
    return f"{x:g}"


ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_gdp))
ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# 8. Chart Formatting
plt.title(
    "GDP Comparison (2000-2024)", fontsize=24, fontweight="bold", color="white", pad=40
)
plt.xlabel("Year", fontsize=15, labelpad=15, color="white")
plt.ylabel("GDP (USD)", fontsize=15, labelpad=15, color="white")

# Adjust Tick & Grid Colors
ax.tick_params(axis="both", colors="white", labelsize=12)
ax.grid(True, linestyle="--", alpha=0.2, color="white")

# 9. Single Combined Square Legend
plt.legend(
    title="Countries",
    loc="upper left",
    bbox_to_anchor=(0.04, 0.98),
    prop={"size": 14},
    title_fontsize=15,
    frameon=True,
    fancybox=False,
    edgecolor="white",
    facecolor=background_color,
    labelcolor="white",
)

# 10. Save and Show
plt.tight_layout()

# Save as Figure_Midnight for your GitHub README gallery
plt.savefig(
    "Figure_Midnight.png", dpi=300, facecolor=fig.get_facecolor(), bbox_inches="tight"
)

plt.show()
