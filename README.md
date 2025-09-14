from fastapi import FastAPI, Request

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
async def run_agent(request: Request):
    payload = await request.json()
    code = payload.get("code", "")
    return {"response": f"Executed code: {code}"}
