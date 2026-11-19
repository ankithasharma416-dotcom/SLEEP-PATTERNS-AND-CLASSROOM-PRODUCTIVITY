"""Predict a classroom productivity rating with the saved project model."""

from pathlib import Path
import argparse

import joblib
import pandas as pd


FEATURES = [
    "On average, how many hours do you sleep per night?",
    "5. What time do you usually go to sleep on weekdays?",
    "How consistent is your sleep schedule?",
    "How often do you sleep late because of assignments, studying, projects, etc.?",
    "How would you rate your overall sleep quality?",
    "How often do you feel sleepy during lectures?",
    "14. How much time do you usually spend on your phone/laptop during the hour before sleeping?",
    "How many caffeinated drinks do you usually consume per day?",
    "On average, how many hours do you study outside classroom hours per day?",
]


def predict(features: dict, model_path: Path | None = None) -> int:
    """Return the model's predicted 1–5 productivity rating for one student."""
    root = Path(__file__).resolve().parents[1]
    model_path = model_path or root / "models" / "final_classroom_productivity_model.pkl"
    missing = [name for name in FEATURES if name not in features]
    if missing:
        raise ValueError(f"Missing required feature(s): {', '.join(missing)}")
    model = joblib.load(model_path)
    row = pd.DataFrame([{name: features[name] for name in FEATURES}], columns=FEATURES)
    return int(model.predict(row)[0])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sleep-duration", required=True)
    parser.add_argument("--bedtime", required=True)
    parser.add_argument("--schedule-consistency", required=True, type=int)
    parser.add_argument("--late-study-frequency", required=True)
    parser.add_argument("--sleep-quality", required=True, type=int)
    parser.add_argument("--lecture-sleepiness", required=True)
    parser.add_argument("--screen-time", required=True)
    parser.add_argument("--caffeine", required=True)
    parser.add_argument("--study-hours", required=True)
    parser.add_argument("--model", type=Path, help="Optional path to a compatible saved model")
    args = parser.parse_args()
    values = dict(zip(FEATURES, [
        args.sleep_duration, args.bedtime, args.schedule_consistency,
        args.late_study_frequency, args.sleep_quality, args.lecture_sleepiness,
        args.screen_time, args.caffeine, args.study_hours,
    ]))
    print(predict(values, args.model))


if __name__ == "__main__":
    main()
