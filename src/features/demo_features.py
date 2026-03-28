import pandas as pd
import numpy as np


def build_demo_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build simplified feature set for demo purposes.

    NOTE:
    This is a minimal version of the production feature engineering pipeline.
    Real implementation includes significantly more complex transformations.
    """

    df = df.copy()

    # --------------------------------------------------
    # BASIC PRICE FEATURES
    # --------------------------------------------------
    df["ptf_diff"] = df["PTF"].diff().fillna(0)

    df["ptf_ma_3"] = df["PTF"].rolling(3, min_periods=1).mean()
    df["ptf_std_3"] = df["PTF"].rolling(3, min_periods=1).std().fillna(0)

    # --------------------------------------------------
    # DEMAND-SUPPLY GAP (simple proxy)
    # --------------------------------------------------
    if "Consumption" in df.columns and "Production" in df.columns:
        df["imbalance"] = df["Consumption"] - df["Production"]

    # --------------------------------------------------
    # TIME FEATURES (important for time series)
    # --------------------------------------------------
    df["hour"] = df["Datetime"].dt.hour

    df["hour_sin"] = np.sin(2 * np.pi * df["hour"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["hour"] / 24)

    # --------------------------------------------------
    # CLEANUP
    # --------------------------------------------------
    df = df.drop(columns=["hour"])

    return df
