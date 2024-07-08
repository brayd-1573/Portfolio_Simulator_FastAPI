from fastapi import FastAPI

app = FastAPI()

@app.get("/run/{strategy}")
def run_model(strategy: str):
    # Placeholder for your model invocation logic
    return {"strategy": strategy, "result": "Model results here"}
