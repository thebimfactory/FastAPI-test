from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

API_KEY = "TBF-123"
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

app = FastAPI()

async def get_api_key(api_key: str = Security(api_key_header)):
    if api_key == API_KEY:
        return api_key
    else:
        raise HTTPException(
            status_code=403,
            detail="Could not validate credentials",
        )


@app.get("/calculate")
async def calculate(a: int, b: int, api_key: str = Depends(get_api_key)):
    addition = a + b
    multiplication = a * b
    return {
        "message": "Hello, World",
        "addition_result": addition,
        "multiplication_result": multiplication
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
