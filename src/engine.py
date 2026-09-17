import numpy as np

class RaceSimulationEngine:
    def __init__(self, initial_fuel: float, tire_wear: float):
        self.initial_fuel = initial_fuel
        self.tire_wear = tire_wear

    def predict_strategy(self, stint_laps: int, tire_compound: str) -> dict:
        compound_modifiers = {
            "soft": 1.4,
            "medium": 1.0,
            "hard": 0.7
        }
        modifier = compound_modifiers.get(tire_compound.lower(), 1.0)

        simulated_wear = min(100.0, self.tire_wear + (stint_laps * 1.5 * modifier))
        fuel_burned = stint_laps * 1.75
        remaining_fuel = max(0.0, self.initial_fuel - fuel_burned)

        base_lap_time = 88.5  # seconds
        wear_penalty = (simulated_wear / 100.0) * 3.5
        estimated_lap_time = base_lap_time + wear_penalty

        pit_probability = min(100.0, max(0.0, (simulated_wear * 0.8) + (stint_laps * 0.5)))

        # Generate lap-by-lap degradation curve for the chart
        stint_curve = []
        for lap in range(1, stint_laps + 1):
            lap_wear = min(100.0, self.tire_wear + (lap * 1.5 * modifier))
            lap_time = base_lap_time + ((lap_wear / 100.0) * 3.5)
            stint_curve.append({
                "lap": lap,
                "lap_time": round(lap_time, 3),
                "wear": round(lap_wear, 1)
            })

        return {
            "estimated_lap_time": round(estimated_lap_time, 3),
            "remaining_fuel_kg": round(remaining_fuel, 2),
            "tire_wear_percentage": round(simulated_wear, 1),
            "pit_stop_probability": round(pit_probability, 1),
            "stint_curve": stint_curve
        }