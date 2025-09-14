from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to DevShowcase"}

@app.get("/credits")
def get_credits():
    return {
        "credits_remaining": 100,
        "premium_features": ["batch_run", "agent_insights"]
    }

@app.post("/run")
def run_agent(payload: dict):
    code = payload.get("code", "")
    return {"response": f"Executed code: {code}"}
