"""Reusable model helpers for loading artefacts and making predictions."""

from __future__ import annotations

import pickle
from typing import Any

import numpy as np


def load_artefacts(model_path: str, scaler_path: str) -> tuple[Any, Any]:
    """Load a trained model and scaler from disk."""

    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)

    with open(scaler_path, "rb") as scaler_file:
        scaler = pickle.load(scaler_file)

    return model, scaler


def predict(model: Any, scaler: Any, features: np.ndarray, threshold: float = 0.5) -> tuple[float, str]:
    """Scale features and return the probability plus a risk label."""

    scaled_features = scaler.transform(features)
    probability = model.predict_proba(scaled_features)[0][1]
    label = "High Risk" if probability > threshold else "Low Risk"
    return probability, label
