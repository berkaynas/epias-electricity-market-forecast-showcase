import pandas as pd


def generate_demo_decision(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate simplified decision outputs from forecast signal.

    NOTE:
    This is a placeholder for a production-grade decision engine.
    Real implementation includes cost modeling, risk control, and dynamic sizing.
    """

    df = df.copy()

    if "forecast_signal" not in df.columns:
        raise ValueError("Forecast signal not found.")

    # --------------------------------------------------
    # SIMPLE DECISION LOGIC
    # --------------------------------------------------
    decisions = []
    hedge_ratios = []

    for val in df["forecast_signal"]:
        if val > 5:
            decision = "HEDGE"
            hedge = 0.5

        elif val < -5:
            decision = "REVERSE"
            hedge = 0.5

        else:
            decision = "NO_ACTION"
            hedge = 0.0

        decisions.append(decision)
        hedge_ratios.append(hedge)

    df["decision"] = decisions
    df["hedge_ratio"] = hedge_ratios

    return df
