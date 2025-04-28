from fastapi import APIRouter, Request, HTTPException # type: ignore
import modules.load_data
import modules.data_analysis
import time
from datetime import datetime

router = APIRouter()

# Carrega os dados
data_analysis = modules.data_analysis.DataAnalysis(modules.load_data.get_data())

@router.get("/top-countries")
def get_top_countries():
    start_time = time.time()
    top_countries = data_analysis.get_top_countries()
    end_time = time.time()
    execution_time_ms = int((end_time - start_time) * 1000)

    return {
        "timestamp": datetime.now().isoformat() + "Z",
        "execution_time_ms": execution_time_ms,
        "data": top_countries
    }
