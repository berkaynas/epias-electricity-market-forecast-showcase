import pandas as pd


def assign_demo_regime(df: pd.DataFrame) -> pd.DataFrame:
    """
    Assign simple regime labels based on rolling volatility.

    NOTE:
    This is a simplified placeholder for a production-grade regime detection system.
    Real implementation uses advanced statistical modeling and state transitions.
    """

    df = df.copy()

    if "ptf_std_3" not in df.columns:
        raise ValueError("Feature 'ptf_std_3' not found. Run feature engineering first.")

    # --------------------------------------------------
    # DEFINE REGIMES BASED ON VOLATILITY
    # --------------------------------------------------
    conditions = [
        df["ptf_std_3"] < 20,                        # low volatility
        (df["ptf_std_3"] >= 20) & (df["ptf_std_3"] < 50),  # medium
        df["ptf_std_3"] >= 50                        # high volatility
    ]

    choices = [0, 1, 2]

    df["regime"] = pd.Series(pd.cut(
        df["ptf_std_3"],
        bins=[-float("inf"), 20, 50, float("inf")],
        labels=choices
    )).astype(int)

    return df
