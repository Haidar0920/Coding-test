from fastapi import FastAPI
from pydantic import BaseModel
from calculate import Calculate
import uvicorn


class CalcData(BaseModel):
    loan_sum: float
    period: int
    rate: float


app = FastAPI()


@app.post("/calculate/")
async def make_calc(data: CalcData):
    return {"full_sum": round(Calculate.calculate(**data.dict()), 2)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
