# plot_percent.py

import matplotlib.pyplot as plt
from pathlib import Path

def plot_percent_profile(series, save_path=None, title_suffix=""):
    x = series.index.astype(str)
    y = series.values

    plt.figure(figsize=(16, 6))
    plt.plot(x, y, color="green", linewidth=2, label="Percentage Profile")

    # Highlight lines at 25%, 50%, 75%, 100%
    for val in [25, 50, 75, 100]:
        plt.axhline(val, color="gray", linestyle="--", linewidth=0.6, alpha=0.5)
        plt.text(len(x) - 1, val + 1, f"{val}%", fontsize=8, color="gray", ha='right')

    plt.title(f"Normalized Production Pattern {title_suffix}")
    plt.xlabel("Time of Day")
    plt.ylabel("Percent of Peak (%)")
    plt.xticks(rotation=90, fontsize=8)
    plt.yticks([0, 25, 50, 75, 100])
    plt.ylim(0, 110)
    plt.grid(True, axis='y', linestyle='--', alpha=0.4)
    plt.tight_layout()

    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=300)
        print(f"Saved percentage graph to: {save_path}")
        plt.close()
    else:
        plt.show()
