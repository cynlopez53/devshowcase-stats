from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to DevShowcase"}

@app.post("/run")
async def run(request: Request):
    try:
        data = await request.json()
        code = data.get("code", "")
        if not code:
            return JSONResponse(content={"error": "No code provided"}, status_code=400)
        response = f"Executed code: {code}"
        return JSONResponse(content={"response": response})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
