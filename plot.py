# plot.py
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path

def _save_plot(x, y, kind="combined", title="", ylabel="Value", save_path=None):
    fig, ax = plt.subplots(figsize=(16, 6))

    if kind in ["bar", "combined"]:
        plt.bar(x, y, label="Bar", alpha=0.6)

    if kind in ["line", "combined"]:
        plt.plot(x, y, color="black", linewidth=1.5, label="Line")

    plt.title(title)
    plt.xlabel("Time of Day")
    plt.ylabel(ylabel)
    plt.xticks(rotation=90, fontsize=8)
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)

    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", "'")))

    
    if kind == "combined":
        ax.legend()
        
    fig.tight_layout()

    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=300)
        print(f"Saved: {save_path}")
        plt.close()
    else:
        plt.show()


def plot_bar_only(series, save_path=None):
    _save_plot(
        x=series.index.astype(str),
        y=series.values,
        kind="bar",
        title="Bar Graph (Summe 15min)",
        ylabel=series.name or "Value",
        save_path=save_path
    )

def plot_line_only(series, save_path=None):
    _save_plot(
        x=series.index.astype(str),
        y=series.values,
        kind="line",
        title="Line Graph (Summe 15min)",
        ylabel=series.name or "Value",
        save_path=save_path
    )

def plot_combined(series, save_path=None):
    _save_plot(
        x=series.index.astype(str),
        y=series.values,
        kind="combined",
        title="Total (Summe 15min)",
        ylabel=series.name or "Value",
        save_path=save_path
    )
