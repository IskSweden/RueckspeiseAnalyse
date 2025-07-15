from load_excel import load_all_years
import pandas as pd
from config import OUTPUT_DIR, OUTPUT_EXCELS, OUTPUT_GRAPHS
from plot import plot_bar_only, plot_line_only, plot_combined
from plot_percent import plot_percent_profile
from HTML_gen import generate_report


if __name__ =="__main__":
    print("loading excel files...")

    df_all = load_all_years()
    
    df_all["timestamp"] = pd.to_datetime(df_all["timestamp"])
    df_all["time_of_day"] = df_all["timestamp"].dt.time

    profile_w = df_all.groupby("time_of_day")["value"].sum()
    profile_w.name = "Leistung kW"

    profile_kwh = profile_w * 0.25
    profile_kwh.name = "Energie (kWh)"

    profile_pct_kwh = (profile_kwh / profile_kwh.max()) * 100
    profile_pct_kwh.name = "Produktion kW (%)"
    

    profile_pct = (profile_w / profile_w.max()) * 100
    profile_pct.name = "Leistung kW (%)"

    print("generating plots...")

    def generate_all(profile, label):
        plot_bar_only(profile, save_path=OUTPUT_GRAPHS / f"ruecklieferung_{label}_bar.png")
        plot_line_only(profile, save_path=OUTPUT_GRAPHS / f"ruecklieferung_{label}_line.png")
        plot_combined(profile, save_path=OUTPUT_GRAPHS / f"ruecklieferung{label}_combined.png")

    generate_all(profile_w, "kW")
    generate_all(profile_kwh, "kWh")

    plot_percent_profile(
        profile_pct,
        save_path=OUTPUT_GRAPHS / "ruecklieferung_pct_highlighted.png",
        title_suffix="(Raw kW)"
    )

    plot_percent_profile(
        profile_pct_kwh,
        save_path=OUTPUT_GRAPHS / "ruecklieferung_pct_kwh_highlighted.png",
        title_suffix="(kWh)"
    )


    
    print("Saving excel exports of data...")

    # Excel export dir
    excel_dir = OUTPUT_EXCELS
    excel_dir.mkdir(parents=True, exist_ok=True)


    # Excel exporting
    df_w = profile_w.reset_index()
    df_w.columns = ["time_of_day", "value_kW"]
    df_w.to_excel(excel_dir / "Ruecklieferung_kW.xlsx", index=False)

    df_kwh = profile_kwh.reset_index()
    df_kwh.columns = ["time_of_day", "value_kWh"]
    df_kwh.to_excel(excel_dir / "Ruecklieferung_kWh.xlsx", index=False)

    df_pct = profile_pct.reset_index()
    df_pct.columns = ["time_of_day", "percent_of_peak_kW"]

    df_pct_kwh = profile_pct_kwh.reset_index()
    df_pct_kwh.columns = ["time_of_day", "percent_of_peak_kWh"]

    df_pct.to_excel(excel_dir / "Ruecklieferung_pct_kW.xlsx", index=False)
    df_pct_kwh.to_excel(excel_dir / "Ruecklieferung_pct_kWh.xlsx", index=False)

    generate_report(profile_w, profile_kwh, profile_pct, profile_pct_kwh)


    print(f"Report, plots and excel saved to: {OUTPUT_DIR.parent}")
