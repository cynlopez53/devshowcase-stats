from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to DevShowcase"}

@app.post("/run")
async def run_agent(request: Request):
    data = await request.json()
    user_input = data.get("input", "")
    
    # Placeholder logic — replace with your GPT or Python runner
    response = f"Processed: {user_input}"
    
    return JSONResponse(content={"response": response})
