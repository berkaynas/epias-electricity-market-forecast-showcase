# ⚡ EPİAŞ Electricity Market Forecasting & Decision System (Showcase)

## Overview

This project demonstrates a modular, real-time forecasting and decision pipeline designed for electricity market dynamics.

The system simulates how market data can be transformed into actionable decisions through:

- Feature engineering
- Regime-aware modeling
- Forecast signal generation
- Decision logic

NOTE:
This repository is a simplified showcase version.  
Proprietary modeling logic, calibration methods, and production trading components are intentionally excluded.

---

## Problem Context

Electricity markets involve:

- Delayed and revised data streams  
- High volatility and regime shifts  
- Decision-making under uncertainty  

A robust system must:

- Avoid data leakage  
- Handle time alignment correctly  
- Adapt to changing market conditions  
- Generate decisions in real-time  

---

## System Architecture

Pipeline:

Data → Ingestion → Features → Regime → Forecast → Decision

Modules:

- Ingestion  
  Loads and validates input data  
  (Production system includes multiple API-based data sources)

- Feature Engineering  
  Rolling statistics, momentum, cyclic encoding  

- Regime Detection  
  Assigns market states based on volatility  
  (Production version uses statistical regime models)

- Forecast Layer  
  Generates signal conditioned on regime  
  (Production version uses ML models)

- Decision Layer  
  Converts signals into actions (HEDGE / NO_ACTION / REVERSE)  
  Includes position sizing logic  

---

## How to Run

python run_demo.py

---

## Example Output

Datetime | forecast_signal | decision | hedge_ratio  
---------------------------------------------------  
2026-01-01 04:00:00 | 6.0 | HEDGE | 0.5  

---

## Notes on This Version

This repository is intentionally simplified:

- No real market APIs  
- No model training or weights  
- No proprietary feature engineering  
- No real cost/edge calculation  

Instead, it focuses on:

- System design  
- Pipeline structure  
- Modular architecture  
- Real-time decision flow  

---

## Production System (Not Included)

The full system (private) includes:

- Multi-source data ingestion  
- Advanced feature engineering  
- Regime-switching statistical models  
- Machine learning forecasting models  
- Real-time correction logic  
- Risk-aware decision engine  

---

## Key Takeaways

This project demonstrates:

- End-to-end pipeline thinking  
- Time-series feature engineering  
- Regime-aware modeling approach  
- Decision system design  
- Production-style modular architecture  

---

## Author

Built as part of a real-world exploration into electricity market forecasting and decision systems.
