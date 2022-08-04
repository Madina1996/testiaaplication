from pydantic import BaseModel

class Param(BaseModel):
    x: float
    y: float
    month: float
    is_weekend: float
    ffmc: float
    dmc: float
    dc: float
    isi: float
    temp: float
    rh: float
    wind: float
    rain: float
    area: float
    class Config:
        schema_extra = {
            "example": {
                "x": 0.543265,
                "y": 0.603791,
                "month": -1.086576,
                "is_weekend": -1.843925,
                "ffmc": -1.382185 ,
                "dmc":  -1.753655,
                "dc": -1.753655,
                "isi": -1.007520,
                "temp": -1.294117 ,
                "rh": 3.352501,
                "wind": 0.439642,
                "rain": -0.137348,
                "area": -0.769306
            }
        }