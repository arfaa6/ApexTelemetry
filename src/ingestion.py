import numpy as np
import pandas as pd


def load_telemetry_csv(file_path: str) -> tuple[np.ndarray, pd.DataFrame]:
  """Ingests raw telemetry CSV logs, cleans data,

  and converts them into structured DataFrames and NumPy arrays.
  """
  df = pd.read_csv(file_path)

  # Fill missing values or drop corrupt telemetry streams
  df = df.dropna(subset=["timestamp", "speed", "rpm", "throttle"])

  # Extract key metrics into structured NumPy arrays for low-latency processing
  timestamps = df["timestamp"].to_numpy(dtype=np.float64)
  speeds = df["speed"].to_numpy(dtype=np.float32)
  throttles = df["throttle"].to_numpy(dtype=np.float32)

  return np.column_stack((timestamps, speeds, throttles)), df