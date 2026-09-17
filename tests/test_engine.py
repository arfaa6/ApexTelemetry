from src.engine import RaceSimulationEngine


def test_simulation_engine():
    engine = RaceSimulationEngine(initial_fuel=100.0, tire_wear=10.0)
    result = engine.predict_strategy(stint_laps=10, tire_compound="soft")

    assert "estimated_lap_time" in result
    assert result["remaining_fuel_kg"] == 82.5
    assert result["tire_wear_percentage"] > 10.0
    assert 0.0 <= result["pit_stop_probability"] <= 100.0