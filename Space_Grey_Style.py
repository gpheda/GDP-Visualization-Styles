import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 1. Set Colors (GitHub/Space Grey Palette)
plt.style.use("seaborn-v0_8-darkgrid")
background_color = "#0d1117"  # Official GitHub Dark Mode color
grid_color = "#30363d"

# 2. Data Loading
file_name = "wb_data.xlsx"
df = pd.read_excel(file_name)
df = df.dropna(subset=["Country Name"])
df.set_index("Country Name", inplace=True)

# 3. Year Processing
year_columns = [col for col in df.columns if "[" in col]
df_clean = df[year_columns].copy()
df_clean.columns = [int(col.split(' ')[0]) for col in df_clean.columns]

# 4. Cleaning & Conversion
df_clean = df_clean.replace("..", pd.NA)
plot_data = df_clean.T.apply(pd.to_numeric)

# 5. Filter
target_countries = ["Iraq", "Egypt", "Morocco", "Oman"]
plot_data = plot_data[target_countries]

# 6. Initialize Plot
fig, ax = plt.subplots(figsize=(15, 10))
fig.patch.set_facecolor(background_color)
ax.set_facecolor(background_color)

# 7. Modern Plotting (Slightly transparent lines for a "glow" effect)
plot_data.plot(ax=ax, marker="o", linewidth=3.5, markersize=7, alpha=0.9)


# 8. Smart Formatter
def format_gdp(x, pos):
    if x >= 1e12:
        return f"{x / 1e12:g}T"
    elif x >= 1e9:
        return f"{x / 1e9:g}B"
    return f"{x:g}"


ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_gdp))
ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# 9. Chart Formatting
plt.title(
    "GDP Trends: Comparative Analysis",
    fontsize=24,
    fontweight="bold",
    color="white",
    pad=40,
)
plt.xlabel("Year", fontsize=15, color="white")
plt.ylabel("GDP (Current USD)", fontsize=15, color="white")

# Adjust Tick & Grid Colors
ax.tick_params(axis="both", colors="white", labelsize=12)
ax.grid(True, linestyle="--", alpha=0.3, color=grid_color)

# 10. Square Legend
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

# 11. Save as the Arsenal filename
plt.tight_layout()
plt.savefig(
    "Figure_SpaceGrey.png", dpi=300, facecolor=fig.get_facecolor(), bbox_inches="tight"
)

plt.show()
