from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
import pandas as pd
import numpy as np

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
        
        
@app.get("/")
async def read_root():
    return {"Xin chào bạn đến với API của TBF - Business Development Team!"}


# @app.get("/calculate")
# async def calculate(a: int, b: int, api_key: str = Depends(get_api_key)):
#     addition = a + b
#     multiplication = a * b
#     return {
#         "Cong": addition,
#         "Nhan": multiplication
#     }
    

# Số hàng và cột
num_rows = 10
num_columns = 3

# Tạo dữ liệu ngẫu nhiên
data = np.random.randint(0, 101, size=(num_rows, num_columns))

# Tạo bảng với pandas
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3'])


# Chuyển bảng thành dạng JSON
json_data = df.to_json(orient='records')


@app.get("/table")
async def table(api_key: str = Depends(get_api_key)):
    return json_data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
