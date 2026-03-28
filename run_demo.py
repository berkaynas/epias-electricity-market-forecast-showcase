from pathlib import Path

from src.ingestion.sample_loader import load_sample_data
from src.features.demo_features import build_demo_features
from src.regime.regime_stub import assign_demo_regime
from src.forecast.forecast_stub import generate_demo_forecast
from src.decision.decision_stub import generate_demo_decision


def run_pipeline():
    print("🚀 Running EPİAŞ Forecast Showcase Pipeline...\n")

    # --------------------------------------------------
    # INGESTION
    # --------------------------------------------------
    print("📥 Loading data...")
    df = load_sample_data()

    # --------------------------------------------------
    # FEATURES
    # --------------------------------------------------
    print("🧠 Building features...")
    df = build_demo_features(df)

    # --------------------------------------------------
    # REGIME
    # --------------------------------------------------
    print("🔀 Assigning regime...")
    df = assign_demo_regime(df)

    # --------------------------------------------------
    # FORECAST
    # --------------------------------------------------
    print("📊 Generating forecast...")
    df = generate_demo_forecast(df)

    # --------------------------------------------------
    # DECISION
    # --------------------------------------------------
    print("⚖️ Generating decisions...")
    df = generate_demo_decision(df)

    # --------------------------------------------------
    # OUTPUT
    # --------------------------------------------------
    output_path = Path("output/demo_output.csv")
    df.to_csv(output_path, index=False)

    print(f"\n✅ Pipeline completed.")
    print(f"📁 Output saved to: {output_path.resolve()}")

    print("\n🔍 Sample output:")
    print(df[["Datetime", "forecast_signal", "decision", "hedge_ratio"]].head())


if __name__ == "__main__":
    run_pipeline()
