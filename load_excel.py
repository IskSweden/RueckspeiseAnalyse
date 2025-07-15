from config import FILES, SHEET_NAME, USE_COLUMNS, COLUMN_RENAMES
import pandas as pd


def load_all_years():
    dfs = []
    for year, path in FILES.items():
        df = pd.read_excel(path, sheet_name=SHEET_NAME, usecols=USE_COLUMNS)
        df.rename(columns=COLUMN_RENAMES, inplace=True)
        df["year"] = year
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)
