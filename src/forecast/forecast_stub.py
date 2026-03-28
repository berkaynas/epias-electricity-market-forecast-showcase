import pandas as pd


def generate_demo_forecast(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate a simplified forecast signal.

    NOTE:
    This is a placeholder for a production-grade forecasting model.
    Real implementation uses machine learning models and regime-specific logic.
    """

    df = df.copy()

    if "regime" not in df.columns:
        raise ValueError("Regime not found. Run regime assignment first.")

    if "ptf_diff" not in df.columns:
        raise ValueError("Feature 'ptf_diff' missing.")

    # --------------------------------------------------
    # SIMPLE REGIME-AWARE SIGNAL
    # --------------------------------------------------
    signal = []

    for i, row in df.iterrows():
        if row["regime"] == 0:
            # stable → follow trend
            val = row["ptf_diff"] * 0.3

        elif row["regime"] == 1:
            # medium → weaker signal
            val = row["ptf_diff"] * 0.1

        else:
            # volatile → dampen
            val = -row["ptf_diff"] * 0.05

        signal.append(val)

    df["forecast_signal"] = signal

    return df
