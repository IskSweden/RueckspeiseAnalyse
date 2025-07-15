# config.py
#
from pathlib import Path

DATA_DIR = Path("data") / "input"
OUTPUT_DIR = Path("data") / "output"
OUTPUT_GRAPHS = OUTPUT_DIR / "Graphs"
OUTPUT_EXCELS = OUTPUT_DIR / "Excels"

FILES = {
    "2023": DATA_DIR / "2023_Lastgang_Ruecklieferung.xlsx",
    "2024": DATA_DIR / "2024_Lastgang_Ruecklieferung.xlsx",    
}


SHEET_NAME = "Rohdaten_1"
USE_COLUMNS = [0, 1]
COLUMN_RENAMES = {
    "Zeitpunkt (Beginn Messung)": "timestamp",
    "Wert": "value"
}
