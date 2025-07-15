from load_excel import load_all_years
import pandas as pd
from config import OUTPUT_FILE_NAME, OUTPUT_DIR
from plot import plot_bar_only, plot_line_only, plot_combined

if __name__ =="__main__":
    print("loading excel files...")

    df_all = load_all_years()
    
    df_all["timestamp"] = pd.to_datetime(df_all["timestamp"])
    df_all["time_of_day"] = df_all["timestamp"].dt.time

    total_profile = df_all.groupby("time_of_day")["value"].sum()

    df_export = total_profile.reset_index()
    df_export.columns = ["time_of_day", "value"]


    df_export.to_excel(OUTPUT_FILE_NAME, index=False)

    plot_bar_only(total_profile, save_path=OUTPUT_DIR / "bar_graph")
    plot_line_only(total_profile, save_path=OUTPUT_DIR / "line_graph")
    plot_combined(total_profile, save_path=OUTPUT_DIR / "combined graph")

    
    print(f"Plots and excel saved to: {OUTPUT_DIR}")
