from fastapi import APIRouter, Request, HTTPException # type: ignore
import modules.load_data
import modules.data_analysis
import time
from datetime import datetime

router = APIRouter()

# Carrega os dados
data_analysis = modules.data_analysis.DataAnalysis(modules.load_data.get_data())

@router.get("/teams")
def get_top_countries():
    start_time = time.time()
    teams_insights = data_analysis.get_team_insights()
    end_time = time.time()
    execution_time_ms = int((end_time - start_time) * 1000)

    return {
        "timestamp": datetime.now().isoformat() + "Z",
        "execution_time_ms": execution_time_ms,
        "data": teams_insights
    }
