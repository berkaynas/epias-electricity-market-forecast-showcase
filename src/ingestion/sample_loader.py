import pandas as pd
from pathlib import Path


def load_sample_data(path="data/sample_market_data.csv"):
    """
    Load sample market data for demo purposes.

    NOTE:
    This is a simplified placeholder for the production ingestion layer.
    Real system includes multiple data sources, validation, and time alignment.
    """

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Sample data not found at {path}")

    df = pd.read_csv(path, parse_dates=["Datetime"])

    # Basic sanity checks (professional touch)
    required_cols = ["Datetime", "PTF"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    df = df.sort_values("Datetime").reset_index(drop=True)

    return df
