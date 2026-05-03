from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "outputs"
MODEL_DIR = OUTPUT_DIR / "models"
CHART_DIR = OUTPUT_DIR / "charts"

OUTPUT_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)
CHART_DIR.mkdir(exist_ok=True)

@dataclass
class AppConfig:
    default_ticker: str = "RELIANCE.NS"
    default_start_date: str = "2018-01-01"
    default_end_date: str = "2026-01-01"
    target_column: str = "Close"
    forecast_horizon: int = 1
    train_ratio: float = 0.70
    val_ratio: float = 0.15
    test_ratio: float = 0.15
    short_window: int = 5
    medium_window: int = 20
    long_window: int = 50
    random_state: int = 42
    app_title: str = "Indian Stock Market Prediction App"
    page_icon: str = "📈"

config = AppConfig()