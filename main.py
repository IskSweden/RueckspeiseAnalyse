from load_excel import load_all_years
import pandas as pd
from config import OUTPUT_FILE_NAME
from plot import plot_total_profile

if __name__ =="__main__":
    print("loading excel files...")

    df_all = load_all_years()
    
    df_all["timestamp"] = pd.to_datetime(df_all["timestamp"])
    df_all["time_of_day"] = df_all["timestamp"].dt.time

    total_profile = df_all.groupby("time_of_day")["value"].sum()

    df_export = total_profile.reset_index()
    df_export.columns = ["time_of_day", "value"]


    df_export.to_excel(OUTPUT_FILE_NAME, index=False)

    plot_total_profile(total_profile)

    
    print(f"data saved to {OUTPUT_FILE_NAME}")
