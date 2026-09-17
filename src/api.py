from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pathlib import Path
from src.engine import RaceSimulationEngine

app = FastAPI(
    title="Motorsport Race Strategy API",
    version="1.0.0",
    description="Real-time race predictions and telemetry stream API",
)

# Mount static files directory for the professional dashboard UI
current_dir = Path(__file__).parent
static_dir = current_dir / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


class SimulationRequest(BaseModel):
    initial_fuel: float = 100.0
    tire_wear: float = 0.0
    stint_laps: int = 15
    tire_compound: str = "medium"


@app.get("/", response_class=HTMLResponse)
def read_root():
    """Serves the professional ApexTelemetry control dashboard."""
    index_file = static_dir / "index.html"
    if index_file.exists():
        return index_file.read_text(encoding="utf-8")
    return "<h1>Motorsport API Running. Dashboard UI file not found.</h1>"


@app.post("/api/v1/simulate-strategy")
def simulate_strategy(payload: SimulationRequest):
    engine = RaceSimulationEngine(
        initial_fuel=payload.initial_fuel, tire_wear=payload.tire_wear
    )
    result = engine.predict_strategy(
        stint_laps=payload.stint_laps, tire_compound=payload.tire_compound
    )
    return {"status": "success", "data": result}


@app.get("/api/v1/telemetry-stream")
def telemetry_stream():
    return {"status": "streaming", "message": "Live telemetry feed active"}