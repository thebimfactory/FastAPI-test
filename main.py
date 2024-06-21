from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

app = FastAPI()

# Định nghĩa API key header
api_key_header = APIKeyHeader(name="X-API-Key")

# Xác thực API key
def get_api_key(api_key: str = Depends(api_key_header)):
    correct_api_key = "TBF-123"  # Thay đổi giá trị này thành API key của bạn
    if api_key != correct_api_key:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

@app.get("/")
async def read_root():
    return {"message": "Xin chào bạn đến với API của TBF - Business Development Team!"}

@app.get("/add")
async def add(a: int, b: int, api_key: str = Depends(get_api_key)):
    return {"result": a + b}

@app.get("/nhan")
async def multiply(a: int, b: int, api_key: str = Depends(get_api_key)):
    return {"result": a * b}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
