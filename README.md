# Rückspeisung Analysis (2023 + 2024)

This project processes and visualizes Rückspeisung (grid feed-in) data from Excel files, generating static plots, energy summaries, and a professional HTML report — all offline and shareable.

---

## Project Structure
```
Data/
├── input/ # Place raw Excel files here
│ ├── 2023_Lastgang_Ruecklieferung.xlsx
│ └── 2024_Lastgang_Ruecklieferung.xlsx
├── output/
│ ├── Graphs/ # Static PNG plots
│ ├── Excels/ # Processed exports (kWh, %, etc.)
│ └── report.html # Clean full report (offline-friendly)
```

## Installation

Clone the repo and install dependencies:

```bash
git clone <your-repo-url>
cd Rueckspeiseanalyse_REUN

# Create venv (optional)
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows

# Install dependencies
pip install -r requirements.txt

## Run the main pipeline
```bash
python main.py
```
