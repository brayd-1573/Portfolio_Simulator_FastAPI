from fastapi import FastAPI
from numba import jit

app = FastAPI()

@jit
@app.get("/run")
async def run_model(strategy: str):
    # Placeholder for your model invocation logic
    return {"strategy": strategy, "result": "Model results here"}
